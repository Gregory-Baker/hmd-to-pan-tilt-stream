
"""
Set a ('90' deg range) servo to a specified angle
"""

import pi_servo_hat
import time
import atexit

# Initialize Constructor
test = pi_servo_hat.PiServoHat()

# Restart Servo Hat (in case Hat is frozen/locked)
test.restart()

servo_no = int(input("Enter no. of servo to control (0-3): "))

# Test Run
#########################################
# Moves servo position to 0 degrees (1ms), Channel 0
test.move_servo_position(servo_no, 0)


# Pause 1 sec
time.sleep(1)

# Sweep
#########################################
while True:
    try:
        servo_angle = input("Enter desired servo angle (deg): ")
        test.move_servo_position(servo_no, int(servo_angle))
    except KeyboardInterrupt:
        test.restart()
        


