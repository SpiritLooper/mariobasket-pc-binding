from inputs import get_gamepad
import math
import threading
from command import Dribble, HitBall, Jump, LoadShot, Pass, ShadowStep

j = Jump()
h = HitBall()
d = Dribble()
ls = LoadShot()
p = Pass()
ss = ShadowStep()

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        X = self.X
        Y = self.Y
        A = self.A
        B = self.B 
        rb = self.RightTrigger
        return [X, Y, A, B, (self.LeftJoystickX, self.LeftJoystickY), rb]

    def exec_commands(self):
        if self.X:
            self.X = 0
            jump = threading.Thread(target=j.run)
            jump.start()

        if self.B:
            self.B = 0
            hit = threading.Thread(target=h.run)
            hit.start()

        if self.A:
            pass_mate = threading.Thread(target=p.run, args=((self.LeftJoystickX/2.), (-self.LeftJoystickY/2.)))
            pass_mate.start()

        if self.Y: 
            step = threading.Thread(target=ss.run, args=(self.LeftJoystickX/2.,))
            step.start()

        if self.RightTrigger >= 0.1: 
            load = threading.Thread(target=ls.run, args=((self.LeftJoystickX + 1.) /2.1, (-self.LeftJoystickY + 1.) /2.1 ))
            load.start()

        # Dribbling
        if (0.25 <= self.RightJoystickX or -0.25 >= self.RightJoystickX) or \
            (0.25 <= self.RightJoystickY or -0.25 >= self.RightJoystickY)   :
            dribble = threading.Thread(target=d.run, args=((self.RightJoystickX + 1.) /2.1, (-self.RightJoystickY + 1.) /2.1 ))
            dribble.start()
        

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state
            self.exec_commands()
if __name__ == '__main__':
    joy = XboxController()
    while True:
        print(joy.read())