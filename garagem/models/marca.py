from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"