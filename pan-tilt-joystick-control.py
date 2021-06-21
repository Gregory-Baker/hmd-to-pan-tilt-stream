
"""
Control a pan-tilt servo using gamepad joystick inputs
"""

import pi_servo_hat
import time
import atexit
from inputs import get_gamepad
import signal

pan_servo_channel = 0
pan_zero_angle = 67

tilt_servo_channel = 1
tilt_zero_angle = 30

js_axis_max = 32768

servo_hat = pi_servo_hat.PiServoHat()
servo_hat.restart()


@atexit.register
def reset_servo_hat():
    print("Shutting servos off")
    servo_hat.restart()

class Servo(object):
    
    def __init__(self, channel, zero_angle):
        
        self.channel = channel
        self.zero_angle = zero_angle
        self.servo = self.setup_servo()
        
    def setup_servo(self):
        servo_hat.move_servo_position(self.channel, self.zero_angle)
    
    def set_angle(self, angle):
        servo_hat.move_servo_position(self.channel, angle + self.zero_angle)


def map_input_to_angle(js_value):
    return int(js_value/js_axis_max * 90)



def main():
    pan_servo = Servo(pan_servo_channel, pan_zero_angle)
    tilt_servo = Servo(tilt_servo_channel, tilt_zero_angle)
    time.sleep(1)
    while True:
        events = get_gamepad()
        for event in events:
            if (event.code == 'ABS_X'):
                pan_angle = map_input_to_angle(event.state)
                pan_servo.set_angle(pan_angle)
            if (event.code == 'ABS_RY'):
                tilt_angle = map_input_to_angle(-event.state)
                tilt_servo.set_angle(tilt_angle)
                print(tilt_angle)
                                          
            
if __name__ == "__main__":
    main()
    
