from time import sleep
from controller_handler import XboxController
from pyautogui import hold
from command import Dribble, HitBall, LoadShot, Pass, ShadowStep, Shot
from math import sin, cos

if __name__ == '__main__':
    handler = XboxController()
    while True:
        sleep(0.2)
