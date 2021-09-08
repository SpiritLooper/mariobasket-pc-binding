from time import sleep
from command import Dribble
from math import sin, cos

if __name__ == '__main__':
    dr = Dribble()
    for i in range(20):
        dr.run(0.5 + cos(i)/2.0, 0.5 + sin(i)/2.0)
        sleep(0.5)
