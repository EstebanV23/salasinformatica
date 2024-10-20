from django.db import models

# Create your models here.

class Sala(models.Model):
  numero_sala = models.CharField(max_length=10)
  capacidad = models.IntegerField()
  disponibilidad = models.BooleanField()
  descripcion = models.TextField()
  
  def __str__(self):
    return self.numero_sala
