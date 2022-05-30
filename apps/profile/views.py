from django.db import transaction
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes

from apps.profile.forms import SignUpForm
from apps.profile.tasks import send_activation
from utils.generators import TokenGenerator


class HomeView(TemplateView):
    template_name = 'home.html'


@transaction.atomic
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    
    elif request.method == 'POST':   
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            domain = get_current_site(request).domain
            send_activation.delay(domain, user.id, 'acc_activate.html')
            messages.success(request, 'Please confirm your email address to complete the registration')
            return redirect('home')

    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):  
    User = get_user_model()  
    account_activation_token = TokenGenerator()
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')  
        return redirect('login') 
    else:  
        return HttpResponse('Activation link is invalid!')


def send_activation_link(domain, user_id, template):
    User = get_user_model()
    user = User.objects.get(id=user_id) 
    account_activation_token = TokenGenerator()
    mail_subject = 'Activation link has been sent to your email id'  
    message = render_to_string(template, {  
        'user': user,  
        'domain': domain,  
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
        'token':account_activation_token.make_token(user),  
    })  
    to_email = user.email  
    email = EmailMessage(  
        mail_subject, message, to=[to_email]  
    )  
    email.send()
    print("Email sent successfully!")

