import time
import rp2
import sys
from machine import PWM, Pin, ADC

# 
motor_number = 0 # 0 by default, 0 -> motor A, 1 -> motor B

##### PIN DEFINITIONS
motorA1 = Pin(19, Pin.OUT)
motorA2 = Pin(18, Pin.OUT)

motorA1_pwm = PWM(motorA1, freq=50, duty_u16=0)
motorA2_pwm = PWM(motorA2, freq=50, duty_u16=0)

motorB1 = Pin(21, Pin.OUT)
motorB2 = Pin(20, Pin.OUT)

motorB1_pwm = PWM(motorB1, freq=50, duty_u16=0)
motorB2_pwm = PWM(motorB2, freq=50, duty_u16=0)

#########################################################
if __name__ == "__main__":
    while True:

        # Read the input sent from the computer into stdin buffer then convert it into integer
        motor_message = list(map(int,sys.stdin.readline().strip("\f").split(" ")))
       
        # If empty no message received just skip
        if motor_message == []: 
            time.sleep_ms(15)
            continue
        
        # Parse Message from GUI
        motor_number = motor_message[0]
        motor_state = motor_message[1]
        motor_direction = motor_message[2]
        motor_dutyCycle = motor_message[3]
        motor_pwmFreq = motor_message[4]
    
        if not motor_number: # if motor A
            if not motor_state: # if should be turned off
                motorA1_pwm.duty_u16(0) # turn off
                motorA2_pwm.duty_u16(0)
            else:
                if motor_direction == 0 :  # ccw
                    motorA1_pwm.duty_u16(motor_dutyCycle)
                    motorA1_pwm.freq(motor_pwmFreq)
                    motorA2_pwm.duty_u16(0)
                    #motorA2_pwm.freq(20) 
                    
                elif motor_direction == 1 :  # cw
                    motorA1_pwm.duty_u16(0)
                    #motorA1_pwm.freq(20)
                    motorA2_pwm.duty_u16(motor_dutyCycle)
                    motorA2_pwm.freq(motor_pwmFreq)          
        else: # if motor B
            if not motor_state: 
                motorB1_pwm.duty_u16(0)
                motorB2_pwm.duty_u16(0)
            else:
                if motor_direction == 0 :  # ccw
                    motorB1_pwm.duty_u16(motor_dutyCycle)
                    motorB1_pwm.freq(motor_pwmFreq)
                    motorB2_pwm.duty_u16(0)
                    motorB2_pwm.freq(20) 
                    
                elif motor_direction == 1 :  # cw
                    motorB1_pwm.duty_u16(0)
                    motorB1_pwm.freq(20)
                    motorB2_pwm.duty_u16(motor_dutyCycle)
                    motorB2_pwm.freq(motor_pwmFreq)    
            
        time.sleep_ms(15)
        

