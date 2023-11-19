from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    #Navbar
    path('login', views.login, name='login'),
    path('diabetesinfo',views.diabetesinfo,name='diabetesinfo'),
    path('heartinfo',views.heartinfo,name = 'heartinfo'),
    path('logout', views.logout, name='logout'),
    path('', views.homepage, name='homepage'),
    path('signup', views.signup, name='signup'),
    

    #Signup page
    path('dsignup', views.dsignup, name='dsignup'),
    path('psignup', views.psignup, name='psignup'),

    #Profile URLs
    path('patienthome', views.patienthome, name='patienthome'),
    path('doctorhome', views.doctorhome, name='doctorhome'),

    #ML Model urls
    path('predictdiabetes/', views.predictor_diab, name='predictdiabetes'),
    path('predictdiabetes/result/', views.formInfo_diab, name='resultdiabetes'),
    path('predictdiabetes/result/diabetes_pdf', views.diabetes_pdf, name='diabetes_pdf'),
    path('predictheart/', views.predictor_heart, name = 'predictheart'),
    path('predictheart/result/', views.formInfo_heart, name='resultheart'),
    path('predictheart/result/heartreport_pdf', views.heartreport_pdf, name='heartreport_pdf'),

    #Report download
    path('doctorreport', views.doctorreport, name='doctorreport'),
    path('report', views.downloadreport, name='downloadreport'),

    #Jugaad 
    path('predictdiabetes/result/homepage2', views.homepage2, name='homepage2'),
    path('predictdiabetes/homepage2', views.homepage2, name='homepage2'),
    path('predictheart/homepage2', views.homepage2, name='homepage2'),
    path('predictheart/result/homepage2', views.homepage2, name='homepage2'),

    #Forgot Password
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('accounts/login/', views.alt_way, name="alt_way"),


]




