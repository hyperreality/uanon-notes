from pwn import xor

with open('1_img.jpg', 'rb') as f:
    img1 = f.read()

with open('2_img.jpg', 'rb') as f:
    img2 = f.read()

with open('4_img.jpg', 'rb') as f:
    img4 = f.read()

xored = xor(img1, img2, img4)
with open(f'1_img.dexored.jpg', 'wb') as f:
    f.write(xored)
