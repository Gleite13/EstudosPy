import webbrowser
import openpyxl
import pyautogui
from urllib.parse import quote  # para enviar corretamente a mensagem  dentro do link
from time import sleep

# navegador = webdriver.Chrome()

# navegador.get('https://web.whatsapp.com/')

# while True:
# while len(navegador.find_elements(By.XPATH,
#  '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/canvas')):
# pass

#   while len(navegador.find_elements(By.ID, 'side')) < 1:
#        pass

#    break

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

workbook = openpyxl.load_workbook('clientes.xlsx')
paginaClientes = workbook['Planilha1']

for linha in paginaClientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Olá {nome} seu boleto vence {vencimento}'

    try:
        linkMensagemFormatada = f'https://web.whatsapp.com/send?phone={telefone}&text="{quote(mensagem)}"'
        webbrowser.open(linkMensagemFormatada)
        sleep(10)

        seta = pyautogui.locateOnScreen('seta.png')
        
        sleep(5)

        pyautogui.click(seta[0], seta[1])

        sleep(5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(5)
    except:
        print(f'Não foi possivel mandar a mensagem')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')