import socket
import wifi
import machine
import webfiles
import tools
import buttons
import ir_read
from machine import Pin, PWM
import time
import hw_buttons
import ujson
import update

REPO_URL = "https://raw.githubusercontent.com/Kerbaltec-Solutions/Everymote/refs/heads/main/"

import gc
gc.collect()

led=Pin(2,Pin.OUT)
led.off()

ir_led=PWM(Pin(16), freq=38000, duty_u16=0)

hw_buttons.init(led, ir_led)

configure=False

led.on()
ir_read.calibrate(ir_led)
led.off()

try:
    with open('WIFI.p', 'r') as rf:
        WiFi_cred=ujson.load(rf)
except:
    WiFi_cred=['','']

# Function to handle incoming connections
def web_page(response,conn,type):
    led.on()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send(f'Content-Type: {type}\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    led.off()

if(WiFi_cred[0] == "" or not wifi.connect(WiFi_cred[0], WiFi_cred[1], 40)):
    # Setup access point
    ap=wifi.accessP()
    configure = True

# Setup socket web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 80))
except:
    machine.reset()
s.listen(5)

def answer(conn,request):
    if 'GET /connect' in request:
        ssid = tools.get_between(request,'ssid=','&')
        password = tools.get_between(request,'password=','&')

        if(wifi.connect(ssid, password, 20)):
            ap.active(False) 
            WiFi_cred = [ssid,password]
            with open('FIFI.p', 'w') as rf:
                ujson.dump(WiFi_cred, rf)
            machine.reset()

    elif 'GET /remotes/add' in request:
        remote = tools.get_between(request,'remote=','&')

        buttons.new_remote(remote)

        web_page(webfiles.build_redirect(f'/'),conn,"text/html")

    elif 'GET /remotes/rm' in request:
        remote = tools.get_between(request,'remote=','&')

        buttons.remove_remote(remote)

        web_page(webfiles.build_redirect(f'/'),conn,"text/html")

    elif 'GET /buttons/add' in request:
        remote = tools.get_between(request,'remote=','&')
        button = tools.get_between(request,'button=','&')
        sequences = []

        led.on()
        nulls=0
        while(nulls<6):
            seq = ir_read.listen()
            print(seq)
            if(len(seq)==0):
                nulls+=1
            else:
                sequences.append(seq)
                led.off()
                time.sleep_ms(500)
                led.on()
                nulls=0
        led.off()

        buttons.edit_button(remote,button,sequences)
        
        web_page(webfiles.build_redirect(f'/remotes?page={remote}'),conn,"text/html")

    elif 'GET /buttons/rm' in request:
        remote = tools.get_between(request,'remote=','&')
        button = tools.get_between(request,'button=','&')

        buttons.remove_button(remote,button)

        web_page(webfiles.build_redirect(f'/remotes?page={remote}'),conn,"text/html")

    elif 'GET /remotes' in request:
        if 'page=' in request:
            page = tools.get_between(request,'page=','&')
            if page == "NEW Remote":
                web_page(webfiles.remote_form,conn,"text/html")
            elif page == "REMOVE Remote":
                web_page(webfiles.build_remoteRM_form(),conn,"text/html")
            elif page=="HOME":
                web_page(webfiles.build_redirect(f'/'),conn,"text/html")
            elif page=="EDIT or ADD button":
                remote = tools.get_between(request,'remote=','&')
                web_page(webfiles.build_button_form(remote),conn,"text/html")
            elif page=="REMOVE button":
                remote = tools.get_between(request,'remote=','&')
                web_page(webfiles.build_buttonRM_form(remote),conn,"text/html")
            elif page=="UPDATE":
                web_page(webfiles.update_page,conn,"text/html")
                update.update(led)
            else:
                web_page(webfiles.build_buttons(page),conn,"text/html")
        elif 'button=' in request:
            button = tools.get_between(request,'button=','&')
            remote = tools.get_between(request,'remote=','&')

            web_page(webfiles.build_buttons(remote),conn,"text/html")

            for seq in buttons.get_button(remote,button):
                led.on()
                ir_read.send(seq, ir_led)
                led.off()
            
    elif(configure):
        web_page(webfiles.wifi_form,conn,"text/html")

    else:
        web_page(webfiles.build_remotes(),conn,"text/html")

    print("Ready...")

def accept():
    try:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        
        print('Content = %s' % request)

        request = request.split(" HTTP")[0]

        request = tools.replace(request)

        answer(conn, request)
    except:
        pass