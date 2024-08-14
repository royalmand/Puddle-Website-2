from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

# ini dipake untuk call url di base html
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacypolicy, name='privacypolicy'),
    path('contact/', views.contact, name='contact'),
    path('term-of-use/', views.tou, name='tou'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]