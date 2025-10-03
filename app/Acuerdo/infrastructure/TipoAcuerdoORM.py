# app/acuerdo/infrastructure/orm.py
from django.db import models

class TipoAcuerdoORM(models.Model):
    idTipoAcuerdo = models.AutoField(primary_key=True, db_column="idTipoAcuerdo")
    TipoAcuerdo = models.CharField(max_length=45, db_column="TipoAcuerdo")

    class Meta:
        db_table = "TipoAcuerdo"  # nombre de la tabla en la BD

    def __str__(self):
        return self.TipoAcuerdo
