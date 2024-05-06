from selenium import webdriver
from pyautogui import hotkey, press, write
from time import sleep
import re
import PyPDF2
import os
import backup.defs as defs

#palavras_chave = ['Brejinho', 'Calumbi', 'Carnaiba', 'Flores', 'Iguaracy', 'Ingazeira', 'Itapetim', 'Quixaba', 'Santa Cruz da Baixa Verde', 'Santa Terezinha', 'Sao Jose do Egito', 'Serra Talhada', 'Solidao', 'Tabira', 'Triunfo', 'Tuparetama', 'Arcoverde', 'Custodia', 'Sertania', 'Betania', 'Sao Jose do Belmonte']
palavras_chave = ['Tuparetama', 'Arcoverde', 'Custodia', 'Betania','Alda Magalhães','Sertânia','Sertania']
encontradas = []


# Abre o navegador e entra no jornal do dia 
data = input('Digite a data do jornal que você quer... ')
navegador = webdriver.Firefox()
link = 'https://sistemas.tce.pe.gov.br/internet/DiarioOficial!download.action?abrirJanela=true&data=' + data
navegador.get(link)


# Scrapping no pdf
hotkey('ctrl', 'f')
for palavra_chave in palavras_chave:
    write(palavra_chave)
    hotkey('ctrl', 'a')
    press('enter')
    press('backspace')
    sleep(0.5) 
    
matches = re.findall(palavra_chave, navegador.page_source, re.IGNORECASE)
if matches:
    encontradas.append(matches)
    
#if palavra_chave.lower() in navegador.page_source.lower():
    #encontradas.append(palavra_chave)


encontradas = [item for sublist in encontradas for item in sublist]

navegador.quit() 

print(f'Palavras encontradas: {encontradas}')

# Mostra se as palavras selecionadas foram ou não achadas

    
