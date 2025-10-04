# app/Acta/domain/repositories.py
from abc import ABC, abstractmethod

from .entities import Acta


class ActaRepository(ABC):
    @abstractmethod
    def save(self, acta: Acta) -> Acta:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Acta:
        pass
