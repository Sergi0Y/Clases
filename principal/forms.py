from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        #Estos son los campos a llenar
        fields = ['nombre', 'profesor', 'n_alumnos', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'profesor': forms.TextInput(attrs={'class': 'form-control'}),
            'n_alumnos': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }   
        