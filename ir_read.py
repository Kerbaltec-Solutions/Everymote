import machine
from machine import Pin
import time


pin = Pin(17, Pin.IN)  # Connect IR receiver to GPIO 17
timestamps = []  # Preallocate space for 200 transitions
last_time = 0

def ir_callback(pin):
    global timestamps, last_time
    now = time.ticks_us()
    timestamps.append(time.ticks_diff(now, last_time))
    last_time = now

pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=ir_callback)


def listen():
    machine.freq(240000000)
    global timestamps, last_time
    timestamps = []  # Preallocate space for 200 transitions
    last_time = time.ticks_us()
    last_l = 0
    time.sleep_ms(500)
    while len(timestamps)>last_l:
        last_l=len(timestamps)
        time.sleep_ms(500)
    machine.freq(80000000)
    return timestamps[1:]
    
def continuous(p):
    while(True):
        ir_in=Pin(p,Pin.IN)
        print(ir_in.value())