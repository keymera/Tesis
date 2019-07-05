from django.db import models
#from django.utils import timezone

# Create your models here.

#class Post(models.Model):
#    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
#
#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()
#
#    def __str__(self):
#        return self.title


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    disco = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    bios = models.CharField(max_length=50)
    ipaddress = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=50)
    marca_modelo = models.CharField(max_length=50)
    externo = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    usuario_equipos = models.CharField(max_length=50)

