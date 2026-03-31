from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    profesor = models.CharField(max_length=200)
    n_alumnos = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
