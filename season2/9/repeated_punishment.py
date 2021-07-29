from z3 import *

def CheckKeyLen(ciphertexts, keylen):
    ciphertexts = [ciphertext.replace(" ", "") for ciphertext in ciphertexts]

    solver = Solver()

    k = [Int("k%d" % i) for i in range(keylen)]
    for kc in k:
        solver.add(kc >= 0)
        solver.add(kc < 26)

    p = [Int("p%d" % i) for i in range(len(ciphertexts[0]))]
    for pc in p:
        solver.add(pc >= 0)
        solver.add(pc < 26)

    key_index = 0
    for ciphertext in ciphertexts:
        for c_index, c_letter in enumerate(ciphertext):
            c = ord(c_letter) - ord('A')
            solver.add((p[c_index] + k[key_index]) % 26 == c)
            key_index = (key_index + 1) % keylen

    result = solver.check()
    if result == unsat:
        return (None, None)
    else:
        m = solver.model()
        key = "".join([chr(m.evaluate(kc).as_long() + ord('A')) for kc in k])
        plaintext = "".join([chr(m.evaluate(pc).as_long() + ord('A')) for pc in p])
        return (key, plaintext)

def PrintRotatedKeyAndPlaintext(key, plaintext):
    def Rotate(s, offset):
        return "".join([chr((ord(c) - ord('A') + offset) % 26 + ord('A')) for c in s])
    for offset in range(26):
        print(Rotate(key, offset), Rotate(plaintext, (26 - offset) % 26))

def Decipher(ciphertexts):
    for keylen in range(1, 30):
        print("Testing key length", keylen)
        key, plaintext = CheckKeyLen(ciphertexts, keylen)
        if key:
            PrintRotatedKeyAndPlaintext(key, plaintext)
            return

if __name__ == "__main__":
    ciphertexts = [
        "ncwvbgprdgtabbdlvpzeljwizdy",
        "lydsrvvjsddxaqnkwcjjowyixdm",
    ]
    Decipher(ciphertexts)
