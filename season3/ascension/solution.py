import requests
import json
import sys

s = requests.Session()

BASE = "https://api.uanon.observer/"

def refresh_token_req(refresh_token):
    global session
    data = {"token": refresh_token}
    response = requests.post('https://api.uanon.observer/auth/refresh_token', json=data)
    print(response.text)
    access_token = response.json()['access_token']
    return access_token

refresh_token = sys.argv[1]

auth_token = refresh_token_req(refresh_token)

headers = {
    "Authorization": f"Bearer {auth_token}",
    "Accept": "application/json"
}

while True:
    res = s.get(BASE + "navigating-the-fall", headers=headers)
    print(res.text)

    indexes = res.json()["message"]["solverIndexes"]
    options = res.json()["message"]["answerOptions"]

    out = []

    for i, v in enumerate(indexes):
        out.append({"answer": 5, "index": v})


    body = {
        "submit": json.dumps(out)
    }

    print(body)

    res = s.post(BASE + "and-falling-up-the-mountain", headers=headers, json=body)

    print(res.text)
    if not "Fortune does not" in res.text:
        break
