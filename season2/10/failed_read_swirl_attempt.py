import string
from PIL import Image
from Crypto.Util.number import *

image = Image.open("china-girl-puzzle.png")
w, h = image.size
im = image.load()

def traverse(img, x, y, edge_len, axis, direction):
    out = []
    last = edge_len - 1

    for i in range(edge_len):
        # print(x,y)
        if direction == "+" and axis == "x":
            x = x + 1
        elif direction == "-" and axis == "x":
            x = x - 1
        elif direction == "+" and axis == "y":
            y = y + 1
        elif direction == "-" and axis == "y":
            y = y - 1
        out.append(im[x, y])

    return out, x, y


def get_swirl(img, x, y, axis_order, dir_order, spiral_reduce):
    out = []

    spiral_reduce *= 2

    edge_len = 32 - (spiral_reduce // 2)
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("1")
    # print(edge)
    edge_len = 31 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("2")
    # print(edge)
    edge_len = 31 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("3")
    # print(edge)
    edge_len = 24 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("4")
    # print(edge)
    edge_len = 24 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("5")
    # print(edge)
    edge_len = 17 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("6")
    # print(edge)
    edge_len = 17 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("7")
    # print(edge)
    edge_len = 10 - spiral_reduce
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("8")
    # print(edge)
    edge_len = 10 - (spiral_reduce // 2)
    edge, x, y = traverse(img, x, y, edge_len, next(axis_order), next(dir_order))
    out.extend(edge)
    # print("9")
    # print(edge)
    # print(out)

    return out

swirls = []
top_swirls = []
right_swirls = []
bottom_swirls = []
left_swirls = []

spiral_reduce = 1

for i in range(44, 1069, 64):
    swirl = get_swirl(im, i, 12+spiral_reduce, iter("xyxyxyxyx"), iter("-++--++--"), spiral_reduce)
    top_swirls.append(swirl)

for i in range(108, 1069, 64):
    swirl = get_swirl(im, 1067-spiral_reduce, i, iter("yxyxyxyxy"), iter("--++--++-"), spiral_reduce)
    right_swirls.append(swirl)

for i in range(971, 10, -64):
    swirl = get_swirl(im, i, 1067-spiral_reduce, iter("xyxyxyxyx"), iter("+--++--++"), spiral_reduce)
    bottom_swirls.append(swirl)

for i in range(971, 74, -64):
    swirl = get_swirl(im, 12+spiral_reduce, i, iter("yxyxyxyxy"), iter("++--++--+"), spiral_reduce)
    left_swirls.append(swirl)

# print(len(top_swirls))
# print(len(right_swirls))
# print(len(bottom_swirls))
# print(len(left_swirls))
# print(left_swirls[-1])

swirls = top_swirls + right_swirls + bottom_swirls + left_swirls
assert len(swirls) == 64
pixels = len(swirls[0])
print(len(swirls[0]))
# assert len(swirls[0]) == pixels

print(top_swirls[0])

par = [0] * pixels
for s in swirls:
    for i in range(pixels):
        par[i] += s[i][0]
print(par)
for i in range(pixels):
    par[i] = par[i] % 2

print("".join([str(i) for i in par]))

# o1 = top_swirls[0]
# o2 = top_swirls[-1]

# for r in range(len(o1)):
#     if o1[r] != o2[r]:
#         print(f"{r}: {o1[r]} {o2[r]}")

print("Green Parities")
par = [0] * pixels
for i, s in enumerate(swirls):
    out = ""
    for j,p in enumerate(swirls[i]):
        out += str(p[2] % 2)
        par[j] += p[2]
        # print(p[0])
    print(f"{i:02}: {out}")

out = ""
for p in par:
    out += str(p % 2)
print(out)
