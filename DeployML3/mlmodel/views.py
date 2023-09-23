from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np

def home(request):
   return HttpResponse('helo')
def diabetes(request):
   return render(request, 'diabetes.html')
def result(request):
   return HttpResponse('Helo')
   # cls=joblib.load('model.sav')
   # lis=[]
   # lis.append(request.GET['HighBP'])
   # lis.append(request.GET['HighChol'])
   # lis.append(request.GET['HeartDiseaseorAttack'])
   # lis.append(request.GET['BMI'])
   # lis.append(request.GET['Income'])
   # lis.append(request.GET['GenHlth'])
   # lis.append(request.GET['Age'])
   # #print(lis)
   # data_array = np.asarray(lis)
   # arr= data_array.reshape(1,-1)
   # ans = cls.predict(arr)
   # print(ans)
   # finalans=''
   # if(ans==1):
   #    finalans='You may have diabetes'
   # elif(ans==0):
   #    finalans = 'You do not have diabetes'
   # return render(request, "result.html",{'ans':finalans})

from .forms import PatientForm2, PatientForm
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Patient2, Patient
from .serializer import PatientSerializers2, PatientSerializers


import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class PatientView2(viewsets.ModelViewSet): 
    queryset = Patient2.objects.all() 
    serializer_class = PatientSerializers2 

class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers




# Form 2
def status2(df):
    try:
        scaler=pickle.load(open("D:\\5 sem\\IT-314 SE\\Project\\Backend\\New folder\\DeployML3\\mlmodel\\Scaler.sav", 'rb'))
        model=pickle.load(open("D:\\5 sem\\IT-314 SE\\Project\\Backend\\New folder\\DeployML3\\mlmodel\\Prediction2.sav", 'rb'))
        X = scaler.transform(df) 
        y_pred = model.predict(X) 
        y_pred=(y_pred>0.80) 
        result = "Yes" if y_pred else "No"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView2(request):
    if request.method=='POST':
        form2=PatientForm2(request.POST or None)

        if form2.is_valid():
            Gender = form2.cleaned_data['gender']
            Age = form2.cleaned_data['age']
            EstimatedSalary = form2.cleaned_data['salary']
            df=pd.DataFrame({'gender':[Gender], 'age':[Age], 'salary':[EstimatedSalary]})
            df["gender"] = 1 if "male" else 2
            result = status2(df)
            return render(request, 'mlmodel/result.html', {"data": result}) 
            
    form2=PatientForm2()
    return render(request, 'mlmodel/form2.html', {'form2':form2})



# Form 1

def status(df):
    try:
        scaler=pickle.load(open("D:\\5 sem\\IT-314 SE\\Project\\Backend\\New folder\\DeployML3\\mlmodel\\Scaler.sav", 'rb'))
        model=pickle.load(open("D:\\5 sem\\IT-314 SE\\Project\\Backend\\New folder\\DeployML3\\mlmodel\\Prediction.sav", 'rb'))
        #X = scaler.transform(df) 
        X=df
        y_pred = model.predict(X) 
        y_pred=(y_pred>0.80) 
        result = "Yes" if y_pred else "No"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def FormView(request):
    model = pickle.load(open("D:\\5 sem\\IT-314 SE\\Project\\Backend\\New folder\\DeployML3\\mlmodel\\Prediction2.sav", 'rb'))
    if request.method=='POST':
        form=PatientForm(request.POST or None)

        if form.is_valid():   

            HighBP = 1 if request.form.get('HighBP') else 0
            HighChol = 1 if request.form.get('HighChol') else 0
            HeartDiseaseorAttack = 1 if request.form.get('HeartDiseaseorAttack') else 0
            BMI = float(request.form['BMI'])
            Income = float(request.form['Income'])
            GenHlth = float(request.form['GenHlth'])
            Age = float(request.form['Age'])

            # Prepare input data
            data = [HighBP, HighChol, BMI, Income, HeartDiseaseorAttack, GenHlth, Age]

            # Predict
            prediction = model.predict([data])[0]

            return render(request, 'mlmodel/result.html', {"data": prediction})
    form=PatientForm()
    return render(request, 'mlmodel/form.html', {'form':form})