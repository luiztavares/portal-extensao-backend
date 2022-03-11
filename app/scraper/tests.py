from ast import Eq
from tkinter import N
from django.test import TestCase
import time
from scraper.models import *

# Create your tests here.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

modalidades = {
    0: 'Curso',
    #1: 'Evento',
    #2: 'Programa',
    #3: 'Projeto',
}

def toDate(s):
    s = s.replace(' ','')
    
    if (len(s) >= 10):
        return f'{s[6:10]}-{s[3:5]}-{s[:2]}'
    else:
        return None

def num(n):
    return None if n == '-' else n

def init_driver(modalidade):

    chrome_options = Options()  
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver', chrome_options=chrome_options)

    driver.get("https://portal.ufrj.br/Inscricao/extensao/acaoExtensao/filtro")
    driver.find_element_by_xpath(f"//select[@id='modalidade']//option[text()='{modalidade}']").click()
    botao_consulta = driver.find_element_by_id("btnConsultar")
    botao_consulta.click()

    return driver

for key in modalidades:

    driver = init_driver(modalidades[key])

    num_paginas = int(driver.find_element_by_css_selector('#gnosys-filtro-paginacao-campos span').text)
    for pag_atual in range(3,num_paginas+1) :
        atual = driver.find_element_by_css_selector('#gnosys-filtro-paginacao-paginaAtual')
        atual.clear()
        atual.send_keys(pag_atual)
        atual.send_keys(Keys.ENTER)
        time.sleep(2)
        page_links = driver.find_elements_by_css_selector('.rich-table-cell.lupa a')

        for i in range(len(page_links)):
            atual = driver.find_element_by_css_selector('#gnosys-filtro-paginacao-paginaAtual')
            atual.clear()
            atual.send_keys(pag_atual)
            atual.send_keys(Keys.ENTER)
            time.sleep(2)
            print(pag_atual,i)
            driver.find_elements_by_css_selector('.rich-table-cell.lupa a')[i].click()

            acao = None
            id = driver.current_url.split('?id=')[1].split('&')[0]
            carga_horaria = driver.find_element_by_css_selector('#cargaHorariaDecorate span').text
            informacoesDaAcaoDeExtensao = InformacoesDaAcaoDeExtensao(
                id = id,
                centro = driver.find_element_by_css_selector('#centroNomeDecorate span').text,
                unidade = driver.find_element_by_css_selector('#unidadeNomeDecorate span').text,
                titulo = driver.find_element_by_css_selector('#acaoExtensaoNomeDecorate span').text,
                modalidade = driver.find_element_by_css_selector('#acaoExtensaoModalidadeDecorate span').text,
                area_tematica_principal = driver.find_element_by_css_selector('#areaTematicaPrimariaExtensaoNomeDecorate span').text,
                area_tematica_secundaria = driver.find_element_by_css_selector('#areaTematicaSecundariaExtensaoNomeDecorate span').text,
                objetivos_de_desenvolvimento_sustentavel = 'todo',
                coordenador_da_acao_de_extensao = driver.find_element_by_css_selector('#coordenadorNomeDecorate span').text,
                Resumo = driver.find_element_by_css_selector('#descricaoAcaoExtensaoDecorate span').text,
                Contato = driver.find_element_by_css_selector('#contatoDecorate span').text,
                data_de_inicio = toDate(driver.find_element_by_css_selector('#dataInicioDecorate span').text),
                data_de_termino = toDate(driver.find_element_by_css_selector('#dataFimDecorate span').text),
                objetivos = driver.find_element_by_css_selector('#objetivosDecorate span').text,
                links_para_redes_sociaus_e_sites = driver.find_element_by_css_selector('#linksAcaoExtensaoDecorate span').text,
                endereco = driver.find_element_by_css_selector('#enderecosDecorate span').text,
                publico_da_acao = driver.find_element_by_css_selector('#publicoAcaoDecorate span').text,
                carga_horaria = num(driver.find_element_by_css_selector('#cargaHorariaDecorate span').text),
            )
            informacoesDaAcaoDeExtensao.save()

            if (informacoesDaAcaoDeExtensao.modalidade == 'Curso'):
                caracterizacaoDeCurso = CaracterizacaoDeCurso(
                    carga_horaria = num(driver.find_element_by_css_selector('#cargaHorariaTotalDecorate span').text),
                    modalidade_do_curso = driver.find_element_by_css_selector('#modalidadeCursoDecorate span').text,
                    classificacao_do_curso = driver.find_element_by_css_selector('#classificacaoCursoDecorate span').text,
                    programa_de_formacao = driver.find_element_by_css_selector('#programaFormacaoDecorate span').text,
                    conteudo_programatico_do_curso = driver.find_element_by_css_selector('#conteudoProgramaticoDecorate span').text,
                    periodos_de_oferta_do_curso_nos_proximos_5_anos = '0'
                )
                caracterizacaoDeCurso.save()
                acao = Curso(id=id,informacoes_da_acao_de_extensao=informacoesDaAcaoDeExtensao,caracterizacao_de_cursos=caracterizacaoDeCurso)

            elif(informacoesDaAcaoDeExtensao.modalidade == 'Projeto'):
                caracterizacaoDeProjeto = CaracterizacaoDeProjeto(
                    metodologia = driver.find_element_by_css_selector('#metodologiaDecorate span').text,
                    duracao_pretendida_do_projeto = num(driver.find_element_by_css_selector('#duracaoPretendidaDecorate span').text),
                )
                caracterizacaoDeProjeto.save()
                acao = Projeto(id=id,informacoes_da_acao_de_extensao=informacoesDaAcaoDeExtensao,caracterizacao_de_projetos=caracterizacaoDeProjeto)

            elif(informacoesDaAcaoDeExtensao.modalidade == 'Evento'):
                caracterizacaoDeEvento = CaracterizacaoDeEvento(
                    duracao_do_evento_em_numero_de_dias = num(driver.find_element_by_css_selector('#duracaoDiasDecorate span').text),
                    quantitativo_de_publico = num(driver.find_element_by_css_selector('#publicoEsperadoDecorate span').text),
                    numero_da_edicao_do_evento = num(driver.find_element_by_css_selector('#numeroEdicaoDecorate span').text),
                    tema_geral_do_evento = driver.find_element_by_css_selector('#temaGeralEventoDecorate span').text,
                )
                caracterizacaoDeEvento.save()
                acao = Evento(id=id,informacoes_da_acao_de_extensao=informacoesDaAcaoDeExtensao,caracterizacao_de_eventos=caracterizacaoDeEvento)

            acao.save()
            tipos_de_instituicao = ['Nacionais','Internacionais']
            for tipo_de_instituicao in tipos_de_instituicao:
                parceiros_nacionais_element = driver.find_elements_by_css_selector(f'#tabelaInstituicoesParceiras{tipo_de_instituicao} tbody tr')
                for parceiro_nacional_element in parceiros_nacionais_element:
                    colunas = parceiro_nacional_element.find_elements_by_css_selector('td')
                    instituicaosParceira = InstituicaosParceira(
                        nome = colunas[0].text,
                        tipo_de_parceiro = colunas[1].find_element_by_css_selector('span').text,
                        forma_de_institucionalizacao = colunas[2].find_element_by_css_selector('span').text,
                        email = colunas[3].text,
                        endereco = colunas[4].text,
                        tipo_de_instituicao = tipo_de_instituicao.lower(),
                    )
                    instituicaosParceira.save()
                    acao.instituicoes_parceiras.add(instituicaosParceira)

            escolas_element = driver.find_elements_by_css_selector(f'#tabelaEscolasParticipantes tbody tr')
            for escola_element in escolas_element:
                colunas = escola_element.find_elements_by_css_selector('td')
                escolaParticipante = EscolaParticipante(
                    nome = colunas[0].text,
                    tipo_de_escola = colunas[1].text,
                    email = colunas[2].text,
                    endereco = colunas[3].text,
                )
                escolaParticipante.save()
                acao.escolas_participantes.add(escolaParticipante)

            tipos_de_membro = {
                'interno': 'tabelaEquipeDeRealizacaoUFRJ',
                'externo' : 'tabelaEquipeDeRealizacaoExterno',
                'extensionista': 'tabelaAlunosExtensao',
            }
            for tipo_de_membro in tipos_de_membro:
                membros_element = driver.find_elements_by_css_selector(f'#{tipos_de_membro[tipo_de_membro]} tbody tr')
                for membro_element in membros_element:
                    colunas = membro_element.find_elements_by_css_selector('td')
                    inicio,fim = colunas[1].find_element_by_css_selector('span').text.split('-')
                    periodo = Periodo(inicio = toDate(inicio), fim=toDate(fim))
                    periodo.save()
                    membro = Membro(
                        nome = colunas[0].text,
                        periodo_de_participacao = periodo,
                        tipo = tipo_de_membro,
                    )
                    membro.save()
                    acao.equipe_de_realizacao.add(membro)

            driver.execute_script("window.history.go(-1)")
    driver.close()