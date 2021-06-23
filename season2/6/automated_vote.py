import requests
import hashlib
import json
import itertools
import time
import os.path
import sys
import string

import create_account


ALPHA = string.ascii_uppercase + string.ascii_lowercase + string.digits

VOTING_FOR_ADDRESS = "tz1Ra4zkxQpN8h6gREin8f2ne5a6BqTwYNos"

sess = requests.Session()

def make_vote(timestamp, vote, target_hash, seed):
    global session
    headers = {
        'authority': 'api.uanon.observer',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://uanon.observer',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://uanon.observer/',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f"Bearer {session}"
    }

    data = {"timestamp":timestamp,"vote":vote,"hash":target_hash,"seed":seed}
    print(data)
    response = sess.post('https://api.uanon.observer/election/vote', headers=headers, json=data)
    print(response.text)
    created = response.json()['message']['voted']['created']
    print(created)
    with open(SAVEFILE, 'w') as f:
        f.write(str(created))

    return response.json()['message']['voted']['created'], response.json()['message']['voted']['work']

def refresh_token_req(refresh_token):
    global session
    headers = {
        'authority': 'api.uanon.observer',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://uanon.observer',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://uanon.observer/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"token": refresh_token}
    response = requests.post('https://api.uanon.observer/auth/refresh_token', headers=headers, json=data)
    print(response.text)
    access_token = response.json()['access_token']
    session = access_token

def hsh(timestamp, address, seed):
    data = (str(timestamp) + address + seed).encode()
    return hashlib.md5(data).hexdigest()

def brute(timestamp, address, target_hash):
    #timestamp = int(time.time() * 1000)
    for i in itertools.product(ALPHA, repeat=7):
        seed = "".join(i)
        hashed = hsh(timestamp, address, seed)
        if hashed[:5] == target_hash:
            return timestamp, seed

def brute2(timestamp, address):
    seed = "AAAAAAA"
    hashed = hsh(timestamp, address, seed)
    return timestamp, seed, hashed[:5]


def register_for_vote():
    global session
    headers = {
        'authority': 'api.uanon.observer',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://uanon.observer',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://uanon.observer/',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f"Bearer {session}"
    }
    data = {"register":True}
    response = requests.post('https://api.uanon.observer/election/register', headers=headers, json=data)
    print(response.text)

tokens, address = create_account.register()
with open(address, 'w') as f:
    f.write(json.dumps(tokens))
refresh_token = tokens["refresh_token"]
refresh_token_req(refresh_token)
register_for_vote()

SAVEFILE = f"{address}.save"

if os.path.isfile(SAVEFILE):
    with open(SAVEFILE) as f:
        timestamp = int(f.read().strip())
else:
    # timestamp = 1624244726087
    timestamp = int(time.time() * 1000)
target_hash = "cb63b"

for i in range(100000000):
    timestamp, seed = brute(timestamp, address, target_hash)
    timestamp, target_hash = make_vote(timestamp, VOTING_FOR_ADDRESS, target_hash, seed)
    time.sleep(30)
    if i != 0 and i % 10 == 0:
        refresh_token_req()

