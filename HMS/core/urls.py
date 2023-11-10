from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('predictdiabetes/result/homepage2', views.homepage2, name='homepage2'),
    path('dsignup', views.dsignup, name='dsignup'),
    path('psignup', views.psignup, name='psignup'),
    path('login', views.login, name='login'),
    path('patienthome', views.patienthome, name='patienthome'),
    path('doctorhome', views.doctorhome, name='doctorhome'),
    path('logout', views.logout, name='logout'),
    path('', views.homepage, name='homepage'),
    path('signup', views.signup, name='signup'),

    #ML Model urls
    path('predictdiabetes/', views.predictor_diab, name='predictdiabetes'),
    path('predictdiabetes/result/', views.formInfo_diab, name='resultdiabetes'),
    path('predictdiabetes/result/venue_pdf', views.venue_pdf, name='venue_pdf'),
    path('predictheart/', views.predictor_heart, name = 'predictheart'),
    path('predictheart/result/', views.formInfo_heart, name='resultheart'),
    path('predictheart/result/heartreport_pdf', views.heartreport_pdf, name='heartreport_pdf'),

    #Jugaad 
    path('predictdiabetes/homepage2', views.homepage2, name='homepage2'),

]



