from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('dsignup', views.dsignup, name='dsignup'),
    path('psignup', views.psignup, name='psignup'),
    path('login', views.login, name='login'),
    path('patienthome', views.patienthome, name='patienthome'),
    path('doctorhome', views.doctorhome, name='doctorhome'),
]