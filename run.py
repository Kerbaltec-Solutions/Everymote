import machine

machine.freq(240000000)

import webserver

while(True):
    webserver.accept()