from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.profile.views import HomeView, activate, signup


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),
]
