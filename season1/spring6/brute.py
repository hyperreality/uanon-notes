from hashlib import blake2b
import json
from struct import pack
from binascii import hexlify, unhexlify
from itertools import product, chain
from tqdm import tqdm
from types import GeneratorType

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
    # print(message, proof, secret)
    # print(proof, secret)
    if proof == secret:
        print(f'[FOUND]: {message}')
        exit()

startwords = ['the', 'be', 'a', 'see', 'my', 'dead']

def brute(secret, wordlist, length=1, capitalize=False, upper=False, lower=False, depth=2):
    total = len(wordlist) ** length
    for combination in tqdm(product(wordlist, repeat=length), total=total):
        for startword in startwords:
            guess = ' '.join([startword, *combination])
            # guess = ''.join([*combination])
            if capitalize:
                submit_answer(guess.capitalize(), secret, depth=depth)
            if upper:
                submit_answer(guess.upper(), secret, depth=depth)
            if lower:
                submit_answer(guess.lower(), secret, depth=depth)
            if all(not flag for flag in [capitalize, upper, lower]):
                submit_answer(guess, secret, depth=depth)

def print_proof(*message):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    print(magic_bytes + length + passphrase)

def generate(secret, wordlist, length=1, capitalize=False, upper=False, lower=False):
    total = len(wordlist) ** length
    print(total)
    for combination in product(wordlist, repeat=length):
        # for startword in startwords:
        guess = ''.join(['we', 'keep', 'it', *combination])
        if capitalize:
            print_proof(guess.capitalize())
        if upper:
            print_proof(guess.upper())
        if lower:
            print_proof(guess.lower())
        if all(not flag for flag in [capitalize, upper, lower]):
            print_proof(guess)


def to_binary(s):
    return " ".join(f"{ord(i):08b}" for i in s)


# wordlist = [w.strip() for w in open('/usr/share/dict/words', 'r').readlines() if len(w.strip()) > 4]
# wordlist = [w.strip() for w in open('./google-10000-english-no-swears.txt', 'r').readlines() if len(w.strip()) < 5]

# secret = '71c5c7899b4f7d0e0492eaf214e8967a7bc570d931a67864143279ebcae77bf8' # twenty-five
# proof = generate_proof('twenty-five', depth=2)
# print(proof, secret)

# Format: Each person, 1st input - Name: Capitalized, ex: Bob

# Format: Each person, 2nd input - Age: 2 digit integer, ex: 11

# Format: Each person, 3rd input - Favorite color: Hexadecimal number, uppercase, preceded by #, example #FFFFFF

# Format: Each person, 4th input - Percentage of crypto position invested in Tezos: Floating point number between 0 and 100, precision of exactly 5 decimals. Round numbers to the 5th decimal if needed. Examples, 12.345678 gets rounded to 12.34568, 3.5 gets extended to 3.50000

# Format: Each person, 5th input - Place of significance: Full capitalized English location name - doublecheck with Wikipedia article title. Example: Mariana Trench

def make_person(name, color, age, wallet, place):
    return [name.capitalize(), color.upper(), str(age), wallet, place]

def generate_wallet():
    for hh in range(24):
        for mm in range(60):
            for ss in range(60):
                for i in range(10):
                    mm = str(mm)
                    ss = str(ss)
                    yield f'{hh}.{mm.zfill(2)}{ss.zfill(2)}{i}'

def generate_color():
    for n in range(16777215):
        print()

secret = '50d2c731a22358cf28bd681f18cdddb3983f34884bf943fb13e7b0ae4b973337'

names = ['Arthur', 'Diana', 'Bill', 'Sophia']
colors = ['#A3C1AD', '#DA70D6', '#87CEEB', '#A3C1AD', '#FFFFFF', '#000000']
wallets = ['24.93857', '33.33333', '93.71681', '29.97925', '18.39570']
all_wallets = generate_wallet()
places = ['Ephesus', 'Mariana Trench', 'San Francisco', 'Golden Gate Bridge', 'Golden Gate', 'Big Ear', 'The Big Ear', 'Ohio State University Radio Observatory']

# people = [
#     {
#         'name': 'Tom',
#         'age': 51,
#         'color': '#80FFD4',
#         'wallet': [*wallets],
#         'place': 'Easter Island'
#     },
#     {
#         'name': 'Sophia',
#         'age': 34,
#         'color': '#A3C1AD',
#         'wallet': [*wallets],
#         'place': [*places]
#     },
#     {
#         'name': [*names],
#         'age': 37,
#         'color': [*colors],
#         'wallet': [*wallets],
#         'place': 'Big Ear'
#     },
#     {
#         'name': [*names],
#         'age': 24,
#         'color': [*colors],
#         'wallet': [*wallets],
#         'place': 'Mount Everest'
#     },
#     {
#         'name': [*names],
#         'age': 55,
#         'color': [*colors],
#         'wallet': [*wallets],
#         'place': [*places]
#     }
# ]


people = [
    {
        'name': 'Tom',
        'color': ['#7FFFD4'],
        'age': ['50', '51'],
        'wallet': ['16.07320', '17.39570'],
        'place': 'Easter Island'
    },
    {
        'name': 'Sophia',
        'color': '#A3C1AD',
        'age': 34,
        'wallet': ['93.71681', '0.93717'],
        'place': ['San Francisco', 'Golden Gate', 'Golden Gate Bridge']
    },
    {
        'name': 'Arthur',
        'color': '#DA70D6',
        'age': 37,
        'wallet': '33.33333',
        'place': ['Big Ear', 'The Big Ear', 'Ohio State University Radio Observatory']
    },
    {
        'name': 'Bill',
        'color': ['#000000', '#FFFFFF', '#060606', '#FF4500', '#FFBF00', '#FF2D00'],
        'age': 24,
        'wallet': ['24.93857', '24.93858'],
        'place': 'Mount Everest'
    },
    {
        'name': 'Diana',
        'color': ['#87CEEB', '#8A2BE2'],
        'age': 55,
        'wallet': '29.97925',
        'place': 'Ephesus'
    }
]

def iterate_attribute(person, attribute):
    field = person[attribute]
    if isinstance(field, list):
        for inner in field:
            yield inner
    else:
        yield field

def iterate_person(person):
    name = iterate_attribute(person, 'name')
    color = iterate_attribute(person, 'color')
    age = iterate_attribute(person, 'age')
    wallet = iterate_attribute(person, 'wallet')
    place = iterate_attribute(person, 'place')
    for option in product(name, color, age, wallet, place):
        yield make_person(*option)

for person1 in iterate_person(people[0]):
    for person2 in iterate_person(people[1]):
        for person3 in iterate_person(people[2]):
            for person4 in iterate_person(people[3]):
                for person5 in iterate_person(people[4]):
                    guess = [*person1, *person2, *person3, *person4, *person5]
                    proof = generate_proof(guess, depth=1001)
                    print(guess)
                    if proof == secret:
                        print('FOUND: ', guess)
                        exit()

    # guess = [*person1]
    # print(guess)
    # prf = generate_proof(["Tom", "51"], depth=2)
    # print(prf)
    

# for option in product(iterate_person(people[0]), iterate_person(people[1]), iterate_person(people[2]), iterate_person(people[3]), iterate_person(people[4])):
#     guess = list(chain.from_iterable(option))
#     print(guess)
                


# Arthur -> #DA70D6


# brute('50d2c731a22358cf28bd681f18cdddb3983f34884bf943fb13e7b0ae4b973337', wordlist, length=1, depth=2, lower=True)
