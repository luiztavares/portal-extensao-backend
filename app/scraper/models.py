from django.db import models

class InstituicaosParceira(models.Model):
    nome = models.CharField(max_length=100)
    tipo_de_parceiro = models.CharField(max_length=100)
    forma_de_institucionalizacao =  models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    endereco =  models.CharField(max_length=1000)
    tipo_de_instituicao =  models.CharField(max_length=100)

class EscolaParticipante(models.Model):
    nome = models.CharField(max_length=100)
    tipo_de_escola = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=1000)

class CoordenadoresAdjuntos(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    centro = models.CharField(max_length=100)

class CaracterizacaoDeProjeto(models.Model):
    metodologia = models.CharField(max_length=10000)
    duracao_pretendida_do_projeto = models.IntegerField(null=True)

class CaracterizacaoDePrograma(models.Model):
    coordenadores_adjuntos = models.ManyToManyField(CoordenadoresAdjuntos)
    acoes_de_extensao_vinculadas = models.ManyToManyField('Acao')
    linhas_de_extensao = 'todo'

class CaracterizacaoDeCurso(models.Model):
    carga_horaria = models.IntegerField(null=True)
    modalidade_do_curso = models.CharField(max_length=100)
    classificacao_do_curso = models.CharField(max_length=100)
    programa_de_formacao = models.CharField(max_length=1000)
    conteudo_programatico_do_curso = models.CharField(max_length=1000)
    periodos_de_oferta_do_curso_nos_proximos_5_anos = models.IntegerField(null=True)

class CaracterizacaoDeEvento(models.Model):
    duracao_do_evento_em_numero_de_dias = models.IntegerField(null=True)
    quantitativo_de_publico = models.IntegerField(null=True)
    numero_da_edicao_do_evento = models.IntegerField(null=True)
    tema_geral_do_evento = models.CharField(max_length=100)

class Periodo(models.Model):
    inicio = models.DateField()
    fim = models.DateField(null=True)

    def __str__(self):
        return f'inicio: {self.inicio}, fim:{self.fim}'

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    periodo_de_participacao = models.ForeignKey(Periodo,on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)

class InformacoesDaAcaoDeExtensao(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    centro = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    titulo = models.CharField(max_length=1000)
    modalidade = models.CharField(max_length=100)
    area_tematica_principal = models.CharField(max_length=100)
    area_tematica_secundaria = models.CharField(max_length=100)
    objetivos_de_desenvolvimento_sustentavel = models.CharField(max_length=100)
    coordenador_da_acao_de_extensao = models.CharField(max_length=100)
    Resumo = models.CharField(max_length=1000)
    Contato = models.CharField(max_length=100)
    data_de_inicio = models.DateField(null=True)
    data_de_termino = models.DateField(null=True)
    objetivos = models.CharField(max_length=1000)
    links_para_redes_sociaus_e_sites = models.CharField(max_length=1000)
    endereco = models.CharField(max_length=1000)
    publico_da_acao = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(null=True)

class Acao(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    informacoes_da_acao_de_extensao = models.ForeignKey(InformacoesDaAcaoDeExtensao,on_delete=models.PROTECT)
    instituicoes_parceiras = models.ManyToManyField(InstituicaosParceira)
    escolas_participantes = models.ManyToManyField(EscolaParticipante)
    equipe_de_realizacao = models.ManyToManyField(Membro)

class Projeto(Acao):
    caracterizacao_de_projetos = models.ForeignKey(CaracterizacaoDeProjeto,on_delete=models.PROTECT)

class Programa(Acao):
    caracterizacao_de_programas = models.ForeignKey(CaracterizacaoDePrograma,on_delete=models.PROTECT)

class Curso(Acao):
    caracterizacao_de_cursos = models.ForeignKey(CaracterizacaoDeCurso,on_delete=models.PROTECT)

class Evento(Acao):
    caracterizacao_de_eventos = models.ForeignKey(CaracterizacaoDeEvento,on_delete=models.PROTECT)
