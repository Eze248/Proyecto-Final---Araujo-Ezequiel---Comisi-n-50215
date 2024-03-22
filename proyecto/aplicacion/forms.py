from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    numero = forms.IntegerField(required=True)

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    clase = forms.CharField(max_length=50, required=True)

class TransaccionForm(forms.Form):
    numeroDeCliente = forms.IntegerField(required=True)
    producto = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    fecha = forms.DateField(required=True)

class SigninForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]