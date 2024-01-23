import time
import rp2
from machine import PWM, Pin, ADC

direction = 0

##### PIN DEFINITIONS
motorA = Pin(19, Pin.OUT)
motorB = Pin(18, Pin.OUT)

motorA_pwm = PWM((motorA), freq=50, duty_u16=0)
motorB_pwm = PWM((motorB), freq=50, duty_u16=0)

pot = ADC(26)

# motorA.off()
# motorB.off()


##### BUTTON ISRs
# button R MotorB
# button L MotorA
def isr_buttonL(pin):
    global direction
    direction = 1

def isr_buttonR(pin):
    global direction
    direction = 2
   
p16 = Pin(16, Pin.IN)
p17 = Pin(17, Pin.IN)

p16.irq(trigger=Pin.IRQ_FALLING, handler=isr_buttonR)
p17.irq(trigger=Pin.IRQ_RISING, handler=isr_buttonL)


#########################################################

if __name__ == "__main__":
    while True:
        duty_cycle = pot.read_u16()
        if direction == 1:
            motorA_pwm.duty_u16(duty_cycle)
            motorB_pwm.duty_u16(0)
        elif direction == 2:
            motorA_pwm.duty_u16(0)
            motorB_pwm.duty_u16(duty_cycle)
        
        
        
    