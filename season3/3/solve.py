from Crypto.Util.number import *
import gmpy2
import json
from itertools import combinations

def encrypt(msg):
    size = 1024
    m = bytes_to_long(msg)
    p = randomPrime(size)
    q = randomPrime(size)
    n = p*q
    e = 3
    c = pow(m,e,n)
    return n, e, c

with open("emails.json") as f:
    emails = json.loads(f.read())

# print(emails)

one = "1611227220000"
two = "1611417060000"
three = "1613363340000"

for cur in [one, two, three]:
    N = [int(a["N"]) for a in emails["emails"][cur]]
    C = [int(a["C"]) for a in emails["emails"][cur]]

    combs = combinations([i for i in range(len(N))], 3)
    for c in combs:
        subN = [N[i] for i in c]
        subC = [C[i] for i in c]
        M = subN[0] * subN[1] * subN[2]
        b = [M // i for i in subN]
        bp = [inverse(x,y) for x,y in zip(b, subN)]
        M3L = [x*y*z for x,y,z in zip(subC, b, bp)]
        l = (M3L[0] + M3L[1] + M3L[2]) % M
        u, v = gmpy2.iroot(l, 3)
        if v==True:
            print(long_to_bytes(u).decode())
            break
