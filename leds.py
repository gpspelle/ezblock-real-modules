#!/usr/bin/env python3
import RPi.GPIO as GPIO
from ezblock import PWM

class Leds():
    def __init__(self, led_colors=['red', 'yellow', 'green'], available_pins=['P9', 'P10', 'P11']):
        self.available_pins = available_pins 
        self.leds = self.__create_leds(led_colors)

    # private method
    def __create_leds(self, led_colors):
        leds = dict()
        for color in led_colors:
            leds[color] = dict()
            leds[color]['state'] = 0

            try:
                leds[color]['pin'] = self.available_pins.pop(0) # pop(0) to get first available pin
                leds[color]['pwm'] = PWM(leds[color]['pin'])
                leds[color]['pwm'].freq(50)           # set frequency (go)
                leds[color]['pwm'].pulse_width(0)          # off it

            except IndexError as e:
                print("Not enough available pins to perform led creation", led_colors, e)

        print(" [.] Created leds", leds)
        return leds


    def stop(self):
        for color in self.leds:
            if self.leds[color]['state']:
                self.leds[color]['pwm'].off()          # off it

    def toggle(self, color):
        try:
            if self.leds[color]['state'] == 0:
                self.leds[color]['pwm'].pulse_width(100)         # set pulse_width (go)
            else:
                self.leds[color]['pwm'].pulse_width(0)          # off it

            self.leds[color]['state'] = 1 - self.leds[color]['state']
        except KeyError as e:
            print("The color", color, "doesn't exist!")
            print("Available colors:", self.leds)
                    




