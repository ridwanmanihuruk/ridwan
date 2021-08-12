from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('tabel/', views.tabel_page),
    path('shop/', views.shop),
    path('shop/logged/', views.shop_logged),
    path('firstpage/', views.firstpage),
    path('secondpage/', views.secondpage),
    path('shop/laptop/', views.shop_laptop),
    path('shop/smartphone/', views.shop_smartphone),
    path('shop/adidascopa/', views.shop_adidascopa),
    path('shop/search/', views.shop_search),
    path('shop/adidaspredator/', views.shop_adidaspredator),
    path('shop/popular/', views.shop_popular),
    path('shop/signin/', views.shop_signin),
    path('shop/signup/', views.shop_signup),
    path('shop/adidasx/', views.shop_adidasx),
    path('shop/console/', views.shop_console),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landig_page),
]