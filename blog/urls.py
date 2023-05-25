from django.urls import path
from .views import inicio ,tareas ,proyectos,documentacion

urlpatterns =[
    path("",inicio,name="inicio"),
    path("tareas/",tareas , name= "tareas"),
    path("proyectos/", proyectos , name="proyectos"),
    path ("documentacion/",documentacion, name = "documentacion")
    
    ]