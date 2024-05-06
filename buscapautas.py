from selenium import webdriver
from pyautogui import hotkey, press, write
from time import sleep
import re

palavras_chave = ['Brejinho', 'Calumbi', 'Carnaiba', 'Flores', 'Iguaracy', 'Ingazeira', 'Itapetim', 'Quixaba', 'Santa Cruz da Baixa Verde', 'Santa Terezinha', 'Sao Jose do Egito', 'Serra Talhada', 'Solidao', 'Tabira', 'Triunfo', 'Tuparetama', 'Arcoverde', 'Custodia', 'Sertania', 'Betania', 'Sao Jose do Belmonte']
#palavras_chave = ['Sertânia', 'Tuparetama', 'Arcoverde', 'Custodia', 'Betania']
encontradas = []


# Abre o navegador e entra no jornal do dia 
data = input('Por favor, digite a data do jornal que você quer... ')
navegador = webdriver.Firefox()
link = 'https://sistemas.tce.pe.gov.br/internet/DiarioOficial!download.action?abrirJanela=true&data=' + data # Ainda vou botar a opção de escolha dos jornais.
navegador.get(link)


# Scrapping no pdf
hotkey('ctrl', 'f')
for palavra_chave in palavras_chave:
    write(palavra_chave)
    hotkey('ctrl', 'a')
    press('enter')
    press('backspace')
    sleep(0.5)
    
# Verifica se a palavra-chave foi encontrada na página
    matches = re.findall(palavra_chave, navegador.page_source, re.IGNORECASE)
    if matches:
        encontradas.append(matches)
    
# Transforma a lista de listas em uma lista plana
navegador.quit() 
print(f'As palavras encontradas foram {encontradas}')
sleep(50000)