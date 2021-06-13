from Crypto.Util.number import *

bins = "0 1 1 00 0 1101 1 1 0 00 10 10 0 1 0 0 001 1 00 1 1 10 1 001 00 00 0 1 1 0001"

out = ""
for i, c in enumerate(bins):
    if i == 0:
        continue
    if c != " ":
        if bins[i-1] == " ":
            out += "1"
        else:
            out += "0"

print(out)

print(long_to_bytes(int("0" + out, 2)))
