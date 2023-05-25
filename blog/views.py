from django.shortcuts import render ,redirect

# Create your views here.

def inicio(request):
    return render (request,"inicio.html")

def documentacion(request):
    return render(request,"documentacion/documentacion.html")

def tareas (request):
    return render(request,"tareas/tareas.html")

def proyectos(request):
    return render(request,"proyectos/proyectos.html")