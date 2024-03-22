from django.db import models

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
