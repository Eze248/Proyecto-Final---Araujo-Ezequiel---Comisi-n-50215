from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    #Clientes
    path('clientes/', ClienteList.as_view() , name = "clientes"),
    path('clientes_create/', ClienteCreate.as_view() , name = "clientes_create"),
    path('clientes_s/', clientes_s , name = "clientes_s"),
    path('clientes_e/', ClienteList1.as_view() , name = "clientes_e"),
    #Empleados
    path('empleados/', EmpleadoList.as_view() , name = "empleados"),
    path('empleados_create/', EmpleadoCreate.as_view() , name = "empleados_create"),
    path('empleados_s/', empleados_s , name = "empleados_s"),
    path('empleados_e/', EmpleadoList1.as_view() , name = "empleados_e"),
    #Productos
    path('productos/', ProductoList.as_view() , name = "productos"),
    path('productos_create/', ProductoCreate.as_view() , name = "productos_create"),
    path('productos_s/', productos_s , name = "productos_s"),
    path('productos_e/', ProductoList1.as_view() , name = "productos_e"),
    #Transacciones
    path('transacciones/', TransaccionList.as_view() , name = "transacciones"),
    path('transacciones_create/', TransaccionCreate.as_view() , name = "transacciones_create"),
    path('transacciones_s/', transacciones_s , name = "transacciones_s"),
    path('transacciones_e/', TransaccionList1.as_view() , name = "transacciones_e"),
]