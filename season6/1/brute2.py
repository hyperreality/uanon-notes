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


secrets = [
    "9c9dba32b632a6f79d5e467fcfc6a5b8be03845830b0bb929502b8957cc549c1",
]

for s in secrets:
    print(s)

    with open("/usr/share/dict/words") as f:
    # with open("/usr/share/wordlists/entities3.txt") as f:
        words = [a.strip().upper().replace(" ", "") for a in f.readlines()]

    for w in words:
        ans = f"ONLYTHETRUTHWILLFORGETWEARE{w}FREED"
        # print(w)
        submit_answer(ans, s)

