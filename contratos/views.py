from rest_framework import viewsets, permissions

from contratos.serializers import (EntidadeSerializer, MoradaSerializer,
                                   ContratoSerializer,
                                   EntidadeDeContratoSerializer)
from contratos.models import Entidade, Morada, Contrato, EntidadeDeContrato


class EntidadeViewSet(viewsets.ModelViewSet):
    queryset = Entidade.objects.all().order_by('nome')
    serializer_class = EntidadeSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoradaViewSet(viewsets.ModelViewSet):
    queryset = Morada.objects.all().order_by('rua')
    serializer_class = MoradaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all().order_by('data_inicio')
    serializer_class = ContratoSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntidadeDeContratoViewSet(viewsets.ModelViewSet):
    queryset = EntidadeDeContrato.objects.all().order_by('entidade')
    serializer_class = EntidadeDeContratoSerializer
    permission_classes = [permissions.IsAuthenticated]
