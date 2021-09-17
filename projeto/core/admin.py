from django.contrib import admin

from .models import Produto, Cliente
# Register your models here.


class ProdutoAdminShow(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco')


admin.site.register(Produto, ProdutoAdminShow)
admin.site.register(Cliente)
