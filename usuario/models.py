from django.db import models
from status.models import Equipo
# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cargo = models.ManyToManyField('Tipo', blank=True)
    area = models.ManyToManyField('Area', blank=True)
    usoequipo = models.OneToOneField(Equipo , null=True,blank=True, on_delete=models.CASCADE)

class Area(models.Model):
    nombre= models.CharField(max_length=50)
    cantidad_usuarios = models.IntegerField()

class Tipo(models.Model):
    tipo_usua = models.CharField(max_length=50)