import pyautogui
from time import sleep

pyautogui.moveTo(1215, 368, duration=1)
for i in range(1000):
    sleep(0.5)
    pyautogui.click()
