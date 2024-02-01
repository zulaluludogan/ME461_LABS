import sys
import time
import select
from machine import PWM, Pin, ADC

# Pin Definitions
coil1 = Pin(10,Pin.OUT)
coil2 = Pin(11,Pin.OUT)
coil3 = Pin(14,Pin.OUT)
coil4 = Pin(15,Pin.OUT)

pins = [coil1, coil2, coil3, coil4]

# set up poller for stdin
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)

# initial state variables
i = 0
run_mode = 0
stop_mode = 0
act_sequence = []
delay = 30000

if __name__ == "__main__":
    
    while True:
        
        # proccess message
        if poller.poll(0):
            stepper_message = sys.stdin.readline().strip("\n")
        
            i = int(stepper_message[0])
            run_mode = int(stepper_message[2])
            stop_mode = int(stepper_message[4])
            delay = int(stepper_message[6])
            act_sequence = stepper_message[10:].rstrip("]'").split("', '")

        
        if not stop_mode:
            if run_mode == 1 : # apply single step
                for j in range(len(pins)):
                    print(act_sequence[i])
                    print(i)
                    step = act_sequence[i].lstrip("'") 
                    pins[j].value(int(step[j])) 
                    
            elif run_mode == 0 : # continuous mode
                for step in act_sequence:
                    for j in range(len(pins)):

                        pins[j].value(int(step[j])) 
                        time.sleep_ms(delay)
        else:
            for j in range(len(pins)):
                pins[j].value(0) 
        
        time.sleep_ms(15)


