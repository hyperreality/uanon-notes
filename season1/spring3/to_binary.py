import sys

with open(sys.argv[1]) as f:
    words = [a.strip() for a in f.readlines()]

for w in words:
    print(" ".join(f"{ord(i):08b}" for i in w))
    print("".join(f"{ord(i):08b}" for i in w))
