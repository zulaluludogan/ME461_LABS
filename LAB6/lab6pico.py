import time
import sys
from machine import PWM, Pin, ADC

coil1 = Pin(19,Pin.OUT)
coil2 = Pin(18,Pin.OUT)
coil3 = Pin(17,Pin.OUT)
coil4 = Pin(16,Pin.OUT)

pins = [coil1, coil2, coil3, coil4]


if __name__ == "__main__":
    while True:
        stepper_message = sys.stdin.readline().strip("\f").split(" ")

        i = int(stepper_message[0])
        run_mode = int(stepper_message[1])
        stop_mode = int(stepper_message[2])
        delay = float(stepper_message[3])
        act_sequence = list(stepper_message[4])

        if not stop_mode:
            if run_mode == 1 : # apply single step
                for j in range(len(pins)):
                    step = list(act_sequence[i]) # e.g. act_sequence[i] = [1,0,0,0]
                    pins[j].value(step[j]) 
                    time.sleep_ms(1)

            elif run_mode == 0 : # continuous mode
                for step in act_sequence:
                    for j in range(len(pins)):
                        pins[j].value(step[j]) 
                        time.sleep_ms(delay)

        else:
            for j in range(len(pins)):
                pins[j].value(0) 
        
        time.sleep_ms(15)