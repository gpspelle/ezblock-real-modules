'''_dict = {
        "D0":  17,
        "D1":  18,
        "D2":  27,
        "D3":  22,
        "D4":  23,
        "D5":  24,
        "D6":  25,
        "D7":  4,
        "D8":  5,
        "D9":  6,
        "D10": 12,
        "D11": 13,
        "D12": 19,
        "D13": 16,
        "D14": 26,
        "D15": 20,
        "D16": 21,
        "SW":  19,
        "LED": 26,
        "PWR": 12,
        "RST": 16,
        "BLEINT": 13,
        "BLERST": 20,
        "MCURST": 21,
    }
'''
from ezblock import Pin, Ultrasonic

class FrontalDistance():
    def __init__(self, trig="D0", echo="D1"):
        self.ultrasonic = Ultrasonic(Pin(trig), Pin(echo)) # create an Ultrasonic object from pin
        print(" [.] Created ultrasonic object", self.ultrasonic) 

    def read(self):
        return self.ultrasonic.read() # read an analog value


# Usage example
#reader = FrontalDistance()
#print(reader.read())

