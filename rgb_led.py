#!/usr/bin/env python3
from ezblock.modules import RGB_LED
from ezblock import PWM

class RGB():
    def __init__(self, p_red="P9", p_green="P10", p_blue="P11"):
        self.rgb = RGB_LED(PWM(p_red), PWM(p_green), PWM(p_blue))
        self.color_dict = {'red': '#ff0000', 'orange': '#ffa500', 'yellow': '#ffff00', 'green': '#008000', 'blue': '#0000ff', 'indigo': '#4b0082', 'violet': 'ee82ee', 'white': '#ffffff', 'black': '000000'}

    def write(self, color):
        print(" [.] Update RGB led state to", color)
        color = self.color_dict[color]
        self.rgb.write(color)
        

