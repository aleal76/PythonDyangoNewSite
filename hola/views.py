from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hola/index.html")

def brian(request):
    return HttpResponse("Hola Brian")

def greet(request, name):
    return render(request, "hola/greet.html", {
        "name": name.capitalize()  #python dictionary
        })


