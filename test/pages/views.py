from django.shortcuts import render

# Create your views here.


'''def first(request):
    x = {'name': 'ali kareem hassan', 'age': 52136874, }  # the context var
    return render(request, 'user/index.html', x)'''

# functions of the nav-bar in the home page


def home(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def sell(request):
    return render(request, 'pages/sell.html')


def Explore(request):
    return render(request, 'pages/explore.html')
