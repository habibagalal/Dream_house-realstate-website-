from django.shortcuts import render
from.models import Property, Profile

# Create your views here.


def property(request):
    x = request.POST.get('name')
    print(x)
    return render(request, 'pages/index.html', {'pro': Property.objects.all().filter(name="Stephanie Mckenzie")})


def search(request):
    return render(request, 'pages/index.html', {'search': Property.objects.get(name="Stephanie Mckenzie")})
