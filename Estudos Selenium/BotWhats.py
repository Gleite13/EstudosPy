from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://web.whatsapp.com/')

while True:
    while len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/canvas')):
        pass

    while len(navegador.find_elements(By.ID, 'side')) < 1:
        pass
    
    #grupo = navegador.find_element(By.ID,'//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div/div[2]')
    #grupo.click()