from hashlib import blake2b
import json
from struct import pack
from binascii import hexlify, unhexlify
from itertools import product
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
    return json.dumps([message], separators=(',', ':')).encode('utf8')

def generate_proof(message, depth=1):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    ans = magic_bytes + length + passphrase
    print(ans)
    return hash(ans, rounds=depth)

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
    words1 = 'google-10000-english-no-swears.txt'
    words2 = 'capitalised-english-words'
    wordlist1 = [w.strip().upper() for w in open(words2, 'r').readlines()]
    wordlist2 = [w.strip().upper() for w in open(words2, 'r').readlines()]
    num = 70529

    for g1 in tqdm(wordlist1):
        for g2 in wordlist2:
            guess = g1 + ' ' + g2 + ' ' + str(num)
            submit_answer(guess, secret, depth=depth)
            # guess = g2 + ' ' + g1 + ' ' + str(num)
            # submit_answer(guess, secret, depth=depth)

def print_proof(*message):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    print(magic_bytes + length + passphrase)

def generate(secret, wordlist, length=1, capitalize=False, upper=False, lower=False):
    total = len(wordlist) ** length
    print(total)
    for combination in product(wordlist, repeat=length):
        for startword in startwords:
            guess = ' '.join([startword, *combination])
            if capitalize:
                print_proof(guess.capitalize())
            if upper:
                print_proof(guess.upper())
            if lower:
                print_proof(guess.lower())
            if all(not flag for flag in [capitalize, upper, lower]):
                print_proof(guess)


# wordlist = [w.strip() for w in open('/usr/share/dict/words', 'r').readlines() if len(w.strip()) > 4]
# wordlist = [w.strip() for w in open('/usr/share/dict/words', 'r').readlines()]
# wordlist = [w.strip() for w in open('words.txt', 'r').readlines()]
# wordlist = [w.strip() for w in open('wordlist.txt', 'r').readlines()]

# secret = '71c5c7899b4f7d0e0492eaf214e8967a7bc570d931a67864143279ebcae77bf8' # twenty-five
# proof = generate_proof('twenty-five', depth=2)
# print(proof, secret)

# wordlist = ["BAD FEED"]

spring2 = "b8ae84dc9ba611054012013e647e5551c1a1e712016b6590ee5db836a0d7a347"
spring3 = "7e8389902114b8be3e5bbfebc6f73cd66fba7bb9667da31c3052711fd61f0add"
# spring4 = "95c7f953d050b7f758c773460f32867bad7036288c00afae8b8bca05515669cc"
# spring5 = "aec2598bae90c7fb37c30fb0e362903a6ffe1e3f1cb688ccfbf8806de2680396"
spring7 = "7a23b88f0443364a4d776962214f654f65075d08743d7b3812d7c0bd7e58c098"
spring8 = "87e402405c9c268532ba64e5130476237cfc1289e2e993d62c97f3b14febcbf0"

wordlist = ""

brute(spring8, wordlist, length=2, depth=2, upper=False, lower=False)

