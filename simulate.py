import requests
import time

url = "http://127.0.0.1:5000/simulate"

for i in range(200):
    r = requests.post(url)
    print(i, r.json())
    time.sleep(0.05)  # reduce delay for faster attack
