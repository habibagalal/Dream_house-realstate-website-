from django.urls import path
from .import views

urlpatterns = [  # urls of the nav-bar

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('sell', views.sell, name='sell'),
    path('explore', views.Explore, name='Explore')
]
