from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
	return HttpResponse("<h1>¡Hola Clase! Este es el primer backend</h1>")
def main(request):
    return render(request,'principal/index.html')
# Create your views here.
