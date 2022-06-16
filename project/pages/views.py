from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from project import settings
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from datetime import datetime


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    extra_content = {'today': datetime.today()}


class AboutUs(TemplateView):
    template_name = 'aboutUs.html'


class Setting(TemplateView):
    template_name = 'settings.html'
