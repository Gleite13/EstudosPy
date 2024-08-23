import pyautogui
import time

pyautogui.PAUSE = 0.3

# Mostra a posição do mouse
print(pyautogui.position())
# Mostra o Tamanho da Tela
print(pyautogui.size())
# move mouse para alguma posição
# pyautogui.moveTo(x=, y=)
# Utilizar scroll do mouse
#pyautogui.scroll(-200)


# Funções do Mouse
time.sleep(3)
pyautogui.click(x=232, y=228)

# funções do teclado
pyautogui.write("Escreva algo")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") # comando pyautogui.KEYBORD_KEYS