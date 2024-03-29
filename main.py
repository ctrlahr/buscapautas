from selenium import webdriver
from pyautogui import hotkey, press, write
from time import sleep
import PyPDF2
import os
import defs

palavras_chave = ['Brejinho', 'Calumbi', 'Carnaiba', 'Flores', 'Iguaracy', 'Ingazeira', 'Itapetim', 'Quixaba', 'Santa Cruz da Baixa Verde', 'Santa Terezinha', 'Sao Jose do Egito', 'Serra Talhada', 'Solidao', 'Tabira', 'Triunfo', 'Tuparetama', 'Arcoverde', 'Custodia', 'Sertania', 'Betania', 'Sao Jose do Belmonte']

# Abre o navegador e entra no jornal do dia 
data = input('Digite a data do jornal que você quer... ')
navegador = webdriver.Firefox()
link = 'https://sistemas.tce.pe.gov.br/internet/DiarioOficial!download.action?abrirJanela=true&data=' + data
navegador.get(link)


# Scrapping no pdf
hotkey('ctrl', 'f')
for i in range(21):
    count = 0
    count += 1
    write(palavras_chave[i])
    hotkey('ctrl', 'a')
    press('enter')
    press('backspace')


palavras_encontradas = defs.verificar_palavras_encontradas(navegador, palavras_chave)

navegador.quit()  
  
if palavras_encontradas:
    print('Palavras achadas')
    
else:
    print('palavra não foi achada')
    
