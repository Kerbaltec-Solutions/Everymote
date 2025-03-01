from machine import Pin, PWM
import time
import buttons

pin_b1 = Pin(26, Pin.IN, Pin.PULL_UP)
pin_b2 = Pin(18, Pin.IN, Pin.PULL_UP)
pin_b3 = Pin(19, Pin.IN, Pin.PULL_UP)
pin_b4 = Pin(23, Pin.IN, Pin.PULL_UP)

led = None
ir_led = None

def init(led_p,ir_led_p):
    global led, ir_led
    led=led_p
    ir_led=ir_led_p

def b1_callback(pin):
    for seq in buttons.get_button("BUILTIN","1"):
        led.on()
        v=512
        
        for t in seq:
            ir_led.duty(v)
            v=-(v-512)
            time.sleep_us(t-50)
        ir_led.duty(0)
        led.off()
        time.sleep_ms(500)

def b2_callback(pin):
    for seq in buttons.get_button("BUILTIN","2"):
        led.on()
        v=512
        
        for t in seq:
            ir_led.duty(v)
            v=-(v-512)
            time.sleep_us(t-50)
        ir_led.duty(0)
        led.off()
        time.sleep_ms(500)

def b3_callback(pin):
    for seq in buttons.get_button("BUILTIN","3"):
        led.on()
        v=512
        
        for t in seq:
            ir_led.duty(v)
            v=-(v-512)
            time.sleep_us(t-50)
        ir_led.duty(0)
        led.off()
        time.sleep_ms(500)

def b4_callback(pin):
    for seq in buttons.get_button("BUILTIN","4"):
        led.on()
        v=512
        
        for t in seq:
            ir_led.duty(v)
            v=-(v-512)
            time.sleep_us(t-50)
        ir_led.duty(0)
        led.off()
        time.sleep_ms(500)

pin_b1.irq(trigger=Pin.IRQ_RISING, handler=b1_callback)
pin_b2.irq(trigger=Pin.IRQ_RISING, handler=b2_callback)
pin_b3.irq(trigger=Pin.IRQ_RISING, handler=b3_callback)
pin_b4.irq(trigger=Pin.IRQ_RISING, handler=b4_callback)