from django.db import models

class Rol(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    permisos = models.TextField()

class Usuario(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class AccesoSistema(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_acceso = models.DateTimeField()
    direccion_ip = models.CharField(max_length=50)

class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateField()
    leido = models.BooleanField(default=False)

class LogAccion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    detalle = models.TextField()
