from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# Funções

def verificar_palavras_encontradas(driver, texto):
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), texto)
    )
        return True
    except:
        return False    

