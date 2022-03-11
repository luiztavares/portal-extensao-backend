from rest_framework import serializers
from scraper.models import *

class InformacoesDaAcaoDeExtensaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesDaAcaoDeExtensao
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesDaAcaoDeExtensao
        fields = ('titulo','modalidade','endereco','coordenador_da_acao_de_extensao')

class CaracterizacaoDeProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracterizacaoDeProjeto
        fields = '__all__'

class CaracterizacaoDeCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracterizacaoDeCurso
        fields = '__all__'

class CaracterizacaoDeEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracterizacaoDeEvento
        fields = '__all__'

class InstituicaosParceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaosParceira
        fields = '__all__'

class EscolaParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscolaParticipante
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class MembroSerializer(serializers.ModelSerializer):
    periodo_de_participacao = PeriodoSerializer()
    class Meta:
        model = Membro
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensaoSerializer(many=False, read_only=True)
    caracterizacao_de_projetos = CaracterizacaoDeProjetoSerializer(many=False, read_only=True)
    instituicoes_parceiras = InstituicaosParceiraSerializer(many=True, read_only=True)
    escolas_participantes = EscolaParticipanteSerializer(many=True, read_only=True)
    equipe_de_realizacao = MembroSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensaoSerializer(many=False, read_only=True)
    caracterizacao_de_eventos = CaracterizacaoDeEventoSerializer(many=False, read_only=True)
    instituicoes_parceiras = InstituicaosParceiraSerializer(many=True, read_only=True)
    escolas_participantes = EscolaParticipanteSerializer(many=True, read_only=True)
    equipe_de_realizacao = MembroSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensaoSerializer(many=False, read_only=True)
    caracterizacao_de_cursos = CaracterizacaoDeCursoSerializer(many=False, read_only=True)
    instituicoes_parceiras = InstituicaosParceiraSerializer(many=True, read_only=True)
    escolas_participantes = EscolaParticipanteSerializer(many=True, read_only=True)
    equipe_de_realizacao = MembroSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'
