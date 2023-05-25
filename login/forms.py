from django.forms import ModelForm
from .models import Tarea

class Tareas_formulario(ModelForm):
    class Meta:
        models = Tarea
        fields = ["nombre","descripcion","puntos","proyecto","usuario_asignado"]
