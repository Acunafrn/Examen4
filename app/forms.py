from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'