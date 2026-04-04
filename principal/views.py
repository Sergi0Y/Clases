from django.shortcuts import render, redirect
from .models import Curso #tabla creada
from .forms import CursoForm # Importamos el formulario que creamos arriba
from django.shortcuts import render, get_object_or_404

def inicio(request):
   #traemos todos los cursos y los guardamos en nuestra variable
   cursos = Curso.objects.all()

    # al apretar guardar o enviar (POST)
   if request.method == 'POST':
      form = CursoForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inicio') #recargamos
   else:
      #si solo entramos a la pag el form va vacío
      form = CursoForm() 
        
   return render(request, 'principal/index.html', {"cursos": cursos, 'form':form})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return render(request, 'principal/detalle.html', {'curso': curso})