import datetime
import email

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# from HMS.core.models import PatientProfile
from core.models import PatientProfile, DoctorProfile
from .forms import psup, dsup


def psignup(request):
    gnbg = psup()
    data = {'form': gnbg}
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
                                                            last_name=lname, height=h, weight=w, gender=g, bloodgroup=b
                                                            , birthdate=bd)
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
        return render(request, 'psignup.html', data)


def dsignup(request):
    gnbg = dsup()
    data = {'form': gnbg}
    if request.method == 'POST':
        username = (str(DoctorProfile.objects.count() + 1) + 'D')
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        g = request.POST['gender']
        b = request.POST['bloodgroup']
        bd = request.POST['birthdate']
        speciality = request.POST['speciality']
        wa = request.POST['work_address']
        pn = request.POST['phone_number']
        c = request.POST['certificate']

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

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = DoctorProfile.objects.create(user=user_model, id_user=user_model.id, first_name=fname,
                                                           last_name=lname, gender=g, bloodgroup=b
                                                           , birthdate=bd, speciality=speciality, work_address=wa,
                                                           phone_number=pn, certificate=c)
                new_profile.save()

                send_mail('Warm Welcome to HMS',
                          "hello doctor, " + fname + " " + lname + " how are you?" + " Your username is: " + username + ".",
                          'djangoautomailsystem@gmail.com',
                          [email], fail_silently=False)

                return redirect('doctorhome')
        else:
            messages.info(request, 'Password not matching')
            return redirect('dsignup')


    else:
        return render(request, 'dsignup.html', data)


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
                return redirect('doctorhome')
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
def doctorhome(request):
    return render(request, 'doctorhome.html')

def signup(request):
    return render(request, 'signup.html')