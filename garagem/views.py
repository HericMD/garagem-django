from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Veiculo
from garagem.serializers import AcessorioSerializer, CategoriaSerializer, CorSerializer, VeiculoSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
