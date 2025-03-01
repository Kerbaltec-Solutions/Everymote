import requests
import machine
import time

REPO_URL = "https://raw.githubusercontent.com/Kerbaltec-Solutions/Everymote/refs/heads/main/"

def update(led):
    response = requests.get(REPO_URL+"files.md")
    if response.status_code == 200:
        for file in response.text.split(","):
            print(file)
            response_f = requests.get(REPO_URL+file)
            if response_f.status_code == 200:
                with open(file, "w", encoding="utf-8") as f:
                    f.write(response_f.text)
    else:
        print("Failed to update. HTTP Code:", response.status_code)
    led.on()
    time.sleep(1)
    machine.reset()