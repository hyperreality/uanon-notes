from Crypto.Util.number import *
import base64
from PIL import Image, ImageDraw

with open('bin_key.txt') as f:
    key = [len(a)-1 for a in f.readlines()]
print(key)

with open('base64s.txt') as f:
    bins = base64.b64decode(f.read()).decode()
# print(bins)

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]

rows = chunks(bins, 33)
# print(rows)

out = []
SKIP = 9

out[:SKIP] = rows[:SKIP].copy()

out2 = ""

for i, r in enumerate(rows[SKIP:]):
    pos1 = key[i]
    pos2 = key[i] + 1

    new_r = list(r)

    if new_r[pos1] == "1":
        new_r[pos1] = "0"
        out2 += "0"
    elif new_r[pos1] == "0":
        new_r[pos1] = "1"
        out2 += "1"

    if new_r[pos2] == "1":
        new_r[pos2] = "0"
        out2 += "0"
    elif new_r[pos2] == "0":
        new_r[pos2] = "1"
        out2 += "1"

    out.append("".join(new_r))
    # print("".join(out))


msg = out2.replace("0", "3").replace("1", "0").replace("3", "1")

def to_text(binary):
    return long_to_bytes(int(binary, 2))

print(to_text(msg))


def draw_qr(rows):
    im = Image.new('1', (33, 33), color=1)
    draw = ImageDraw.Draw(im)

    for y, row in enumerate(rows):
        for x, i in enumerate(row):
            if i == "1":
                draw.point((x, y), 0)

    im = im.resize((256,256),Image.ANTIALIAS)
    im.show()
    im.save("qr.png")

draw_qr(out)
