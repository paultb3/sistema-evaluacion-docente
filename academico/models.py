from django.db import models

from django.db import models
from usuarios.models import Usuario

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=200)
    semestre = models.IntegerField()

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=200)
    antiguedad = models.IntegerField()

class Comision(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)

class MiembroComision(models.Model):
    id = models.AutoField(primary_key=True)
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=100)

class Curso(models.Model):
    codigoCurso = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=200)
    semestre = models.IntegerField()
    facultad = models.CharField(max_length=200)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
