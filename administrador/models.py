from django.db import models

# Create your models here.

class DMPPROJECT:
    # Define las propiedades y métodos de tu clase
    pass

class Compra(models.Model):
    nombre  = models.CharField(primary_key=True, max_length=20)
    Detalle = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    
    def _str_(self):
        return str(self.nombre)