import machine
import time

led_rojo = machine.Pin(15, machine.Pin.OUT)
led_verde = machine.Pin(14, machine.Pin.OUT)
led_azul = machine.Pin(13, machine.Pin.OUT)

led_rojo.value(0)
led_verde.value(0)
led_azul.value(0)

boton = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if boton.value() == 0:
        led_rojo.value(1)
        led_verde.value(0)
        led_azul.value(0)
        print("Rojo")
        time.sleep(2)
    
        led_rojo.value(0)
        led_verde.value(1)
        led_azul.value(0)
        print("Verde")
        time.sleep(2)
    
        led_rojo.value(0)
        led_verde.value(0)
        led_azul.value(1)
        print("Azul")
        time.sleep(2)
        
        led_rojo.value(0)
        led_verde.value(0)
        led_azul.value(0)
        print("Fin de secuencia")
        
    
