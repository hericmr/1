#importa bibliotecas
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
#inicializa o webdriver do chrome
navegador = webdriver.Chrome()

#acessa o site
navegador.get("https://povosantista.blogspot.com/")

#encontra o elemento da página com base no nome do elemento
campo_de_busca = navegador.find_element(By.NAME, "q")
#preenche campo de busca e envia
campo_de_busca.send_keys('Héric Moura')
campo_de_busca.submit()
sleep(999)