from hashlib import blake2b
import json
import itertools
from struct import pack
from binascii import hexlify, unhexlify

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

def submit_answer(message, secret, depth=1):
    proof = generate_proof(message, depth=depth)
    if proof == secret:
        print(f'[FOUND]: {message}')
        exit()

def print_proof(*message):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    print(magic_bytes + length + passphrase)


"""
ranges
1:31 1:33
3:07 3:09
3:07 3:09
3:40 3:42
3:42 3:44
4:06 4:08
4:16 4:18
4:18 4:19
"""

TIMES = [
    ["00:01:31", "00:01:32", "00:01:33"],
    ["00:03:07", "00:03:08", "00:03:09"],
    ["00:03:07", "00:03:08", "00:03:09"],
    ["00:03:40", "00:03:41", "00:03:42"],
    ["00:03:42", "00:03:43", "00:03:44"],
    ["00:04:06", "00:04:07", "00:04:08"],
    ["00:04:16", "00:04:17", "00:04:18"],
    ["00:04:18", "00:04:19"],
]

secret = "09f8b6eaef24133b83a5db28c21b56d3375d3bcfc2c2460edd315ebcd0249d2a"


for t1 in TIMES:
    for t2 in TIMES:
        bla = TIMES.copy()
        bla.append(t1)
        bla.append(t2)
        bla = sorted(bla)
        for out in itertools.product(*bla):
            out = sorted(out)
            submit_answer(out, secret)
