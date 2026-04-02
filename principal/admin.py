from django.contrib import admin
from .models import Curso


#Esto dice como mostraremos los datos
class CursoAdmin(admin.ModelAdmin):
    #titulos de las columnas    
    list_display = ("nombre","profesor", "n_alumnos")
    #buscador por nombre
    search_fields = ("nombre",)
    
admin.site.register(Curso, CursoAdmin)
