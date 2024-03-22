from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
def home(request):
  return render(request, "aplicacion/index.html")

#Clientes
@login_required
def clientes(request):
    return render(request, "aplicacion/clientes.html")
@login_required
def clientes_s(request):
    return render(request, "aplicacion/searchC.html")

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteList1(LoginRequiredMixin, ListView):
    model = Cliente

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nombre","numero"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nombre", "numero"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")  
#Empleados
@login_required
def empleados(request):
    return render(request, "aplicacion/empleados.html")
@login_required
def empleados_s(request):
    return render(request, "aplicacion/searchE.html")

class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoList1(LoginRequiredMixin, ListView):
    model = Empleado

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ["nombre","apellido"]
    success_url = reverse_lazy("empleados")

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("empleados")

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy("empleado")  
#Productos
@login_required
def productos(request):
    return render(request, "aplicacion/productos.html")
@login_required
def productos_s(request):
    return render(request, "aplicacion/searchP.html")

class ProductoList(LoginRequiredMixin, ListView):
    model = Producto

class ProductoList1(LoginRequiredMixin, ListView):
    model = Producto

    def get_queryset(self):
        return super().get_queryset().filter(
            nombre__icontains=self.request.GET.get("buscar")
        )

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ["nombre","clase"]
    success_url = reverse_lazy("productos")

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ["nombre", "clase"]
    success_url = reverse_lazy("productos")

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")  
#Transacciones
@login_required
def transacciones(request):
    return render(request, "aplicacion/transacciones.html")
@login_required
def transacciones_s(request):
    return render(request, "aplicacion/searchT.html")

class TransaccionList(LoginRequiredMixin, ListView):
    model = Transaccion

class TransaccionList1(LoginRequiredMixin, ListView):
    model = Transaccion

    def get_queryset(self):
        return super().get_queryset().filter(
            producto__icontains=self.request.GET.get("buscar")
        )

class TransaccionCreate(LoginRequiredMixin, CreateView):
    model = Transaccion
    fields = ["numeroDeCliente","producto","precio","fecha"]
    success_url = reverse_lazy("transacciones")

class TransaccionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaccion
    fields = ["numeroDeCliente", "producto","precio","fecha"]
    success_url = reverse_lazy("transacciones")

class TransaccionDelete(LoginRequiredMixin, DeleteView):
    model = Transaccion
    success_url = reverse_lazy("transacciones")

#Usuarios

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else: 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def signin(request):
    if request.method == "POST":
        miForm = SigninForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = SigninForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )  
