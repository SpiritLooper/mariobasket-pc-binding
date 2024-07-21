from screen_move import Move

class AbstractCommand:
    def __init__(self) -> None:
        self.move = Move()

    def run(self, **params):
        raise NotImplementedError

class Dribble(AbstractCommand):
    def run(self, x_ratio, y_ratio):
        self.move.tap(x_ratio, y_ratio)

class Shot(AbstractCommand): 
    def run(self):
        self.move.line(0.5, 0.9, 0.5, 0.1)

class LoadShot(AbstractCommand):
    def run(self, x, y):
        self.move.hold(x,y)

class HitBall(AbstractCommand):
    def run(self):
        self.move.line(0.5, 0.1, 0.5, 0.9)

class Jump(AbstractCommand):
    def run(self):
        self.move.line(0.5, 0.9, 0.5, 0.1)

class Counter(AbstractCommand):
    def run(self, x, y):
        self.move.hold(x,y)

class RealeaseCounter(AbstractCommand):
    def run(self):
        self.move.realease()

class Pass(AbstractCommand):
    def run(self, dir_x, dir_y):
        self.move.line(0.5 - dir_x,0.5 - dir_y, 0.5 + dir_x, 0.5 + dir_y)

class UseItem(AbstractCommand):
    def run(self, dir_x, dir_y):
        self.move.line(0.5 - dir_x,0.5 - dir_y, 0.5 + dir_x, 0.5 + dir_y)

class ShadowStep(AbstractCommand):
    def run(self, dir_x):
        self.move.line(-dir_x + 0.5,0.5, dir_x + 0.5, 0.5)