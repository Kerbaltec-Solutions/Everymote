import machine
from machine import Pin
import time
import random


pin = Pin(17, Pin.IN)  # Connect IR receiver to GPIO 17
timestamps = []  # Preallocate space for 200 transitions
last_time = 0
calib_fac = 0

def ir_callback(pin):
    global timestamps, last_time
    now = time.ticks_us()
    timestamps.append(time.ticks_diff(now, last_time))
    last_time = now

pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=ir_callback)


def listen():
    machine.freq(240000000)
    global timestamps
    reset()
    last_l = 0
    time.sleep_ms(500)
    while len(timestamps)>last_l:
        last_l=len(timestamps)
        time.sleep_ms(500)
    machine.freq(80000000)
    return read()
    
def continuous(p):
    while(True):
        ir_in=Pin(p,Pin.IN)
        print(ir_in.value())

def reset():
    global timestamps, last_time
    timestamps = [] 
    last_time = time.ticks_us()

def read():
    return timestamps[1:]

def calibrate(ir_led):
    reset()
    send_seq=[random.randint(250,1500) for i in range(10)]
    time.sleep_ms(500)
    send(send_seq,ir_led)
    times = read()
    time_d=[times[i] - send_seq[i] for i in range(len(times))]
    print(times)
    print(time_d)

def send(seq, ir_led):
    seq = [500]+seq
    v=0
    
    for t in seq:
        ir_led.duty(v)
        v=-(v-512)
        time.sleep_us(t+calib_fac)
    ir_led.duty(0)
    time.sleep_ms(500)