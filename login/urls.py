

from django.urls import path
from .views import entrar,tareas
urlpatterns =[
    path("",entrar,name="login"),
    path("tareas/",tareas ,name="tareas")
    
    ]