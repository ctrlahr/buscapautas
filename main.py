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

# Chama a função e armazena se as palavras foram ou não achadas em uma variavel
palavras_encontradas = defs.verificar_palavras_encontradas(navegador, palavras_chave) # Dá certo, mas só se só uma palavra for colocada na função
print(palavras_encontradas)

navegador.quit()  

# Mostra se as palavras selecionadas foram ou não achadas

    
