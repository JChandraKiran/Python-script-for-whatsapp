import pyautogui as pg
import time
count = 1
while count <= 100:
    pg.click(477,692)
    time.sleep(0.1)
    pg.write('{}. I Love You'.format(count))
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
    count +=1
