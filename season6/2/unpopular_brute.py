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
    return json.dumps(message, separators=(',', ':')).encode('utf-8')

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

def print_proof(*message):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    print(magic_bytes + length + passphrase)


secret = "775bed9daae4e50c8af1b6b93b98f0e0725a5ad6636aa30a4b3e508fe0254945"

with open("all_lore.txt") as f:
    wordlist = f.read().upper().replace("\n", " ").split()

words = []

for i, w in enumerate(wordlist):
    try:
        words.append(w)
        words.append(w + wordlist[i+1])
        words.append(w + wordlist[i+1] + wordlist[i+2])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9] + wordlist[i+10] + wordlist[i+11])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9] + wordlist[i+10] + wordlist[i+11] + wordlist[i+12])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9] + wordlist[i+10] + wordlist[i+11] + wordlist[i+12] + wordlist[i+13])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9] + wordlist[i+10] + wordlist[i+11] + wordlist[i+12] + wordlist[i+13] + wordlist[i+14] + wordlist[i+15])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6] + wordlist[i+7] + wordlist[i+8] + wordlist[i+9] + wordlist[i+10] + wordlist[i+11] + wordlist[i+12] + wordlist[i+13] + wordlist[i+14] + wordlist[i+15] + wordlist[i+16])
    except:
        pass

modded = ["".join(filter(str.isalnum, w)) for w in words]
words.extend(modded)

# print(words)

# words = []

# import string
# for i in itertools.product(string.ascii_uppercase, repeat=6):
#     w = "".join(i)
#     submit_answer(w, secret)

# secret = "9c9dba32b632a6f79d5e467fcfc6a5b8be03845830b0bb929502b8957cc549c1"
# words.append("ONLYTHETRUTHWILLFORGETWEAREKNOTFREED")

# for w in words:
#     # print(w)
#     submit_answer(w, secret)


import string
w = None
bla = len("UNPOPULAR")
alpha = string.digits + string.ascii_uppercase + string.punctuation
for i in range(bla):
    print(w)
    for j in range(bla):
        if i == j:
            break
        for k in range(bla):
            if k == j:
                break
            for l in alpha:
                for m in alpha:
                    for n in alpha:
                        word = list("UNPOPULAR")
                        # word.insert(i, l)
                        # word.insert(j, m)
                        word[i] = l
                        word[j] = m
                        word[k] = n
                        w = "".join(word)
                        # print(w)
                        submit_answer(w, secret)
