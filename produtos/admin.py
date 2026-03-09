from django.contrib import admin
from produtos.models import ProdutoImagem, ProdutoInfo


class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 1


@admin.register(ProdutoInfo)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ProdutoImagemInline]
