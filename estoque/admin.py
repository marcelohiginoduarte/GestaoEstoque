from django.contrib import admin
from .models import Produto, Movimentacao

class Produtoadimin(admin.ModelAdmin):
    list_display = ('nome',('preco'), 'quantidade',)
    list_display_links = ('nome', ('preco'),'quantidade',)
    search_fields =('nome',)


admin.site.register(Produto, Produtoadimin)


class Movimentacaoadmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    list_display_links = ('produto', 'data')

admin.site.register(Movimentacao, Movimentacaoadmin)