from django.shortcuts import render
from django.http import Http404
from .models import Property
from django.views.generic import TemplateView


# def property(request):
#     the_Property = Property.objects.all()

#     return render(request, 'pages/index.html', {'house': the_Property})


# def detail(request):
#     Notes = Property.objects.all()
#     return render(request, 'pages/details_page.html', {'note': Notes})


class Details(TemplateView):
    template_name = 'details_page.html'


class Sell12(TemplateView):
    template_name = 'sell1,2.html'


class Sell3(TemplateView):
    template_name = 'pages/sell 3.html'


class Sell4(TemplateView):
    template_name = 'pages/sell-4.html'


class Filter(TemplateView):
    template_name = 'pages/onboaded i.html'


class Filter2(TemplateView):
    template_name = 'pages/onboaded ii.html'


class Filter3(TemplateView):
    template_name = 'pages/onboaded iii.html'


class ThankYou(TemplateView):
    template_name = 'thank_you.html'
