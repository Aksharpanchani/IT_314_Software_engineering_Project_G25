import datetime
import email
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# from HMS.core.models import PatientProfile
from core.models import PatientProfile, DoctorProfile, Report
# from .forms import psup, dsup




def homepage(request):
    return render(request, 'homepage.html')

#Signup
def signup(request):
    return render(request, 'signup.html')
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
        # w = request.POST['weight']
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
                                                            last_name=lname, height=h, gender=g, bloodgroup=b,
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
        return render(request, 'users/patient/psignup.html')
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
        return render(request, 'users/doctor/dsignup.html')


@login_required(login_url='login')
def alt_way(request):
    return redirect('homepage')

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

def diabetesinfo(request):
    return render(request,'disease/diabetes/diabetesinfo.html')

def heartinfo(request):
    return render(request,'disease/heart/heartinfo.html')





@login_required(login_url='login')
def patienthome(request):
    try:
        patprof = PatientProfile.objects.get(user=request.user)
        reports = Report.objects.filter(patient=patprof)
        return render(request, 'users/patient/patienthome.html', {'patientprofile': patprof, 'reports': reports})
    except PatientProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def doctorhome(request):
    try:
        doctor_profile = DoctorProfile.objects.get(user=request.user)
        return render(request, 'users/doctor/doctorhome.html', {'DoctorProfile': doctor_profile})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')










from joblib import load




#Views of Diabetes
@login_required(login_url='login')
def predictor_diab(request):
    try:
        doctor_profile = DoctorProfile.objects.get(user=request.user)
        return render(request, 'disease/diabetes/form_diab.html', {'DoctorProfile': doctor_profile})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')


diab_model = load('./SavedModels/diabetes_model.joblib')
@login_required(login_url='login')
def formInfo_diab(request):
    
    try:
        doctor_profile=DoctorProfile.objects.get(user=request.user)
        PatientID = request.GET['PatientID']
        patientcheck = User.objects.filter(username=PatientID).count()
        if patientcheck == 0:
            messages.info(request, 'No such patient exists')
            return redirect('predictdiabetes')
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
            "1":1,
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
        elif Age<=79:
            AgeML=12
        else:
            AgeML=13



        #print(HighBP,HighChol, HeartDiseaseorAttack,GenHlth,Age,Stroke,BMI,PatientID,DiseaseName)


        y_pred = diab_model.predict_proba([[HighBPML,HighCholML,BMI,StrokeML,HeartDiseaseorAttackML,GenHlthML,AgeML]])
        y_pred = y_pred*100

        y_out= round(y_pred[0][1],2)

        #Save model here
        new_report = Report.objects.create(doctor=doctor_profile, patient=patient_profile, disease=DiseaseName, HighBP=HighBP,
                                           HighChol=HighChol, BMI=BMI, Stroke=Stroke, HeartDiseaseAttack=HeartDiseaseorAttack,
                                           GenHlth=GenHlthML, Age=Age, Result=y_out)
        report_id = new_report.id

        #df_report = [[HighBP,HighChol,BMI,Stroke,HeartDiseaseorAttack,GenHlth,Age]]


        return render(request,'disease/diabetes/result_diab.html',{'data':y_out, 'DoctorProfile':doctor_profile,'PatientID':PatientID ,'DiseaseName':DiseaseName,'HighBP':HighBP,'HighChol':HighChol ,'BMI':BMI ,
                                                  'Stroke':Stroke,'HeartDiseaseorAttack':HeartDiseaseorAttack,'GenHlth': GenHlth,'Age':Age, 'report_id':report_id})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')

#Views of Heart Disease
@login_required(login_url='login')
def predictor_heart(request):
    try:
        doctor_profile = DoctorProfile.objects.get(user=request.user)
        return render(request,'disease/heart/form_heart.html',{'DoctorProfile':doctor_profile})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')

heart_model = load('./SavedModels/heart_model.joblib')

@login_required(login_url='login')
def formInfo_heart(request):
    
    try:
        doctor_profile=DoctorProfile.objects.get(user=request.user)
        PatientID = request.GET['PatientID']

        patientcheck = User.objects.filter(username=PatientID).count()
        if patientcheck == 0:
            messages.info(request, 'No such patient exists')
            return redirect('predictheart')
        patient_profile = PatientProfile.objects.get(user=User.objects.get(username=PatientID))

        DiseaseName = "Cardio"
        Age = request.GET['Age']
        Age= int(Age)
        Height = request.GET['Height']
        Height= int(Height)
        Weight = request.GET['Weight']
        Weight = int(Weight)
        SystolicBP = request.GET['SystolicBP']  #aka ap_hi in ML model
        SystolicBP= int(SystolicBP)
        DiastolicBP = request.GET['DiastolicBP'] #aka ap_lo in ML model
        DiastolicBP= int(DiastolicBP)
        CholestrolLevel = request.GET['CholestrolLevel']
        CholestrolLevel= int(CholestrolLevel)
        GlucoseLevel = request.GET['GlucoseLevel']
        GlucoseLevel= int(GlucoseLevel)
        Smoking = request.GET['Smoking']
        PhysicalActivity = request.GET['PhysicalActivity'] #aka active in ML model

        if Smoking=='Yes':
            SmokingML = 1
        else:
            SmokingML=0

        if PhysicalActivity=='Yes':
            PhysicalActivityML = 1
        else:
            PhysicalActivityML=0

        y_pred = heart_model.predict_proba([[Age,Height,Weight,SystolicBP,DiastolicBP,CholestrolLevel,GlucoseLevel,SmokingML,PhysicalActivityML]])
        #y_pred = heart_model.predict_proba([[2,168,62,110,80,1,1,1,1]])
        y_pred = y_pred*100
        y_out = round(y_pred[0][1], 2)

        new_report = Report.objects.create(doctor=doctor_profile, patient=patient_profile, disease=DiseaseName,
                                           Height=Height, Weight=Weight, SystolicBP=SystolicBP,
                                           DiastolicBP=DiastolicBP, CholestrolLevel=CholestrolLevel, GlucoseLevel=GlucoseLevel,
                                           Smoking=Smoking, PhysicalActivity=PhysicalActivity,
                                           Age=Age, Result=y_out)

        return render(request,'disease/heart/result_heart.html',{'data':y_out,'PhysicalActivity': PhysicalActivity,'Smoking': Smoking ,'GlucoseLevel': GlucoseLevel ,
                                                   'CholestrolLevel': CholestrolLevel ,'DiastolicBP':DiastolicBP ,'SystolicBP': SystolicBP,'Weight':Weight ,'Height':Height
                                                     , 'Age':Age ,'DiseaseName': DiseaseName ,'PatientID': PatientID,'DoctorProfile':doctor_profile})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')






#Getting Report
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

@login_required(login_url='login')
def homepage2(request):
    return redirect('doctorhome')

@login_required(login_url='login')
def doctorreport(request):
    try:
        docprof = DoctorProfile.objects.get(user=request.user)
        reports = Report.objects.filter(doctor=docprof)
        return render(request, 'users/doctor/doctorreport.html', {'doctorprofile': docprof, 'reports': reports})
    except DoctorProfile.DoesNotExist:
        auth.logout(request)
        return redirect('login')
@login_required(login_url='login')
def downloadreport(request):
    try:
        report_id = request.GET.get('report_id')
        report_data = Report.objects.get(id=report_id)

        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 14)

        # List of lines
        conclusion = ""
        if report_data.DoctorConclusion == 1:
            conclusion = "Positive"
        else:
            conclusion = "Negative"

        if report_data.disease == "Diabetes":

            lines = [
                "Doctor : " + report_data.doctor.first_name + " " + report_data.doctor.first_name,
                "Disease : " + report_data.disease,
                "Patient : " + report_data.patient.first_name + " " + report_data.patient.last_name,
                "Age :" + str(report_data.Age),
                "Blood Pressure Level: " + str(report_data.HighBP),
                "Cholestrol Level : " + str(report_data.HighChol),
                "BMI (Body Mass Index) : " + str(report_data.BMI),
                "Stroke : " + str(report_data.Stroke),
                "Symptoms of Heart Attack : " + str(report_data.HeartDiseaseAttack),
                "General Health (Out of 5) : " + str(report_data.GenHlth),
                "Diabetes : " + conclusion,
                "Prescription : " + report_data.DoctorPrescription,
                "General Advice : " + report_data.DoctorGeneralAdvice
            ]

        else:

            lines = [
                "Doctor : " + report_data.doctor.first_name + " " + report_data.doctor.first_name,
                "Disease : " + report_data.disease,
                "Patient : " + report_data.patient.first_name + " " + report_data.patient.last_name,
                "Age :" + str(report_data.Age),
                "PhysicalActivity :" + report_data.PhysicalActivity,
                "Smoking: " + report_data.Smoking,
                "GlucoseLevel :" + str(report_data.GlucoseLevel),
                "CholestrolLevel :" + str(report_data.CholestrolLevel),
                "DiastolicBP :" + str(report_data.DiastolicBP),
                "SystolicBP :" + str(report_data.SystolicBP),
                "Weight :" + str(report_data.Weight),
                "Height :" + str(report_data.Height),
                "HeartDisease : " + conclusion,
                "Prescription : " + report_data.DoctorPrescription,
                "General Advice : " + report_data.DoctorGeneralAdvice
            ]

        # Loop

        for line in lines:
            textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        reportName = report_data.patient.first_name + " " + report_data.disease + " " + "Report.pdf"
        return FileResponse(buf, as_attachment=True, filename=reportName)
    except Report.DoesNotExist:
        auth.logout(request)
        return redirect('login')

@login_required(login_url='login')
def diabetes_pdf(request):

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
    report = Report.objects.filter(doctor=Doctor, patient=Patient, disease=Disease).latest('date')


    report.DoctorPrescription = Prescription
    report.DoctorGeneralAdvice = Verdict
    if TrueResult == "Satisfied":
        if float(Prediction)>50:
            report.DoctorConclusion = 1
        else:
            report.DoctorConclusion = 0
    else:
        if float(Prediction)>50:
            report.DoctorConclusion = 0
        else:
            report.DoctorConclusion = 1
        report.DoctorConclusion = 0

    report.save()



    #Saving data in the CSV file

    with open("./datasets/diabetes_retrain.csv","a",newline="") as File:

        writer = csv.writer(File)
        
        # writer.writerow(['age','height','weight','ap_hi','ap_lo','cholestrol',
        #              'gluc','smoke','active','cardio'])
        if report.HighBP=='No':
            hibp=0
        else:
            hibp=1

        if report.HighChol=='No':
            hichol=0
        else:  
            hichol=1
        
        if report.Stroke=='No':
            stroke=0
        else:
            stroke=1
        
        if report.HeartDiseaseAttack=='No':
            heartattack=0
        else:
            heartattack=1
        
        
        writer.writerow([hibp,hichol,report.BMI,stroke,heartattack,
                        report.GenHlth,report.Age,report.DoctorConclusion])

        File.close()


    #Generating PDF

    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    #List of lines

    if report.DoctorConclusion==1:
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

@login_required(login_url='login')
def heartreport_pdf(request):


    #Fetching data from form
    DoctorName = request.POST['DoctorName']
    PatientID = request.POST['PatientID']
    Disease = request.POST['DiseaseName']
    PhysicalActivity = request.POST['PhysicalActivity']
    Smoking = request.POST['Smoking']
    GlucoseLevel = request.POST['GlucoseLevel']
    CholestrolLevel = request.POST['CholestrolLevel']
    DiastolicBP = request.POST['DiastolicBP']
    SystolicBP = request.POST['SystolicBP']
    Weight = request.POST['Weight']
    Height = request.POST['Height']
    Age = request.POST['Age']

    Prediction  = request.POST['Prediction'] #Only for model
    TrueResult = request.POST['TrueResult']
    Prescription = request.POST['Prescription']
    Verdict = request.POST['DoctorVerdict']

    Patient = PatientProfile.objects.get(user=User.objects.get(username=PatientID))

    Doctor = DoctorProfile.objects.get(user=request.user)
    report = Report.objects.filter(doctor=Doctor, patient=Patient, disease=Disease).latest('date')

    report.DoctorPrescription = Prescription
    report.DoctorGeneralAdvice = Verdict
    if TrueResult == "Satisfied":
        if float(Prediction)>50:
            report.DoctorConclusion = 1
        else:
            report.DoctorConclusion = 0
    else:
        if float(Prediction)>50:
            report.DoctorConclusion = 0
        else:
            report.DoctorConclusion = 1
        report.DoctorConclusion = 0
    report.save()


    #Saving data in the CSV file

    with open("./datasets/cardio_retrain.csv","a",newline="") as File:

        writer = csv.writer(File)
        
        # writer.writerow(['age','height','weight','ap_hi','ap_lo','cholestrol',
        #              'gluc','smoke','active','cardio'])
        if report.Smoking=='Yes':
            smoking=1
        else:
            smoking=0

        if report.PhysicalActivity=='Yes':
            active = 1
        else:
            active=0
        
        writer.writerow([report.Age,report.Height,report.Weight,report.SystolicBP,report.DiastolicBP,
                        report.CholestrolLevel,report.GlucoseLevel,smoking,
                        active,report.DoctorConclusion])

        File.close()


    #Generating PDF

    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    #List of lines

    if report.DoctorConclusion==1:
        Conclusion = "Positive"
    else:
        Conclusion = "Negative"

    lines=[
        "Doctor : " + DoctorName,
        "Disease : " + Disease,
        "Patient : " + Patient.first_name + " " + Patient.last_name,
        "Age :" + Age,
        "PhysicalActivity :" + PhysicalActivity,
        "Smoking: " + Smoking,
        "GlucoseLevel :" + GlucoseLevel,
        "CholestrolLevel :" + CholestrolLevel,
        "DiastolicBP :" + DiastolicBP,
        "SystolicBP :" + SystolicBP,
        "Weight :" + Weight,
        "Height :" + Height,
        "HeartDisease : "+Conclusion,   
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




