from django import forms 

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
    producto = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    fecha = forms.DateField(required=True)