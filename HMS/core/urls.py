from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('dsignup', views.dsignup, name='dsignup'),
    path('psignup', views.psignup, name='psignup'),
    path('login', views.login, name='login'),
    path('patienthome', views.patienthome, name='patienthome'),
    path('doctorhome', views.doctorhome, name='doctorhome'),
    path('', views.homepage, name='homepage'),
    path('signup', views.signup, name='signup'),
    path('predictdiabetes/',views.predictor_diab,name = 'predictdiabetes'),
    path('predictdiabetes/result/',views.formInfo_diab,name='result'),
    path('predictheart/',views.predictor_heart,name = 'predictheart'),
    path('predictheart/result/',views.formInfo_heart,name='result'),
    path('venue_pdf',views.venue_pdf,name='venue_pdf'),


]




