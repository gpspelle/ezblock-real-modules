from ezblock import PWM, Pin
import time

class Wheels():

    def __init__(self, motor1_pwm_pin="P13", motor2_pwm_pin="P12", motor1_dir_pin="D4", motor2_dir_pin="D5"):

        self.motor1_pwm = PWM(motor1_pwm_pin)
        self.motor2_pwm = PWM(motor2_pwm_pin)
        self.motor1_dir = Pin(motor1_dir_pin)
        self.motor2_dir = Pin(motor2_dir_pin)

        self.motor_direction = [self.motor1_dir, self.motor2_dir]
        self.motor_speed = [self.motor1_pwm, self.motor2_pwm]

        print(" [.] Created left and right wheel in stop position")

        self.cali_dir_value = [1, -1]
        self.cali_speed_value = [0, 0]

        self.PERIOD = 4095
        self.PRESCALER = 10

        for pin in self.motor_speed:
            pin.period(self.PERIOD)
            pin.prescaler(self.PRESCALER)

        self.motor_direction_calibration(1, 1) # motor1 in forward mode
        self.motor_direction_calibration(2, 1) # motor2 in forward mode


    def stop(self):
        self.set_motor_speed(1, 0)               # Stop motor1
        self.set_motor_speed(2, 0)               # Stop motor2


    def forward(self):
        self.motor_direction_calibration(1, 1) 
        self.motor_direction_calibration(2, -1) 
        self.set_motor_speed(1, 25)               # Speed motor1
        self.set_motor_speed(2, 21)               # Speed motor2


    def right(self):
        self.motor_direction_calibration(1, 1) 
        self.motor_direction_calibration(2, -1) 
        self.set_motor_speed(1, 0)                # Stop motor1
        self.set_motor_speed(2, 25)               # Speed motor2
        

    def left(self):
        self.motor_direction_calibration(1, 1) 
        self.motor_direction_calibration(2, -1) 
        self.set_motor_speed(2, 0)                # Stop motor2
        self.set_motor_speed(1, 25)               # Speed motor1

    
    def backward(self):
        self.stop()

        self.motor_direction_calibration(1, -1) 
        self.motor_direction_calibration(2, 1) 
        self.set_motor_speed(1, 25)
        self.set_motor_speed(2, 21)


    def set_motor_speed(self, motor, speed):
        motor -= 1
        if speed >= 0:
            direction = 1 * self.cali_dir_value[motor]
        elif speed < 0:
            direction = -1 * self.cali_dir_value[motor]
        speed = abs(speed)
        if speed != 0:
            speed = int(speed /2 ) + 30
        speed = speed - self.cali_speed_value[motor]
        if direction > 0:
            self.motor_direction[motor].high()
            self.motor_speed[motor].pulse_width_percent(speed)
        else:
            self.motor_direction[motor].low()
            self.motor_speed[motor].pulse_width_percent(speed)


    def motor_speed_calibration(self, value):
        if value < 0:
            self.cali_speed_value[0] = 0
            self.cali_speed_value[1] = abs(value)
        else:
            self.cali_speed_value[0] = abs(value)
            self.cali_speed_value[1] = 0


    def motor_direction_calibration(self, motor, value):
        # 1: positive direction
        # -1: negative direction
        motor -= 1
        self.cali_dir_value[motor] = value
        

'''# Usage example
wheels = Wheels()

wheels.forward()

time.sleep(5)
wheels.stop()

wheels.right()
time.sleep(2)

wheels.left()
time.sleep(2)

wheels.backward()

time.sleep(2)
wheels.stop()
'''
