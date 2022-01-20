import pyautogui as pg 
import time
time.sleep(15)
txt =open('animals.txt','r')
a ="Prince Ghouse is "

for i in txt:
    pg.write(a+" "+i)
    pg.press('Enter')
    