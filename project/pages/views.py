from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def result(request):
    return render(request, 'pages/result.html')


def login(request):
    return render(request, 'pages/create_account.html')


def setting(request):
    return render(request, 'pages/settings.html')


def details(request):
    return render(request, 'pages/details_page.html')


def about(request):
    return render(request, 'pages/aboutUs.html')


def sell(request):
    return render(request, 'pages/sell 3.html')


def feature(request):
    return render(request, 'pages/index.html')
