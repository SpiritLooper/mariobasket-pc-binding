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
