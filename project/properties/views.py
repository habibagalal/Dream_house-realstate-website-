from django.shortcuts import render
from django.http import Http404
from .models import Property
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import UploadedProb
from .models import Property


# def property(request):
#     the_Property = Property.objects.all()

#     return render(request, 'pages/index.html', {'house': the_Property})


# def detail(request):
#     Notes = Property.objects.all()
#     return render(request, 'pages/details_page.html', {'note': Notes})


class Details(TemplateView):
    template_name = 'details_page.html'


class HouseView(ListView):

    template_name = 'details_page.html'
    model = Property
    context_object_name = "houses"


class HouseDetails(DetailView):
    model = Property
    context_object_name = "house"
    template_name = 'details_page.html'


class Sell12(TemplateView):
    template_name = 'sell1,2.html'


class Sell3(TemplateView):
    template_name = 'sell 3.html'


class Sell4(TemplateView):
    template_name = 'sell-4.html'


class Filter(TemplateView):
    template_name = 'onboaded i.html'


class Filter2(TemplateView):
    template_name = 'onboaded ii.html'


class Filter3(TemplateView):
    template_name = 'onboaded iii.html'


class ThankYou(TemplateView):
    template_name = 'thank_you.html'


def upload(request):
    if request.method == 'POST':
        images = ['']

        new = UploadedProb.objects.create_new(images=images)

    else:
        return(request, 'pages/index.html')
