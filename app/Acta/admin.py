# app/Acta/infrastructure/admin.py
from django.contrib import admin

from .models import ActaModel


@admin.register(ActaModel)
class ActaAdmin(admin.ModelAdmin):
    # pyrefly: ignore  # bad-override
    list_display = ("id", "titulo", "contenido")  # columnas en el listado
    # pyrefly: ignore  # bad-override
    search_fields = ("titulo",)  # buscador
