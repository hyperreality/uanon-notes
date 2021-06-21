import requests
import hashlib
import json
import itertools
import time
import os.path
import sys

import string
ALPHA = string.ascii_uppercase + string.ascii_lowercase + string.digits

addresses = {
    "hyper": "tz1Ra4zkxQpN8h6gREin8f2ne5a6BqTwYNos",
    "marcos": "tz1L9g4SaPvg5uwZbCvEwbySu2hgwLb3qSGJ",
    "murdock": "tz1YR1xrSJcrRxyiP3t2XjDMeR7HQd7Ftx7E",
    "obedient": "tz1MDKxang5ESAAbQmGA6WLyXE9C35qNyM25",
    "ajiv": "tz1PXQ6Bde6fXrb17Y45EA4ipzsa54oeMA4P",
    "void": "tz1c7DxQ458d3cZpRS3i1LjvksTR2HnwUojR",
    "juicy": "tz1gbmCFAW9PxkvgJkrrK31ZGs8Uno7AthAR",
    "booty": "tz1dVAVAoed6n56btP9ZRTsKvZgFHE7CnYr5",
    "solo": "tz1heX8RszReXS9mMPeRYYZh5KXXa68bzPmx",
    "bezos": "tz1KtdUyM94tKcNgHak8o4NjFaetg1uJi6ht",
    "nolan": "tz1bwJgigF7MJxZqH29eYGiWhPzmJnkboHpo",
    "carl": "tz1XmJn8EBjzGhL1zut4gRGjFxpZzjQkyMhV",
}

WHOAMI = sys.argv[1]
VOTING_FOR = "hyper"
WHOAMI_ADDRESS = addresses[WHOAMI]
VOTING_FOR_ADDRESS = addresses[VOTING_FOR]

TOKENFILE = f"{WHOAMI}.token"
SAVEFILE = f"last_timestamp.{WHOAMI}.save"

# get using JSON.parse(localStorage.getItem("auth-tokens-production"))['refreshToken']
if not os.path.isfile(TOKENFILE):
    raise Exception(f"must add your refresh token to {TOKENFILE}")
else:
    with open(TOKENFILE) as f:
        TOKEN = f.read().strip()
        print(TOKEN)

if os.path.isfile(SAVEFILE):
    with open(SAVEFILE) as f:
        timestamp = int(f.read().strip())
else:
    timestamp = int(time.time() * 1000)
    timestamp = 1624244726087
target_hash = "cb63b"
session = None

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

def refresh_token():
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

    data = {"token": TOKEN}
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


for i in range(100000000):
    if i % 10 == 0:
        refresh_token()
    timestamp, seed = brute(timestamp, WHOAMI_ADDRESS, target_hash)
    #timestamp, seed, target_hash = brute2(timestamp, HYPER_ADDRESS)
    timestamp, target_hash = make_vote(timestamp, VOTING_FOR_ADDRESS, target_hash, seed)
    time.sleep(30)

