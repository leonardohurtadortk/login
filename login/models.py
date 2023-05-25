from django.db import models
from django.conf import settings

class Project(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    inicio_tiempo = models.DateField()
    fin_tiempo = models.DateField()
    usuario = models.ManyToManyField(settings.AUTH_USER_MODEL)

class Task(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    due_date = models.DateField()
    completada = models.BooleanField(default=False)
    proyecto = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)