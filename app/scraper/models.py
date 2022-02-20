from django.db import models

class InstituicoesParceiras:
    def __init__(self):
        nome = None
        tipo_de_parceiro = None
        forma_de_institucionalizacao = None
        email = None
        endereco = None
        tipo_de_instituicao = None

class EscolasParticipantes():
    def __init__(self):
        nome = None
        tipo_de_escola = None
        email = None
        endereco = None

class CoordenadoresAdjuntos():
    def __init__(self):
        nome = None
        unidade = None
        centro = None

class CaracterizacaoDeProjetos:
    def __init__(self):
        metodologia = None
        duracao_pretendida_do_projeto = None

class CaracterizacaoDeProgramas:
    def __init__(self):
        coordenadores_adjuntos = None
        acoes_de_extensao_vinculadas = None
        linhas_de_extensao = None

class CaracterizacaoDeCursos:
    def __init__(self):
        carga_horaria = None
        modalidade_do_curso = None
        classificacao_do_curso = None
        programa_de_formacao = None
        conteudo_programatico_do_curso = None
        periodos_de_oferta_do_curso_nos_proximos_5_anos = None

class CaracterizacaoDeEventos:
    def __init__(self):
        duracao_do_evento_em_numero_de_dias = None
        quantitativo_de_publico = None
        numero_da_edicao_do_evento = None
        tema_geral_do_evento = None

class EquipeDeRealizacao:
    def __init__(self):
        nome = None
        periodo_de_participacao = Periodo()
        tipo = None

class Periodo:
    def __init__(self):
        inicio = None
        fim = None

class InformacoesDaAcaoDeExtensao:
    def __init__(self):
        centro = None
        unidade = None
        titulo = None
        modalidade = None
        area_tematica_principal = None
        area_tematica_secundaria = None
        objetivos_de_desenvolvimento_sustentavel = None
        coordenador_da_acao_de_extensao = None
        Resumo = None
        Contato = None
        data_de_inicio = None
        data_de_termino = None
        objetivos = None
        links_para_redes_sociaus_e_sites = None
        endereco = None
        publico_da_acao = None
        carga_horaria = None
        instituicoes_parceiras = None
        equipe_de_realizacao = None

class Projeto:
    def __init__():
        informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensao()
        instituicoes_parceiras = InstituicoesParceiras()
        escolas_participantes = EscolasParticipantes()
        caracterizacao_de_projetos = CaracterizacaoDeProjetos()
        equipe_de_realizacao = EquipeDeRealizacao()

class Programa:
    def __init__():
        informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensao()
        instituicoes_parceiras = InstituicoesParceiras()
        escolas_participantes = EscolasParticipantes()
        caracterizacao_de_programas = CaracterizacaoDeProgramas()
        equipe_de_realizacao = EquipeDeRealizacao()

class Curso:
    def __init__():
        informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensao()
        instituicoes_parceiras = InstituicoesParceiras()
        escolas_participantes = EscolasParticipantes()
        caracterizacao_de_cursos = CaracterizacaoDeCursos()
        equipe_de_realizacao = EquipeDeRealizacao()

class Evento:
    def __init__():
        informacoes_da_acao_de_extensao = InformacoesDaAcaoDeExtensao()
        instituicoes_parceiras = InstituicoesParceiras()
        escolas_participantes = EscolasParticipantes()
        caracterizacao_de_eventos = CaracterizacaoDeEventos()
        equipe_de_realizacao = EquipeDeRealizacao()
