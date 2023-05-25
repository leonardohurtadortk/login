from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import Tareas_formulario

# Create your views here.

def entrar (request):
    if request.method == 'GET':
        print("enviando datos")
        return render (request,"login.html",{
            "form": UserCreationForm
            })

    else:
        if request.POST["password1"] == request.POST["password2"] :
            try:
                user =User.objects.create_user(username=request.POST["username"],password=request.POST["password1"]) 
                user.save()
                login(request,user)
                return redirect("/tareas/")
            
            except:
                return render(request,"login.html",{
                    "form": UserCreationForm,
                    "error": "El usuario ya existe" 
                    
                    })
        return render(request,"login.html",{
            "form": UserCreationForm,
            "error": "Las contraseñas no coinciden"
            })
    
def tareas (request):
    return render(request,"tareas/tareas.html",{
        "form":Tareas_formulario
        
        })


            
