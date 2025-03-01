import network
import time

network.hostname("everymote")

def connect(ssid,key,timeout):
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid,key)
        while not wlan.isconnected():
            time.sleep_ms(500)
            timeout-=1
            if(timeout==-1):
                wlan.active(False)
                return False
    print('network config:', wlan.ipconfig('addr4'))
    return True

def accessP():  
    ap = network.WLAN(network.WLAN.IF_AP) 
    ap.config(ssid='Everymote-setup')
    ap.config(max_clients=10)
    ap.active(True) 
    print('network config:', ap.ipconfig('addr4'))
    return(ap)

