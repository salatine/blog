from django.db import models


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=64, verbose_name='Nome')
    context_object_name = 'categorias'

    def __str__(self):
        return self.nome_cat
