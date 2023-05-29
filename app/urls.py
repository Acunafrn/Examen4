from django.db import router
from django.urls import path, include
from .views import listar_productos, productos, carrito, ProductoViewset, agregar_productos, modificar_productos, eliminar_productos, listar_productos
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('api/', include(router.urls)),
    path('agregar-producto/', agregar_productos, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_productos, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_productos, name="eliminar_producto"),
    path('listar-producto', listar_productos, name="listar_producto"),
    #path('', base, name="base"),
]
