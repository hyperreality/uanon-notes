
out = b""
base64 = b""
for i in range(1, 7):
    with open(f"image{i}.dec", "rb") as f:
        data = f.read()

    chunk = data[29:0x117]
    base64 += chunk

    chunk = data[0x130:]
    out += chunk

with open(f"image_combined.jpg", "wb") as f:
    f.write(out)

with open(f"b64_combined.txt", "wb") as f:
    f.write(base64)
