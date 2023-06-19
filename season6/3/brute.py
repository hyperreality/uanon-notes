from hashlib import blake2b
import json
import itertools
from struct import pack
from binascii import hexlify, unhexlify
from tqdm import tqdm

def hash(message, rounds=1):
    h = message
    for i in range(rounds):
        if i + 1 == rounds:
            h = blake2b(h, digest_size=32).hexdigest()
        else:
            h = blake2b(h, digest_size=32).digest()
    return h

def stringify(message):
    if isinstance(message, str):
        message = [message]
    return json.dumps(message, separators=(',', ':')).encode('utf8')

def generate_proof(message, depth=1):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    # print(passphrase)
    length = pack('>l', len(passphrase))
    return hash(magic_bytes + length + passphrase, rounds=depth)

def verify_proof(proof, secret, depth=2, start_depth=1):
    rounds = depth - start_depth
    proof_bytes = unhexlify(proof.encode('utf8'))
    return hash(proof_bytes, rounds=rounds) == secret

def submit_answer(message, secret, depth=2):
    proof = generate_proof(message, depth=depth)
    if proof == secret:
        print(f'[FOUND]: {message}')
        exit()

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(enc, password):
    unhexed = enc
    if len(password) > 32:
        return ""
    else:
        password += b" " * (32 - len(password))
    # unhexed_pass = bytes.fromhex(password)
    # print("IV")
    # print(unhexed[:16])
    # print("Encrypted")
    # print(unhexed[16:])
    # print(password)
    # print(unhexed[:16])
    cipher = AES.new(password, AES.MODE_CBC, unhexed[:16])
    dec = cipher.decrypt(unhexed[16:])
    try:
        pad = int(dec[-1])
    except:
        return ""

    out = dec

    if all([ord(a) < 128 for a in out.decode('latin-1')]):
        print(out)
        return out


with open("trace1.txt.enc", "rb") as f:
    trace1 = f.read()
with open("trace3.txt.enc", "rb") as f:
    trace3 = f.read()


import string
alpha = string.ascii_uppercase + string.digits

for o in alpha:
    for o2 in alpha:
        for i1 in alpha:
            for i2 in alpha:
                for i3 in alpha:
                    w = f"{o}{i1}{o2}{i2}{o}{o2}{i3}{o}"
                    # w = w.lower()
                    if decrypt(trace3, w.encode()):
                        print(w)

