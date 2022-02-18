from django.test import TestCase

# Create your tests here.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='/usr/bin/firefox')

driver.get("https://portal.ufrj.br/Inscricao/extensao/acaoExtensao/filtro")
print(driver.title)   
botao_consulta = driver.find_element_by_id("btnConsultar")
print(dir(botao_consulta))

driver.close()