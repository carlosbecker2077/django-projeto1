from django.db import models
from django.db.models.base import Model

# Create your models here.


class Produto(models.Model):
    # lição aprendida: a propriedade name= muda o nome do campo no banco
    codigo = models.CharField('Código', max_length=30, default='')
    nome = models.CharField('Nome', max_length=100, default='')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.codigo} | {self.nome}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=30)
    email = models.CharField('E-Mail', max_length=100)

    def __str__(self):
        return self.nome
