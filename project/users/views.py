from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    extra_content = {'today': datetime.today()}


def home(request):
    return render(request, 'pages/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']  # ('lname', "lname")
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']  # ('pass2', "pass2")

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('signin')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signin')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        myuser = User.objects.create_user(
            username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()

    return render(request, "create_account.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            fname = user.first_name

            return render(request, "pages/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signup')

    return render(request, "sign_in.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
