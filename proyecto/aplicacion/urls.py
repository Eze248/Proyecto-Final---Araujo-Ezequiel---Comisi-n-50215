from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    #Clientes
    path('clientes/', ClienteList.as_view() , name = "clientes"),
    path('clientes_create/', ClienteCreate.as_view() , name = "clientes_create"),
    path('clientes_s/', clientes_s , name = "clientes_s"),
    path('clientes_e/', ClienteList1.as_view() , name = "clientes_e"),
    path('clientes_u/<int:pk>/', ClienteUpdate.as_view(), name = "clientes_u"),
    path('clientes_d/<int:pk>/', ClienteDelete.as_view(), name = "clientes_d"),
    #Empleados
    path('empleados/', EmpleadoList.as_view() , name = "empleados"),
    path('empleados_create/', EmpleadoCreate.as_view() , name = "empleados_create"),
    path('empleados_s/', empleados_s , name = "empleados_s"),
    path('empleados_e/', EmpleadoList1.as_view() , name = "empleados_e"),
    path('empleados_u/<int:pk>/', EmpleadoUpdate.as_view(), name = "empleados_u"),
    path('empleados_d/<int:pk>/', EmpleadoDelete.as_view(), name = "empleados_d"),
    #Productos
    path('productos/', ProductoList.as_view() , name = "productos"),
    path('productos_create/', ProductoCreate.as_view() , name = "productos_create"),
    path('productos_s/', productos_s , name = "productos_s"),
    path('productos_e/', ProductoList1.as_view() , name = "productos_e"),
    path('productos_u/<int:pk>/', ProductoUpdate.as_view(), name = "productos_u"),
    path('productos_d/<int:pk>/', ProductoDelete.as_view(), name = "productos_d"),
    #Transacciones
    path('transacciones/', TransaccionList.as_view() , name = "transacciones"),
    path('transacciones_create/', TransaccionCreate.as_view() , name = "transacciones_create"),
    path('transacciones_s/', transacciones_s , name = "transacciones_s"),
    path('transacciones_e/', TransaccionList1.as_view() , name = "transacciones_e"),
    path('transacciones_u/<int:pk>/', TransaccionUpdate.as_view(), name = "transacciones_u"),
    path('transacciones_d/<int:pk>/', TransaccionDelete.as_view(), name = "transacciones_d"),
    #Usuarios
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('signin/', signin, name="signin"),
    path('profile/', editProfile, name="profile"),
    path('<int:pk>/password/', CambiarContraseña.as_view(), name="cambiar_contraseña"),
    path('avatar/', addAvatar, name="avatar"),
    #Otro
    path('aboutme/', aboutme, name= "aboutme"),

]