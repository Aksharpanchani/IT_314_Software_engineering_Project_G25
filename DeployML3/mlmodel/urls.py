#urls.py in mlmodel
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
   path('',views.home,name='home'),
   path('diabetes/',views.diabetes,name='diabetes'),
   path('result/',views.result,name='result'),
   path('form2/',views.FormView2,name='form2'),
   path('form/',views.FormView,name='form'),
   path('api/', include(router.urls)),
]