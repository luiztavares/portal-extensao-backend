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

class CaracterizacaoDeProjetos:
    def __init__(self):
        metodologia = None
        duracao_pretendida_do_projeto = None

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
    pass

class Curso:
    pass

class Evento:
    pass

