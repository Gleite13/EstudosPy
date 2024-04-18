import pyautogui
import time

time.sleep(7)
file = open("shrek.txt", "r")


for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")