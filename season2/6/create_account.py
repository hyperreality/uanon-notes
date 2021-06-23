import requests
import json
import time
from struct import pack
from pytezos import pytezos
from pytezos.crypto.key import Key

pytezos = pytezos.using(shell='mainnet')
# print(pytezos.shell.node.uri)

def generate_acct():
    newsk = Key.generate(curve=b'p2', export=False)
    sk = newsk.secret_key()
    pk = newsk.public_key()
    address = newsk.public_key_hash()

    return newsk, sk, pk, address

def sig_message(address):
    return "Tezos Signed Message: " + json.dumps({
        "type": 'auth',
        "name": "Project Uanon",
        "pkh": address,
        "expires": int(time.time() * 1000) + (5 * 60 * 1000)
    })


def format_sig(message):
    magic_bytes = b'\x05\x01'
    length = pack('>l', len(message))
    return (magic_bytes + length + message.encode()).hex()


def make_login_signature(newsk_obj, address):
    sig_msg = sig_message(address)
    sig_hex = format_sig(sig_msg)
    print(sig_hex)
    signature = newsk_obj.sign(sig_hex)
    print(signature)
    return sig_hex, signature


def send_login_req(sig_msg, signature, pk):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://uanon.observer',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://uanon.observer/',
        'TE': 'Trailers',
    }
    data = {"msg": sig_msg, "sig": signature, "pubKey": pk}
    print(data)

    response = requests.post('https://api.uanon.observer/auth', headers=headers, json=data)
    print(response.json())

    return response.json()


def register():
    newsk_obj, sk, pk, address = generate_acct()
    sig_hex, sig = make_login_signature(newsk_obj, address)
    tokens = send_login_req(sig_hex, sig, pk)
    return tokens, address


if __name__ == "__main__":
    register()


