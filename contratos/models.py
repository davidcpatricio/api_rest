from django.db import models


class Entidade(models.Model):
    nome = models.CharField(max_length=150)
    nif = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Morada(models.Model):
    entidade = models.ForeignKey(
        Entidade,
        on_delete=models.PROTECT,
        blank=True, null=True
    )
    rua = models.CharField(max_length=100)
    porta = models.CharField(max_length=10, blank=True)
    codigo_postal = models.CharField(max_length=8)
    localidade = models.CharField(max_length=255)
    ativo_inativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.rua} {self.porta} - {self.codigo_postal} {self.localidade}'


class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    preco = models.DecimalField(decimal_places=2, max_digits=20)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'Contrato {self.id}'


class EntidadeDeContrato(models.Model):
    class Meta:
        verbose_name = 'Entidade de Contrato'
        verbose_name_plural = 'Entidades de Contratos'

    entidade = models.ForeignKey(
        Entidade,
        on_delete=models.PROTECT,
        blank=True, null=True
    )
    contrato = models.ForeignKey(
        Contrato,
        on_delete=models.PROTECT,
        blank=True, null=True
    )

    def __str__(self):
        return f'Entidade {self.entidade_id} - Contrato {self.contrato_id}'
