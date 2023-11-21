import re

from django.db import models
from django.forms import ValidationError

from utils.validate_nif import validate_nif


class Entidade(models.Model):
    nome = models.CharField(max_length=150)
    nif = models.CharField(max_length=9, verbose_name='NIF')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    telefone = models.CharField(max_length=20)

    def clean(self):
        error_messages = {}

        if not validate_nif(self.nif):
            error_messages['nif'] = 'NIF inválido.'

        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return self.nome


class Morada(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    rua = models.CharField(max_length=100)
    porta = models.CharField(max_length=10, blank=True)
    codigo_postal = models.CharField(max_length=8)
    localidade = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def clean(self):
        error_messages = {}

        if not re.search(r'\d{4}-\d{3}', self.codigo_postal) or \
                len(self.codigo_postal) != 8:
            error_messages['codigo_postal'] = 'Código postal inválido.'

        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return f'{self.rua} {self.porta} - {self.codigo_postal} {self.localidade}'


class Contrato(models.Model):
    data_inicio = models.DateField(verbose_name = 'Data de início')
    data_fim = models.DateField(verbose_name='Data de fim')
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

    def get_preco_formatado(self):
        return f'{self.preco:.2f}€'
    get_preco_formatado.short_description = 'Preço'

    def __str__(self):
        return f'Contrato {self.id}'


class EntidadeDeContrato(models.Model):
    class Meta:
        verbose_name = 'Entidade de Contrato'
        verbose_name_plural = 'Entidades de Contratos'

    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT)

    def __str__(self):
        return f'Entidade {self.entidade} - Contrato {self.contrato_id}'
