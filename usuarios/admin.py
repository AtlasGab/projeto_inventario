
from django.contrib import admin
from .models import Material, Movimentacao, Emprestimo


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade', 'estoque_minimo', 'localizacao', 'ativo')
    search_fields = ('nome', 'categoria', 'localizacao')
    list_filter = ('categoria', 'ativo', 'permanente')


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('material', 'tipo', 'quantidade', 'requisitante', 'data_hora')
    search_fields = ('material__nome', 'requisitante', 'matricula')
    list_filter = ('tipo', 'data_hora')


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'material', 'quantidade', 'requisitante', 'status', 'data_emprestimo')
    search_fields = ('codigo', 'material__nome', 'requisitante', 'matricula')
    list_filter = ('status', 'data_emprestimo')
