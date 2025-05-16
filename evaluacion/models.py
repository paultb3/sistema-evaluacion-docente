from django.db import models

from django.db import models
from academico.models import Estudiante, Docente, Curso
from django.utils import timezone

class PeriodoEvaluacion(models.Model):
    idPeriodo = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)

class CriterioEvaluacion(models.Model):
    idCriterio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

class Evaluacion(models.Model):
    idEvaluacion = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    comentarios = models.TextField()
    estado_final = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class EvaluacionPendiente(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class HistorialEvaluacion(models.Model):
    idHistorial = models.AutoField(primary_key=True)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    fecha_cambio = models.DateField()
    descripcion_cambio = models.TextField()

class DetalleEvaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    criterio = models.ForeignKey(CriterioEvaluacion, on_delete=models.CASCADE)
    valoracion = models.IntegerField()
