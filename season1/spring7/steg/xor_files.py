from pwn import xor

with open('background.png', 'rb') as f:
    background = f.read()
with open('lights.png', 'rb') as f:
    lights = f.read()

bla = xor(background, lights)

with open('out', 'wb') as f:
    f.write(bla)

