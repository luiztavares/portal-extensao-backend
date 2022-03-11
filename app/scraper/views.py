from scraper.models import *
from scraper.serializers import *
from rest_framework import viewsets
from itertools import chain


# Create your views here.

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class HomeViewSet(viewsets.ModelViewSet):
    projeto = InformacoesDaAcaoDeExtensao.objects.filter(modalidade='Projeto')[0:2]
    evento = InformacoesDaAcaoDeExtensao.objects.filter(modalidade='Evento')[0:2]
    curso = InformacoesDaAcaoDeExtensao.objects.filter(modalidade='Curso')[0:2]

    queryset = projeto | evento | curso
    
    serializer_class = HomeSerializer