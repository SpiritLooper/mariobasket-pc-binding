import pyautogui
from time import sleep


def sanitize(str):
    s = str.strip().split(',')
    return int(s[0][1:]), int(s[1][0:len(s[1])-1])

def load_rect():
    f = open("rect.txt", 'r')
    res = f.read()
    f.close()
    p1, p2 = res.split('\n')
    x1 , y1 = sanitize(p1)
    x2 , y2 = sanitize(p2)

    if x1 > x2:
        x1 , x2 = x2, x1    
    if y1 > y2:
        y1 , y2 = y2, y1

    return (x1 , y1), (x2 , y2)

class AbstractCommand:
    def __init__(self) -> None:
        self.minP, self.maxP = load_rect()
    
    def run(self, **params):
        raise NotImplementedError
    
    def get_abs_coords(self, x_rel,y_rel):
        return self.minP[0] + x_rel, self.minP[1] + y_rel
    
    def get_coords_ratio(self, ratio_x, ratio_y):
        lenX = self.maxP[0] - self.minP[0]
        lenY = self.maxP[1] - self.minP[1]
        return self.minP[0] + lenX * ratio_x ,  self.minP[1] + lenY * ratio_y 

class Dribble(AbstractCommand):
    def run(self, x_ratio, y_ratio):
        x, y = self.get_coords_ratio(x_ratio, y_ratio)
        pyautogui.mouseDown(x, y)
        sleep(0.2)
        pyautogui.mouseUp()



