from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
	return HttpResponse("<h1>¡Hola Clase! Este es el primer backend</h1>")
""" def main(request):
    return render(request,'principal/index.html') """
def main(request):
    datos ={
        "nombre_curso": "Programación Backend con Django",
        "profesor": "Sergio",
        "n_alumnos": 15,
        "lista_alumnos": ["Juan", "María", "Pedro", "Ana"]
    }
    return render(request, 'principal/index.html',datos)
# Create your views here.
