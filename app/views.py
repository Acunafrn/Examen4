from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from rest_framework import viewsets
from .serializers import ProductoSerializers
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

def carrito(request):
    return render(request, 'app/carrito.html')
    
@permission_required('app.view_producto')
def listar_productos(request):

    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)

@permission_required('app.add_producto')
def agregar_productos(request):

    data = {
        'form': ProductoForm()
    }

    if request.method =='POST':
        formulario=ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.change_producto')
def modificar_productos(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)

    producto.delete()

    return redirect(to="listar_producto")






