from django.http.response import HttpResponseBadRequest
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
import json

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    category_json = serializers.serialize('json', categories) 
    return Response({'data': category_json})

@api_view(['GET'])
def get_products(request):
    product = Product.objects.all()
    product_json = serializers.serialize('json', product ) 
    return Response({'data': product_json})

@api_view(['POST'])
def create_categories(request):
    name = ''
    description = ''

    if(request.body != None):
        print(request.body)
        json_data_from_body = json.loads(request.body)
        name = json_data_from_body['name']
        description = json_data_from_body['description']

    model_category = Category.objects.create(name=name,description=description)
    model_category.save()
    model_json = serializers.serialize('json', [model_category]) 
    return Response({'message': 'success creating categories', 'data_created': model_json})


@api_view(['POST'])
def create_review(request):
    if(request.body != None):

        review_data = {}
        if(request.POST != {}):
            # ini dari parameter POST
            review_data['name'] = request.POST.get('name')
            review_data['email'] = request.POST.get('email')
            review_data['review'] = request.POST.get('review')
        else:
            # ini dari body
            json_data = json.loads(request.body)
            review_data['name'] = json_data['name']
            review_data['email'] = json_data['email']
            review_data['review'] = json_data['review']

        product_model = Product.objects.get(pk=1)
        review_model = Review.objects.create(
            name=review_data['name'],
            email=review_data['email'],
            review=review_data['review'],
            product=product_model,
        )
        review_model.save()
        model_json = serializers.serialize('json', [review_model])
        return Response({'message': 'success create review', 'model_created': model_json})
    else:
        return HttpResponseBadRequest("Tidak ada request")
