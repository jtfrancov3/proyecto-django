from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsuarioPersonalizado(AbstractUser): 
    correo = models.EmailField(unique=False) 
    def __str__(self): 
        return self.username
    
class Categoria_Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10,decimal_places=2)
    stock_minimo = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    categoria_producto = models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE, related_name='productos') # Relacionando Productos a una categoria del producto (Muchos a 1)
    
    def __str__(self):
        return self.nombre