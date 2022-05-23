from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('login/', views.login, name='login'),
    path('setting/', views.setting, name='setting'),
    path('details/', views.details, name='details'),
    path('about/', views.about, name='about'),
    path('sell/', views.sell, name='sell'),
    path('feature/', views.feature, name='feature'),

]
