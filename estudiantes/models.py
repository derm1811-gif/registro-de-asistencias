from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    asistencia = models.BooleanField()


