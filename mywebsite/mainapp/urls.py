from django.urls import path
from django.urls.resolvers import URLPattern
from . import views, api

urlpatterns = [
    path('tabel/', views.tabel_page),
    path('shop/', views.shop),
    # path('shop/logged/', views.shop_logged),
    path('firstpage/', views.firstpage),
    path('secondpage/', views.secondpage),
    path('shop/adidascopa/', views.shop_adidascopa),
    path('shop/search/', views.shop_search),
    path('shop/popular/', views.shop_popular),
    path('shop/adidaspredator/', views.shop_adidaspredator),
    path('shop/signin/', views.shop_signin),
    # path('shop/signed/', views.shop_signed),
    path('shop/signout/', views.shop_signout),
    path('shop/signup/', views.shop_signup),
    path('shop/adidasx/', views.shop_adidasx),
    path('shop/products/<int:id_products>', views.shop_products),
    path('shop/allproducts/', views.shop_allproducts),
    path('shop/allproducts/filter/', views.shop_allproducts_filter),
    path('example/', views.example),
    path('second/', views.second_page),


    path('api/category/get-all/', api.get_categories),
    path('api/product/get-all/', api.get_products),
    path('api/category/create/', api.create_categories),
    path('api/review/create/', api.create_review),



    path('', views.landig_page),
]


