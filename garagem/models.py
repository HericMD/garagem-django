from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Acessórios"


class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Cores"


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome.upper()


class Veiculo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="marca")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="categoria"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="cor")
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, default=0
    )

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} {self.cor}"

    class Meta:
        verbose_name_plural = "veículos"
        verbose_name = "veículo"
