import time
import sys
from machine import PWM, Pin, ADC

servoMotor = Pin(15, Pin.OUT)
servoMotor_pwm = PWM(servoMotor, freq=50, duty_u16=0)

pot = ADC(26)

MAX = 2500000
MIN = 500000
MID = 1500000

POT_MIN = 700
POT_MAX = 51000


if __name__ == "__main__":
    while True:
        servo_message = sys.stdin.readline().strip("\f").split(" ")
        print(servo_message)
        servo_position = MIN + (servo_message[0]/65536) * (MAX - MIN)
        servoMotor_pwm.duty_ns(int(servo_position))
        time.sleep_ms(15)

