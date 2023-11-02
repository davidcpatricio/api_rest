from rest_framework import serializers
from contratos.models import Entidade, Morada, Contrato, EntidadeDeContrato


class EntidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entidade
        fields = 'nome', 'nif', 'email', 'telefone',


class MoradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Morada
        fields = 'entidade', 'rua', 'porta', 'codigo_postal', 'localidade',


class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = 'data_inicio', 'data_fim', 'preco', 'descricao',


class EntidadeDeContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntidadeDeContrato
        fields = 'entidade', 'contrato',
