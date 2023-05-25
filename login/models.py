from django.db import models
from django.conf import settings

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    inicio_tiempo = models.DateField()
    fin_tiempo = models.DateField()
    usuario = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.nombre 

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creada = models.DateField(auto_now_add=True)
    importante = models.BooleanField(default= False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario_asignado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    puntos = models.IntegerField()

    def __str__(self):
        return self.nombre + " - By "+ self.usuario_asignado.username