import time
import sys
from machine import PWM, Pin, ADC

servoMotor = Pin(22, Pin.OUT)

servoMotor_pwm = PWM(servoMotor, freq=50, duty_u16=0)
pot = ADC(26)

MAX = 2500000 
MIN = 500000

POT_MIN = 700
POT_MAX = 51000


if __name__ == "__main__":
    while True:
        servo_position = MIN + int( (MAX - MIN) * pot.read_u16()/(POT_MAX - POT_MIN) ) # Linear Interpolation
        servoMotor_pwm.duty_ns(int(servo_position))
        
        time.sleep_ms(20)
