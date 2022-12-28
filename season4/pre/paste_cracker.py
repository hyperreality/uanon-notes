import itertools
import requests
import string
import time

s = requests.Session()

for i in itertools.product(string.ascii_lowercase, repeat=3):
    print("".join(i))

    bla = "".join(i)

    path = f"t9{bla}EtQ"

    res = s.get(f"https://pastebin.com/{path}")

    print(res)

    if res.status_code != 404:
        print("yay")
        exit()

    time.sleep(1)
