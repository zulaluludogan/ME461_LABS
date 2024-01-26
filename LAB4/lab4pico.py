import time
import rp2
import sys
from machine import PWM, Pin, ADC

# 
motor_number = 0 # 0 by default, 0 -> motor A, 1 -> motor B

##### PIN DEFINITIONS
motorA1 = Pin(19, Pin.OUT)
motorA2 = Pin(18, Pin.OUT)

motorA1_pwm = PWM((motorA1), freq=50, duty_u16=0)
motorA2_pwm = PWM((motorA2), freq=50, duty_u16=0)

#########################################################

if __name__ == "__main__":
    while True:

        # Read the input sent from the computer into stdin buffer
        motor_message = sys.stdin.readline().strip("\f").split(" ")
        
        if motor_message == "": 
            time.sleep_ms(15)
            continue

        motor_number = motor_message[0]
        motor_state = motor_message[1]
        motor_direction = motor_message[2]
        motor_dutyCycle = motor_message[3]
        motor_pwmFreq = motor_message[4]
    
        if not motor_number:
            if not motor_state: 
                motorA1.duty_u16(0)
                motorA2.duty_u16(0)
            else:
                if motor_direction == 0 :  # ccw
                    motorA1_pwm.duty_u16(motor_dutyCycle)
                    motorA2_pwm.duty_u16(0)
                elif motor_direction == 1 :  # cw
                    motorA1_pwm.duty_u16(0)
                    motorA2_pwm.duty_u16(motor_dutyCycle)
                # motorA1_pwm.freq(motor_pwmFreq)
                # motorA2_pwm.freq(motor_pwmFreq)               

        time.sleep_ms(15)



        
        
        
    