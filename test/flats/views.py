from django.shortcuts import render
from.models import House

# Create your views here.


def house(request):
    return render(request, 'pages/index.html', {'h': House.objects.all()})
