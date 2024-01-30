import time
import sys
from machine import PWM, Pin, ADC

servoMotor = Pin(22, Pin.OUT)
servoMotor_pwm = PWM(servoMotor, freq=50, duty_u16=0)

MAX = 2500000
MIN = 500000

if __name__ == "__main__":
    while True:
        
        servo_message = list(map(int, sys.stdin.readline().strip("\r\f\n").split(" ")))
        
        if servo_message == []:
            time.sleep_ms(1)
            continue
        
        if servo_message[1] == 1:
            servoMotor_pwm.deinit()
        else:
            servo_position = MIN + int((MAX - MIN) * servo_message[0]/65536)
            servoMotor_pwm.init(freq=50, duty_ns=servo_position)
            #servoMotor_pwm.duty_ns(int(servo_position))
        
        time.sleep_ms(5)




