import time
import pyautogui

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('mspaint')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(300, 300)

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.25)
        distance -= 5
        pyautogui.drag(0, distance, duration=0.25)
        pyautogui.drag(-distance, 0, duration=0.25)
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.25)

pyautogui.alert('Fim do teste.')
time.sleep(2)
pyautogui.click('btn_ok.png')
pyautogui.hotkey('alt', 'f4')
time.sleep(2)
pyautogui.press('right')
pyautogui.press('enter')
