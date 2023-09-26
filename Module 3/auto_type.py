import pyautogui
from time import*
sleep(5)
for i in range(0,10):
    pyautogui.write('I love you ,python', interval=0.25)
    pyautogui.press('enter')