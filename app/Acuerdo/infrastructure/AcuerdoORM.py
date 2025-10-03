# app/acuerdo/infrastructure/orm.py
from django.db import models
from app.Acuerdo.infrastructure.TipoAcuerdoORM import TipoAcuerdoORM

class AcuerdoORM(models.Model):
    idAcuerdo = models.IntegerField(primary_key=True, db_column="idAcuerdo")
    NumeroAcuerdo = models.CharField(max_length=255, db_column="NumeroAcuerdo")
    FechaActa = models.DateField(db_column="FechaActa")
    NumeroAcuerdoAnterior = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_column="NumeroAcuerdoAnterior"
    )

    tipoAcuerdo = models.ForeignKey(
        TipoAcuerdoORM,
        on_delete=models.PROTECT,
        db_column="TipoAcuerdo_idTipoAcuerdo",
        related_name="acuerdos"
    )

    class Meta:
        db_table = "Acuerdo" 

    def __str__(self):
        return f"{self.NumeroAcuerdo} ({self.FechaActa})"
