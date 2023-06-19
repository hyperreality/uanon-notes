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

secret = "d5de6ff254499e6e3a25d97273c9c9c0fe78e54d7f0581cfc46cb89eba5cddef"

bla = [
    ["CECILIA", "ANDREW"],
    ["GREG"],
    ["GABE"],
    ["DR3W", "DR3WSTAYL0R"],
    ["2033"],
    ["BIKER", "EDGARALLANPOE"],
    ["YEHUDA"],
    ["ANDREW", "CECILIA"],
    ["GARBAGE", "SACK"],
    ["400"],
]

# with open("420_THE_GAME/APRIL20.dat") as f:
with open("/usr/share/dict/words") as f:
    wordlist = [a.upper() for a in f.read().split()]
# print(bla)

words = wordlist.copy()

for i, w in enumerate(wordlist):
    # print(i)
    # print(w)
    try:
        double = words[i] + words[i+1]
        words.append(double)
    except IndexError:
        pass
# with open("/usr/share/dict/words") as f:
#     words = list(set([a.upper() for a in f.read().split()]))
# print(words)

words = list(set(words))

print(len(words))

for i, _ in enumerate(bla):
    print(i)
    # for j, _ in enumerate(bla):
        # if i == j:
        #     continue
    copied = bla.copy()
    for w1 in words:
        # for w2 in words:
        copied[i] = [w1]
            # copied[j] = [w2]
        for out in itertools.product(*copied):
            # print(out)
            submit_answer(out, secret)


for i, _ in enumerate(bla):
    print(i)
    for j, _ in enumerate(bla):
        if i == j:
            continue
        copied = bla.copy()
        for w1 in words:
            for w2 in words:
                copied[i] = [w1]
                copied[j] = [w2]
                for out in itertools.product(*copied):
                    # print(out)
                    submit_answer(out, secret)
