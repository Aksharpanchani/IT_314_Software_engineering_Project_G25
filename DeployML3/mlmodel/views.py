from django.shortcuts import render, redirect 
from django.http import HttpResponse

from joblib import load
diab_model = load('./SavedModels/diabetes_model.joblib')
# heart_model = load('./SavedModels/heart_model.joblib')

def home(request):
    return HttpResponse('Helo')


#Views of Diabetes
def predictor_diab(request):
    return render(request,'mlmodel/form_diab.html')

def formInfo_diab(request):

    HighBP = request.GET['HighBP']
    if HighBP=='No':
        HighBP=1
    else:
        HighBP=0
    print(HighBP)
    HighChol = request.GET['HighChol']
    BMI = request.GET['BMI']
    Stroke = request.GET['Stroke']
    HeartDiseaseorAttack = request.GET['HeartDiseaseorAttack']
    GenHlth = request.GET['GenHlth']
    Age = request.GET['Age']
    y_pred = diab_model.predict_proba([[HighBP,HighChol,BMI,Stroke,HeartDiseaseorAttack,GenHlth,Age]])
    y_pred = y_pred*100
    return render(request,'mlmodel/result_diab.html',{'data':y_pred[0][1]})


#Views of Heart Disease
def predictor_heart(request):
    return render(request,'mlmodel/form_heart.html')

def formInfo_heart(request):

    age = request.GET['Age']
    height = request.GET['Height']
    weight = request.GET['Weight']
    ap_hi = request.GET['Systolic BP']
    ap_lo = request.GET['Diastolic BP']
    cholestrol = request.GET['Cholestrol Level']
    glucose = request.GET['Glucose Level']
    smoking = request.GET['Smoking']
    active = request.GET['PhysicalActivity']

    y_pred = heart_model.predict_proba([[age,height,weight,ap_hi,ap_lo,cholestrol,glucose,smoking,active]])
    y_pred = y_pred
    return render(request,'mlmodel/result_heart.html',{'data':y_pred[0][1]})