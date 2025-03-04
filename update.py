import requests
import machine
import time

REPO_URL = "https://raw.githubusercontent.com/Kerbaltec-Solutions/Everymote/refs/heads/main/"

def update(led):
    print("UPDATING")
    response = requests.get(REPO_URL+"files.md")
    if response.status_code == 200:
        for file in response.text.split(","):
            print(file)
            retrys = 5
            while retrys>0:
                try:
                    response_f = requests.get(REPO_URL+file)
                    if response_f.status_code == 200:
                        with open(file, "w", encoding="utf-8") as f:
                            f.write(response_f.text)
                            led.on()
                            time.sleep_ms(250)
                            led.off()
                            print("SUCCESS")
                            retrys=0
                    else:
                        retrys-=1
                except:
                    retrys-=1
    else:
        print("Failed to update. HTTP Code:", response.status_code)
    led.on()
    time.sleep(1)
    machine.reset()