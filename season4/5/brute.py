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

a = ["Isaiah", "Kid", "Kid Catholic", "François Legault", "Dad"]
b = ["Jesus", "God", "Jesus H Christ", "Jesus H. Christ", "Catholicism", "Death", "DEATH!", "An Angel", "Angel", "The Devil", "Mother Earth", "racism"]
c = ["blood", "death", "Death", "DEATH!", "Nothing", "Zero", "nothing", "racism", "https://www.cbc.ca/player/play/1656126019944", "All French Canadians are Catholic"]

with open('poem.txt') as f:
    poem = f.read()

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]

words = poem.split()
# print(words)
c += words

import string
def depunc(word):
    for s in string.punctuation:
        word = word.rstrip(s)
    return word

out = []
for i, w in enumerate(words):
    try:
        out.append(" ".join([depunc(a) for a in [w, words[i+1]]]))
        # out.append(" ".join([depunc(a) for a in [w, words[i+1], words[i+2].rstrip(".").rstrip(",")]]))
        # out.append(" ".join([depunc(a) for a in [w, words[i+1], words[i+2], words[i+3], words[i+4].rstrip(".").rstrip(",")]]))
        # out.append(" ".join([depunc(a) for a in [w, words[i+1], words[i+2], words[i+3], words[i+4], words[i+5].rstrip(".").rstrip(",")]]))
        # out.append(" ".join([depunc(a) for a in [w, words[i+1], words[i+2], words[i+3], words[i+4], words[i+5], words[i+6].rstrip(".").rstrip(",")]]))
        # out.append(" ".join([depunc(a) for a in [w, words[i+1], words[i+2], words[i+3], words[i+4], words[i+5], words[i+6], words[i+7], words[i+8].rstrip(".").rstrip(",")]]))
    except:
        pass

# print(out)

c += out
# print(c)

# with open('/usr/share/wordlists/entities.txt') as f:
#     entities = [a.replace("_", " ").rstrip() for a in f.readlines()]

c = ["Mother Earth", "his beautiful lips mouth", "Him on the soap box", "Cambodia", "mother earth", "Mother earth", "Eternity", "O", "0", "eternity", "(1+1/1·1-1/1·2+1/2·3 / ø3=2ø+1=F3ø+F2 )"]
c = ["proper nouns", "nouns", "speech", "objects", "Nouns", "Speech", "Objects", "Language", "language", "words", "Words", "strange loops", "beyond the pale"]

nouns = a + b

bla = [
    a,
    b,
    c,
    # entities,
]

secret = "e3fe66cd3948f293ef77c16e3df4b36bad7a5d06404e175d18c44bbbb63a7ed1"


for out in tqdm(itertools.product(*bla)):
    submit_answer(out, secret)
