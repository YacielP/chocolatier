from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    CATEGORIAS = [
        ('Combos', 'combos'),
        ('Individuales', 'individuales'),
        ('Otros', 'otros')
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/',blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")