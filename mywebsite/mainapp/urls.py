from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landig_page),
]