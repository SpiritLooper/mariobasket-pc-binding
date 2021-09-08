from time import sleep

from pyautogui import hold
from command import Dribble, LoadShot, Shot
from math import sin, cos

if __name__ == '__main__':
    ls = LoadShot()
    s = Shot()
    ls.run(0.1,0.1)
    sleep(1)
    ls.run(0.5,0.5)
    sleep(1)
    ls.run(0.9,0.9)
    sleep(1)
    s.run()    
