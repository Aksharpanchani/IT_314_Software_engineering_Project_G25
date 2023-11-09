import datetime
import email

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# from HMS.core.models import PatientProfile
from core.models import PatientProfile, DoctorProfile, Report
# from .forms import psup, dsup


def psignup(request):
    # gnbg = psup()
    # data = {'form': gnbg}
    if request.method == 'POST':
        username = (str(PatientProfile.objects.count() + 1) + 'P')
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        w = request.POST['weight']
        h = request.POST['height']
        g = request.POST['gender']
        b = request.POST['bloodgroup']
        bd = request.POST['birthdate']
        pn = request.POST['number']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('psignup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('psignup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in and redirect to settings page

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = PatientProfile.objects.create(user=user_model, id_user=user_model.id, first_name=fname,
                                                            last_name=lname, height=h, weight=w, gender=g, bloodgroup=b,
                                                            phone_number=pn, birthdate=bd)
                new_profile.save()

                send_mail('Warm Welcome to HMS',
                          "hello, " + fname + " " + lname + " how are you?" + " Your username is: " + username + ".",
                          'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('patienthome')
        else:
            messages.info(request, 'Password not matching')
            return redirect('psignup')


    else:
        return render(request, 'psignup.html')


def dsignup(request):
    # gnbg = dsup()
    # data = {'form': gnbg}
    if request.method == 'POST':

        username = (str(DoctorProfile.objects.count() + 1) + 'D')
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        g = request.POST['gender']
        bd = request.POST['birthdate']
        speciality = request.POST['speciality']
        wa = request.POST['work_address']
        pn = request.POST['number']
        certi = request.FILES.get('certificate')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('dsignup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('dsignup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in and redirect to settings page

                # user_login = auth.authenticate(username=username, password=password)
                # auth.login(request, user_login)

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = DoctorProfile.objects.create(user=user_model, id_user=user_model.id, first_name=fname,
                                                           last_name=lname, gender=g, birthdate=bd, speciality=speciality, work_address=wa,
                                                           phone_number=pn, certificate=certi)
                new_profile.save()

                send_mail('Warm Welcome to HMS',
                          "hello doctor, " + fname + " " + lname + " how are you?" + " Your username is: " + username + ". " + "Your profile will be verified after 2-3 business days.",
                          'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('homepage')
        else:
            messages.info(request, 'Password not matching')
            return redirect('dsignup')

    else:
        return render(request, 'dsignup.html')


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            s = str(username)
            if s[len(s) - 1] == 'P':
                return redirect('patienthome')
            else:
                if DoctorProfile.objects.get(user=user).Verified == True:
                    return redirect('doctorhome')
                else:
                    messages.info(request, 'Your profile is yet to be verified')
                    return redirect('login')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


# @login_required(login_url='login')
def homepage(request):
    # user_profile = Profile.objects.get(user=request.user)
    # posts = Post.objects.all()
    # liked_posts = LikePost.objects.filter(username=request.user).values()
    # if len(posts) != 0:
    #     return render(request, 'home.html',
    #                   {'user_profile': user_profile, 'posts': posts, 'liked_posts': liked_posts})
    # else:
    #     return render(request, 'nopost.html')
    return render(request, 'homepage.html')


@login_required(login_url='login')
def patienthome(request):
    return render(request, 'patienthome.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def doctorhome(request):
    doctor_profile = DoctorProfile.objects.get(user=request.user)
    return render(request, 'doctorhome.html', {'DoctorProfile': doctor_profile})

def signup(request):
    return render(request, 'signup.html')









from joblib import load




#Views of Diabetes
def predictor_diab(request):
    doctor_profile=DoctorProfile.objects.get(user=request.user)

    return render(request,'form_diab.html',{'DoctorProfile':doctor_profile})

def formInfo_diab(request):
    diab_model = load('./SavedModels/diabetes_model.joblib')
    
    doctor_profile=DoctorProfile.objects.get(user=request.user)
    PatientID = request.GET['PatientID']
    patient_profile = PatientProfile.objects.get(user=User.objects.get(username=PatientID))
    DiseaseName = 'Diabetes'

    HighBP = request.GET['HighBP']
    if HighBP=='No':
        HighBPML=0
    else:
        HighBPML=1
    
    HighChol = request.GET['HighChol']


    if HighChol=='No':
        HighCholML=0
    else:
        HighCholML=1

    BMI = request.GET['BMI']

    Stroke = request.GET['Stroke']
    if Stroke=='No':
        StrokeML=0
    else:
        StrokeML=1


    HeartDiseaseorAttack = request.GET['HeartDiseaseorAttack']
    if HeartDiseaseorAttack=='No':
        HeartDiseaseorAttackML=0
    else:
        HeartDiseaseorAttackML=1


    GenHlth = request.GET['GenHlth']
    switcher = {
        "1": 1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
    }
    GenHlthML = switcher.get(GenHlth)
    Age = request.GET['Age']
    Age= int(Age)

    if Age<=24:
        AgeML=1
    elif Age<=29:
        AgeML=2
    elif Age<=34:
        AgeML=3
    elif Age<=39:
        AgeML=4
    elif Age<=44:
        AgeML=5
    elif Age<=49:
        AgeML=6
    elif Age<=54:
        AgeML=7
    elif Age<=59:
        AgeML=8
    elif Age<=64:
        AgeML=9
    elif Age<=69:
        AgeML=10
    elif Age<=74:
        AgeML=11
    elif Age<=79 :
        AgeML=12
    else:
        AgeML=13
    
    

    #print(HighBP,HighChol, HeartDiseaseorAttack,GenHlth,Age,Stroke,BMI,PatientID,DiseaseName)


    y_pred = diab_model.predict_proba([[HighBPML,HighCholML,BMI,StrokeML,HeartDiseaseorAttackML,GenHlthML,AgeML]])
    y_pred = y_pred*100

    y_out= round(y_pred[0][1],2)

    #Save model here
    new_report = Report.objects.create(doctor=doctor_profile, patient=patient_profile, disease=DiseaseName, HighBP=HighBPML,
                                       HighChol=HighCholML, BMI=BMI, Stroke=StrokeML, HeartDiseaseAttack=HeartDiseaseorAttackML,
                                       GenHlth=GenHlthML, Age=AgeML, Result=y_out)
    report_id = new_report.id

    #df_report = [[HighBP,HighChol,BMI,Stroke,HeartDiseaseorAttack,GenHlth,Age]]

    
    return render(request,'result_diab.html',{'data':y_out, 'DoctorProfile':doctor_profile,'PatientID':PatientID ,'DiseaseName':DiseaseName,'HighBP':HighBP,'HighChol':HighChol ,'BMI':BMI ,
                                              'Stroke':Stroke,'HeartDiseaseorAttack':HeartDiseaseorAttack,'GenHlth': GenHlth,'Age':Age, 'report_id':report_id})


#Views of Heart Disease
def predictor_heart(request):
    return render(request,'form_heart.html')

def formInfo_heart(request):
    heart_model = load('./SavedModels/heart_model.joblib')
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
    return render(request,'result_heart.html',{'data':y_pred[0][1]})


#Getting Report
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

@login_required(login_url='login')
def homepage2(request):
    return redirect('doctorhome')

def venue_pdf(request):

    #Fetching data from form
    DoctorName = request.POST['DoctorName']
    PatientID = request.POST['PatientID']
    Disease = request.POST['DiseaseName']
    HighBP = request.POST['HighBP']
    HighChol = request.POST['HighChol']
    BMI = request.POST['BMI']
    Stroke = request.POST['Stroke']
    HeartDiseaseorAttack = request.POST['HeartDiseaseorAttack']
    GenHlth = request.POST['GenHlth']
    Age = request.POST['Age']
    Prediction  = request.POST['Prediction'] #Only for model
    TrueResult = request.POST['TrueResult']
    Prescription = request.POST['Prescription']
    Verdict = request.POST['DoctorVerdict']

    Patient = PatientProfile.objects.get(user=User.objects.get(username=PatientID))
    Doctor = DoctorProfile.objects.get(user=request.user)
    report = Report.objects.filter(doctor=Doctor, patient=Patient, disease=Disease).last()


    report.DoctorPrescription = Prescription
    report.DoctorGeneralAdvice = Verdict
    if TrueResult == "Satisfied":
        report.DoctorConclusion = 1
    else:
        report.DoctorConclusion = 0

    report.save()

    #Generating PDF

    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    #List of lines

    if TrueResult=="Satisfied":
        Conclusion = "Positive"
    else:
        Conclusion = "Negative"

    lines=[
        "Doctor : " + DoctorName,
        "Disease : " + Disease,
        "Patient : " + Patient.first_name + " " + Patient.last_name,
        "Age :" + Age,
        "Blood Pressure Level: " + HighBP,
        "Cholestrol Level : " + HighChol,
        "BMI (Body Mass Index) : " + BMI,
        "Stroke : " + Stroke,
        "Symptoms of Heart Attack : " + HeartDiseaseorAttack,
        "General Health (Out of 5) : " + GenHlth,
        "Diabetes : "+Conclusion,   
        "Prescription : " + Prescription,
        "General Advice : " + Verdict
    ]

    #Loop

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    reportName = Patient.first_name + " " + Disease + " " + "Report.pdf"
    return FileResponse(buf,as_attachment=True, filename=reportName)
