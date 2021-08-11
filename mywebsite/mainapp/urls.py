from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('tabel/', views.tabel_page),
    path('shop/', views.shop),
    path('firstpage/', views.firstpage),
    path('secondpage/', views.secondpage),
    path('shop/laptop/', views.shop_laptop),
    path('shop/smartphone/', views.shop_smartphone),
    path('shop/adidascopa/', views.shop_adidascopa),
    path('shop/adidaspredator/', views.shop_adidaspredator),
    path('shop/adidasx/', views.shop_adidasx),
    path('shop/console/', views.shop_console),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landig_page),
]