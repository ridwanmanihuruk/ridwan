from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as plt

# Create your views here.
def landig_page(request):
    return HttpResponse('Hello Ridwan Haay')

def second_page(request):
    angka = 100
    return HttpResponse(angka)

def tabel_page(request):
    a = [1,2,4,6,8,4,7,9]
    b = [11,12,13,14,15,16,17,18,19]
    return HttpResponse(a)

def example(request):
    return render(request, 'example.html')

def newpage(request):
    return HttpResponse("new")

def a(request):
    return HttpResponse()

def shop(request) :
    return render(request, 'shop.html')

def firstpage(request) :
    return render(request, 'firstpage.html')

def secondpage(request) :
    return render(request, 'secondpage.html')

def shop_laptop(request):
    return render(request, 'shop_laptop.html')


def shop_console(request):
    return render(request, 'shop_console.html')


def shop_smartphone(request):
    return render(request, 'shop_smartphone.html')

def shop_adidascopa(request) :
    return render(request, 'shop_adidascopa.html')

def shop_adidasx(request):
    return render(request, 'shop_adidasx.html')

def shop_adidaspredator(request):
    return render(request, 'shop_adidaspredator.html')

def shop_popular(request):
    return render(request, 'shop_popular.html')

def shop_signin(request):
    return render(request, 'shop_signin.html')

def shop_signup(request):
    return render(request, 'shop_signup.html')