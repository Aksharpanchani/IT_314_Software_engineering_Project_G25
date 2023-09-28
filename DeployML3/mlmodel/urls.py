#urls.py in mlmodel
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
   path('',views.home,name='home'),
   path('predictor/',views.predictor,name = 'predictor'),
   path('predictor/result/',views.formInfo,name='result'),
   
]