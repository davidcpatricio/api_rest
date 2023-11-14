from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from contratos.serializers import (EntidadeSerializer, MoradaSerializer,
                                   ContratoSerializer,
                                   EntidadeDeContratoSerializer)
from contratos.models import Entidade, Morada, Contrato, EntidadeDeContrato


class EntidadeViewSet(viewsets.ModelViewSet):
    queryset = Entidade.objects.all().order_by('nome')
    serializer_class = EntidadeSerializer
    permission_classes = [IsAuthenticated]

    def get_paginated_response(self, data):
        return Response(data)


class MoradaViewSet(viewsets.ModelViewSet):
    queryset = Morada.objects.all().order_by('rua')
    serializer_class = MoradaSerializer
    permission_classes = [IsAuthenticated]

    def get_paginated_response(self, data):
        return Response(data)


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all().order_by('data_inicio')
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

    def get_paginated_response(self, data):
        return Response(data)


class EntidadeDeContratoViewSet(viewsets.ModelViewSet):
    # queryset = EntidadeDeContrato.objects.all().order_by('entidade')
    serializer_class = EntidadeDeContratoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        contrato_id = self.kwargs.get('contrato_id', None)
        entidade_id = self.kwargs.get('entidade_id', None)

        if contrato_id is not None:
            return EntidadeDeContrato.objects.filter(contrato=contrato_id)

        if entidade_id is not None:
            return EntidadeDeContrato.objects.filter(entidade=entidade_id)

        return EntidadeDeContrato.objects.all()

    def get_paginated_response(self, data):
        return Response(data)
