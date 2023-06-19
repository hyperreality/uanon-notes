
for i in range(1, 7):
    with open(f"image{i}.png", "rb") as f:
        data = f.read()

    print(data)

    end = bytes.fromhex("00000049454e44ae426082")

    trailer = data.split(end)

    with open(f"image{i}.enc", "wb") as f:
        f.write(trailer[1])
