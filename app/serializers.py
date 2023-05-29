from dataclasses import fields
from pyexpat import model
from .models import Producto
from rest_framework import serializers


class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'