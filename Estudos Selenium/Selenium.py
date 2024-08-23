from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.youtube.com/watch?v=8AMNaVt0z_M&t=5s")
sleep(5)

navegador.find_element('xpath', '//*[@id="search"]').send_keys("Python")

navegador.find_element('xpath', '//*[@id="search-icon-legacy"]/yt-icon/span/div')