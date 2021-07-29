from pwn import xor

with open('strange_chunk.bin', 'rb') as f:
    file = f.read()

with open('china-girl-puzzle.png', 'rb') as f:
    key = f.read()

xored = xor(file, key[:len(file)])
with open(f'fileout.pdf', 'wb') as f:
    f.write(xored)
