from Crypto.Util.number import *
import struct
from collections import Counter

with open('china-girl-puzzle.png', 'rb') as f:
    chinagirl = f.read()

header = chinagirl[:33]
first = chinagirl[33:33+65536+12]
# first = chinagirl[33:0xe00cd-4]
second = chinagirl[0xe00cd-4:0xe00cd+39962+8]
iwtf = chinagirl[0xe9cf3-4:].replace(b"iwTF", b"IDAT")
iwtf = b''
end = chinagirl[-12:]

# out = bytearray()
# for s in strange:
#     out.append(0xff - s)

out = header + first + second + iwtf + end

with open('out.png', 'wb') as f:
    f.write(out)

# print(strange[:4])
# print(strange[4:8])
# print(struct.unpack("I", strange[4:8]))


print(Counter(chinagirl).most_common())
