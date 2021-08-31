from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
import os
import time
import random
import string
import nomes, sobrenomes

# Gerar nomes aleatórios

nome_index = random.randrange(200)
sobrenome_index = random.randrange(100)

nome = nomes.name_list[nome_index]
sobrenome = sobrenomes.lastname_list[sobrenome_index]

# Gerar senha aleatória

chars = string.ascii_letters + string.digits + '!#$'
password = ''.join(random.choice(chars) for i in range(8))



# Definindo o navegador.

navegador = webdriver.Chrome()

# Abrir a aba

navegador.get('https://github.com/Biduww')
navegador.execute_script("window.open('https://shortlyai.com/signup/', 'secondtab');") # cria a segunda aba
navegador.switch_to_window('secondtab') # transfere pra segunda aba

# Preencher dados padrões

    # Nome

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/input[1]').send_keys(nome)

    # Sobrenome

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/input[2]').send_keys(sobrenome)

    # Password

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/input[4]').send_keys(password)

# Gerar e-mail temporario e usar ele no cadastro

navegador.execute_script(
    "window.open('https://temp-mail.org/pt/', 'thirdtab');") # cria a aba do e-mail

navegador.switch_to_window('thirdtab') # troca pra aba do e-mail

time.sleep(10) # Delay
navegador.find_element_by_xpath(
    '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button').click()
#email = navegador.find_element_by_xpath('//*[@id="mail"]').text

time.sleep(4)

navegador.switch_to_window('secondtab') # volta pra aba de sing-up

act = ActionChains(navegador)

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/input[3]').click()

act.key_down(keys.Keys.CONTROL).send_keys('v').key_up(keys.Keys.CONTROL).perform()

time.sleep(5)
email = navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/input[3]').get_attribute('value')

# Dar submit no sing-up

navegador.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/a[3]').click()

# Guardar os dados em um arquivo, para o fácil acesso

with open('info.txt', 'a', newline='') as arquivo:
    arquivo.write(f"email: {email}, senha: {password}   ")


