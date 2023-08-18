from django.db import models
from garagem.models import Cor, Acessorio, Modelo
from uploader.models import Image

class Veiculo(models.Model):
    descricao = models.CharField(max_length=50)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
    )

    def __str__(self):
        return f"{self.descricao} {self.modelo} {self.ano} {self.cor}"

    class Meta:
        verbose_name_plural = "veículos"
        verbose_name = "veículo"