import machine

machine.freq(80000000)

import webserver

while(True):
    webserver.accept()