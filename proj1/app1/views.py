from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .seazializers import *
# Create your views here.
@api_view(['GET'])
def productlist(request):
    post = Product.objects.all()
    serializer=ProductDetails(post,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def productclr(request):
    post=Productioncolour.objects.all()
    serializer=Productioncolor(post,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productimg(request):
    post=Productionimage.objects.all()
    serializer=Productionimg(post,many=True)
    return Response(serializer.data)
