from rest_framework import serializers
from contratos.models import Entidade, Morada, Contrato, EntidadeDeContrato


class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = ('id', 'nome', 'nif', 'email', 'telefone')


class MoradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morada
        fields = ('entidade', 'rua', 'porta', 'codigo_postal', 'localidade')


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('id', 'data_inicio', 'data_fim', 'preco', 'descricao')


class EntidadeDeContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeDeContrato
        fields = ('entidade', 'contrato')
