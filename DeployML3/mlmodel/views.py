from django.shortcuts import render, redirect 
from django.http import HttpResponse

from joblib import load
model = load('./SavedModels/model.joblib')

def home(request):
    return HttpResponse('Helo')

def predictor(request):
    return render(request,'mlmodel/form12.html')

def formInfo(request):

    HighBP = request.GET['HighBP']
    HighChol = request.GET['HighChol']
    BMI = request.GET['BMI']
    Stroke = request.GET['Stroke']
    HeartDiseaseorAttack = request.GET['HeartDiseaseorAttack']
    GenHlth = request.GET['GenHlth']
    Age = request.GET['Age']
    y_pred = model.predict_proba([[HighBP,HighChol,BMI,Stroke,HeartDiseaseorAttack,GenHlth,Age]])
    y_pred = y_pred
    return render(request,'mlmodel/result.html',{'data':y_pred[0][1]})

