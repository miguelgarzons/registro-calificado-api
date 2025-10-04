# app/Acta/infrastructure/views.py
from rest_framework.response import Response
from rest_framework.views import APIView

from app.Acta.application.use_cases import CrearActa

from .repositories import DjangoORMActaRepository


class CrearActaView(APIView):
    def post(self, request):
        repo = DjangoORMActaRepository()
        use_case = CrearActa(repo)
        acta = use_case.ejecutar(
            titulo=request.data["titulo"], contenido=request.data["contenido"]
        )
        return Response({"id": acta.id, "titulo": acta.titulo})
