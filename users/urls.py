from django.urls import path
from users import views
from django.views.generic import TemplateView

from .views import *


app_name = 'users'

urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('success/', TemplateView.as_view(template_name='users/success_registration.html'), name='success'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('ver_perfil/', ver_perfil, name='ver_perfil'),
]