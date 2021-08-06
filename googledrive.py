import pyautogui
import time

pyautogui.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('google')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com')
pyautogui.press('enter')
# pyautogui.click('restjanela.png')
time.sleep(1)
pyautogui.hotkey('win','d')
pyautogui.moveTo(113,346)
pyautogui.mouseDown()
pyautogui.moveTo(1096, 532)

pyautogui.hotkey('alt','tab')
pyautogui.mouseUp()
time.sleep(5)
pyautogui.hotkey('alt', 'f4')
pyautogui.alert("O código foi finalizado. Você já pode utilizar o computador!")