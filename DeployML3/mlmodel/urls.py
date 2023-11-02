#urls.py in mlmodel
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
   path('',views.home,name='home'),
   path('predictdiabetes/',views.predictor_diab,name = 'predictdiabetes'),
   path('predictdiabetes/result/',views.formInfo_diab,name='result'),
   path('predictheart/',views.predictor_heart,name = 'predictheart'),
   path('predictheart/result/',views.formInfo_heart,name='result'),
   
]