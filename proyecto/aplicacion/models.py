from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}"
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre},{self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"

class Transaccion(models.Model):
    numeroDeCliente = models.IntegerField()
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    fecha = models.DateField(max_length=50)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
