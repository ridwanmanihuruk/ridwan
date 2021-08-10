from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('tabel/', views.tabel_page),
    path('shop/', views.shop),
    path('firstpage/', views.firstpage),
    path('secondpage/', views.secondpage),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landig_page),
]