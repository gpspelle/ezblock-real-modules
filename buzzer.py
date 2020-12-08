#!/usr/bin/env python3
from ezblock.modules import Buzzer
from ezblock import PWM

class Buzz():
    def __init__(self, pwm="P8"):
        self.buzz = Buzzer(PWM(pwm))
        self.notes = {"E7" : 2637, "F7" : 2793, "G7" : 3136, "A7" : 3520, "B7" : 3951}

    def play(self, note, duration=1000):
        # duration is in ms

        print(" [.] Playing", note)
        freq = self.notes[note]
        self.buzz.play(freq, duration)

# Usage example
#buzz = Buzz()
#buzz.play("B7")
