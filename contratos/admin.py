from django.contrib import admin
from contratos import models


@admin.register(models.Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'nif', 'email', 'telefone',
    ordering = '-id',
    search_fields = 'id', 'nome', 'nif', 'email', 'telefone',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'nome', 'nif', 'email', 'telefone',
    list_display_links = 'id',


@admin.register(models.Morada)
class MoradaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'entidade', 'rua', 'porta', 'codigo_postal',
        'localidade', 'ativo_inativo'
    )
    ordering = '-id',
    search_fields = (
        'id', 'entidade', 'rua', 'porta', 'codigo_postal', 'localidade'
    )
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'rua', 'porta', 'codigo_postal', 'localidade',
    list_display_links = 'id',


@admin.register(models.Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'data_inicio', 'data_fim', 'preco', 'descricao',
    )
    ordering = '-id',
    search_fields = 'id', 'data_inicio', 'data_fim', 'descricao',
    'localidade',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'data_fim', 'descricao',
    list_display_links = 'id',


@admin.register(models.EntidadeDeContrato)
class EntidadeDeContratoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'entidade', 'contrato',
    )
    ordering = '-id',
    search_fields = 'id', 'entidade', 'contrato',
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id',
