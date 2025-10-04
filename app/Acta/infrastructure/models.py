# app/Acta/infrastructure/models.py
from django.db import models

class ActaModel(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
