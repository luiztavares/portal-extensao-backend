from ast import Eq
from django.test import TestCase
import time
from scraper.models import *

# Create your tests here.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def init_driver():

    chrome_options = Options()  
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver', chrome_options=chrome_options)

    driver.get("https://portal.ufrj.br/Inscricao/extensao/acaoExtensao/filtro")
    return driver

driver = init_driver()

botao_consulta = driver.find_element_by_id("btnConsultar")
botao_consulta.click()

driver.find_element_by_css_selector('.rich-table-cell.lupa a').click()


centro = driver.find_element_by_css_selector('#centroNomeDecorate span').text
print(centro)

driver.close()