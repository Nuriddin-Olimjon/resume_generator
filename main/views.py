from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes
from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.db import transaction
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from main.forms import SignUpForm
from main.utils import TokenGenerator


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    success_url = '/login/'
    success_message = 'Please confirm your email address to complete the registration'
    template_name = 'registration/register.html'


# @transaction.atomic
# def signup(request):
#     if request.method == 'GET':
#         form = SignUpForm()
    
#     elif request.method == 'POST':   
#         form = SignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             send_activation_link(request, user, 'acc_activate.html')
#             messages.success(request, 'Please confirm your email address to complete the registration')
#             return redirect('login')

#     return render(request, 'registration/register.html', {'form': form})


def send_activation_link(request, user, template):
    current_site = get_current_site(request)  
    account_activation_token = TokenGenerator()
    mail_subject = 'Activation link has been sent to your email id'  
    message = render_to_string(template, {  
        'user': user,  
        'domain': current_site.domain,  
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
        'token':account_activation_token.make_token(user),  
    })  
    to_email = user.email  
    email = EmailMessage(  
        mail_subject, message, to=[to_email]  
    )  
    email.send()


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
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')
