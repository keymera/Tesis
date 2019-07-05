from django.db import models

class Log(models.Model):
    usuario=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)