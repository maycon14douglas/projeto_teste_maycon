import pyautogui as pag
from time import sleep

pag.moveTo(1849, 921, duration=2)
for i in range(100):
    sleep(0.5)
    pag.doubleClick()
