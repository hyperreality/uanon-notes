import requests
import string
import time

def check(url):
    r = requests.head(url, allow_redirects=False)
    print(r.status_code)
    if r.status_code == 301:
        return r.headers.get('Location')
    elif r.status_code == 404:
        return False
    else:
        exit(f'{url}: {r.status_code}')


attempt = "ikiiik"

i1 = attempt[0].upper()
i2 = attempt[1].upper()
i4 = attempt[2]
i5 = attempt[3].upper()
i6 = attempt[4].upper()
for i3 in string.digits:
    url = f"https://bit.ly/4{i1}{i2}{i3}{i4}{i5}{i6}"
    location = check(url)
    if location:
        print(f"{url} {location}")
    time.sleep(0.5)
