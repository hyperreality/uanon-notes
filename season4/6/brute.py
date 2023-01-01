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

secret = "823f5c2958976069579ee41ec4f9d4a9ffc1937690ce4ba62fda93578cb89a6a"

bla = [
    ["cult from the same sloth"],
    ["dark side of the groom", "dank side of the groom", "dark brew of the groom", "dark hyde of the groom"],
    ["one time dad"],
    ["gas lightening", "gas laughlines", "gas delighting"],
    ["sow on and sow fourth"],
    [
        # "row row row your boat drowning in a dream",
        #  "row row row your boat drowning as i dream",
        # "row row row your boat dreaming as i drown",
        "row row row your boat lifeboat in a dream",
        "row row row your boat lifeboat is a dream",
    ],
    ["rome is where the art is"],
    ["the body police tick"],
]

lengths = [ 24, 22, 12, 14, 21, 41, 24, 20 ]

# gas = []
# with open('/usr/share/dict/words') as f:
#     words = [a.strip() for a in f.readlines()]
# for a in words:
#     if len(a) == 5:
#         gas.append("gas light{a}")
#     if len(a) == 10:
#         gas.append("gas {a}")
# bla[3] = gas

for out in itertools.product(*bla):
    # out = sorted(out)
    submit_answer(out, secret)

# for i, b in enumerate(bla):
#     print(i)
#     assert len(b) == lengths[i]



# with open('/usr/share/wordlists/entities.txt') as f:
#     words = [a.strip() for a in f.readlines()]

# for a in words:
#     if len(a) == 10:
#         bla[3] = "gas {a}"
#         submit_answer(bla, secret)
# # for a in words:
# #     if len(a) == 4:
# #         bla[1] = "{a} side of the groom"
# #         bla[1] = "dark {a} of the groom"
#     # for w in words:
#     #     if len(w) == 7:
#     #         four = f"the gas{w}"

#     #         bla[3] = four
#     #         submit_answer(bla, secret)
#     #     if len(w) == 10:
#     #         four = f"gas {w}"

#     #         bla[3] = four
#             # submit_answer(bla, secret)


# four = "gas laughlines"
# bla[3] = four
# submit_answer(bla, secret)
