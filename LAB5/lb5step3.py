import time
import sys
from machine import PWM, Pin, ADC

servoMotor = Pin(22, Pin.OUT)
servoMotor_pwm = PWM(servoMotor, freq=50, duty_u16=0)

MAX = 2500000
MIN = 500000

servo_position = MIN + int((MAX - MIN) * argv/180) # linear interpolation of the max and minimum positions

# if invalid value release the servo
if servo_position > MAX or servo_position < MIN:
    servoMotor_pwm.deinit()
    
servoMotor_pwm.duty_ns(servo_position)
time.sleep_ms(5)

#usage exec(open("lb5step3.py").read(), {'argv': degree})
