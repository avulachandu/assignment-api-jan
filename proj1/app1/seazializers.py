from rest_framework import serializers
from .models import *


class Productioncolor(serializers.ModelSerializer):
    class Meta:
        model=Productioncolour
        fields='__all__'

class Productionimg(serializers.ModelSerializer):
    class Meta:
        model=Productionimage
        fields='__all__'

class ProductDetails(serializers.ModelSerializer):
    productcr=Productioncolor(read_only=True,many=False)
    productimg=Productionimg(read_only=True,many=False)
    
    class Meta:
        model=Product
        fields=("id","title","description","price","unique_code","size","quality","productcr","productimg")

