from django.db import models

# Create your models here.
class Documentacion (models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    