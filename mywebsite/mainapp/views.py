from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.templatetags.static import static

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

def shop_logged(request) :
    return render(request, 'shop.html', {'logged':True})

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
    # try:
    category_copa = Category.objects.get(pk=1)    
    product_stock = Product.objects.filter(category=category_copa) 
    if(product_stock.count() != 0):
        return render(request, 'shop_category.html', {'product_list': product_stock, 'category':category_copa,'available': True})
    else:
        return render(request, 'shop_category.html', {'available': False})
    # eXcept:
    #     return HttpResponse("Terjadi Error")

def shop_adidasx(request):
    try:
        category_x = Category.objects.get(pk=2)    
        product_stock = Product.objects.filter(category=category_x)
              
        if(product_stock.count() != 0):
            return render(request, 'shop_category.html', {'product_list': product_stock,'category':category_x,'available': True})
        else:
            return render(request, 'shop_category.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")

def shop_adidaspredator(request):
    try:
        category_predator = Category.objects.get(pk=3)    
        product_stock = Product.objects.filter(category=category_predator)
              
        if(product_stock.count() != 0):
            return render(request, 'shop_category.html', {'product_list': product_stock, 'category':category_predator, 'available': True})
        else:
            return render(request, 'shop_category.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")

def shop_popular(request):
    return render(request, 'shop_popular.html')

# def shop_signin(request):
#     return render(request, 'shop_signin.html')


def shop_signin(request):
    if(request.POST == {}):
        print("GET")
        return render(request, 'shop_signin.html')
    else:
        print(request.POST)
        account = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(account)
        if account is not None:
            login(request, account)
            # if(user.user_level == 0):
            return redirect('/shop/')
            # return redirect('/')
        else:
            return render(request, 'shop_signin.html', {'message': 'wrong username or password'})
    return render(request, 'shop_signin.html')

def shop_signout(request):
    logout(request)
    return redirect('/shop/')

def shop_signup(request):
    return render(request, 'shop_signup.html')

def shop_products(request, id_products):
    # print(request.GET)
    # print(request.GET['mainproduct_name'])
    # mainproduct = Product.objects.filter(name__=request.GET['mainproduct_name'])  
    mainproduct = Product.objects.get(pk=id_products)
    print(mainproduct)
    return render(request, 'shop_products.html', {'mainproduct': mainproduct})

def shop_search(request) :
    try:
        print(request.GET)
            # category_copa = Category.objects.get(pk=1)
            #pk == primary_key
        if(request.GET == {}):
            product_stock = Product.objects.all
        else:    
            product_stock = Product.objects.filter(name__contains=request.GET['product_name'])
            # WHERE name like 'chrome'

        #
        if(product_stock.count() != 0):
            return render(request, 'shop_search.html', {'product_list': product_stock, 'available': True})
        else:
            return render(request, 'shop_search.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")

def shop_allproducts(request):
    # try:
    #     print(request.GET)
    product_stock = Product.objects.all()
        # form = SearchForm(request.GET)
        # print(form.is_valid())
        # if(form.is_valid()):
        #     product_laptop = Product.objects.filter(
        #     name__contains=request.GET['product_name'])
        # else:
        #     return render(request, 'shop_allproducts.html', {'available': False})

    if(product_stock.count() != 0):
        return render(request, 'shop_allproducts.html', {'product_list': product_stock, 'available': True})
    else:
        return render(request, 'shop_allproducts.html', {'available': False})
    # except:
    #     return HttpResponse("Terjadi Error")

def shop_allproducts_filter(request):
    # try:
    print(request.GET)
    # product_stock = Product.objects.all()
    form = SearchForm(request.GET)
    print(form.is_valid())
    min = request.GET['price_min']
    max = request.GET['price_max']
    if(form.is_valid()):
        product_stock = Product.objects.filter()
        if(product_stock.count() != 0):
            return render(request, 'shop_allproducts.html', {'product_list': product_stock, 'available': True})
        else:
            return render(request, 'shop_allproducts.html', {'available': False})
    else:        
        return render(request, 'shop_allproducts.html', {'available': False})
    
    # except:
    #     return HttpResponse("Terjadi Error")