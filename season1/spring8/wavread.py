import numpy as np
import wavio
import string

wav = wavio.read('message.wav')

print(wav)
out = []
prev = None
for i in range(4096):
    d = wav.data[i]
    print(f"Index: {i}")
    print(f"Data:  {d}")
    ind = d[0] - d[1]
    if prev is None:
        prev = ind
    else:
        byte = abs(prev) * 16 + abs(ind)
        byte = 255 - byte
        if byte >= 0 and byte < 256:
            out.append(int(byte))
        prev = None

print(out)
print(len(out))

xorkey = "crypt0r0de0"

with open('out.zip', 'wb') as f:
    f.write(bytearray(out))


