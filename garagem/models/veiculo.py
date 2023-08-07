from django.db import models
from garagem.models import Cor, Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(max_length=5)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(10, 2)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="modelos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="modelos")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"
