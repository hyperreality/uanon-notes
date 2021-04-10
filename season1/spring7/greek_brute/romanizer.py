from romanize import romanize
import sys

with open(sys.argv[1]) as f:
    words = [a.strip() for a in f.readlines()]

for w in words:
    print(romanize(w).upper())
