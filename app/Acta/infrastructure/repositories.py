# app/Acta/infrastructure/repositories.py
from app.Acta.domain.entities import Acta
from app.Acta.domain.repositories import ActaRepository

from .models import ActaModel


class DjangoORMActaRepository(ActaRepository):
    def save(self, acta: Acta) -> Acta:
        # pyrefly: ignore  # missing-attribute
        model = ActaModel.objects.create(titulo=acta.titulo, contenido=acta.contenido)
        return Acta(id=model.id, titulo=model.titulo, contenido=model.contenido)

    def find_by_id(self, id: int) -> Acta:
        # pyrefly: ignore  # missing-attribute
        model = ActaModel.objects.get(pk=id)
        return Acta(id=model.id, titulo=model.titulo, contenido=model.contenido)
