from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *
def home(request):
  return render(request, "aplicacion/index.html")

def clientes(request):
    return render(request, "aplicacion/clientes.html")

def empleados(request):
    return render(request, "aplicacion/empleados.html")

def productos(request):
    return render(request, "aplicacion/productos.html")

def transacciones(request):
    return render(request, "aplicacion/transacciones.html")

def clientes_s(request):
    return render(request, "aplicacion/searchC.html")

def empleados_s(request):
    return render(request, "aplicacion/searchE.html")

def productos_s(request):
    return render(request, "aplicacion/searchP.html")

def transacciones_s(request):
    return render(request, "aplicacion/searchT.html")

class ClienteList(ListView):
    model = Cliente

class ClienteList1(ListView):
    model = Cliente

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )

class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nombre","numero"]
    success_url = reverse_lazy("clientes")

class EmpleadoList(ListView):
    model = Empleado

class EmpleadoList1(ListView):
    model = Empleado

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )

class EmpleadoCreate(CreateView):
    model = Empleado
    fields = ["nombre","apellido"]
    success_url = reverse_lazy("empleados")

class ProductoList(ListView):
    model = Producto

class ProductoList1(ListView):
    model = Producto

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )


class ProductoCreate(CreateView):
    model = Producto
    fields = ["nombre","clase"]
    success_url = reverse_lazy("productos")

class TransaccionList(ListView):
    model = Transaccion

class TransaccionList1(ListView):
    model = Transaccion

    def get_queryset(self):
        return super().get_queryset().filter(
            producto__icontains=self.request.GET.get("buscar")
        )

class TransaccionCreate(CreateView):
    model = Transaccion
    fields = ["producto","precio","fecha"]
    success_url = reverse_lazy("transacciones")