import machine
import time
 
led = machine.PWM(machine.Pin(15))
potenciometro = machine.ADC(27)
 
led.freq(1000)
 
while True:
    led.duty_u16(potenciometro.read_u16())
    
