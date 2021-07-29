import morse_talk as mtalk

cipher = """
ihawgrokpihaokphcmjaonrf
xnyveucflecuwoeeonnbxskt
fogzpdrjqvtmnhmnkodsirck
ecklhwotoxlsfjozmsoloadr
mrieoimoouijmnewfudiiogt
tqethvhmtxkeqgaotamirgmg
tesrnyeteowldconjioauksk
hsjcialpeqcecuqabzdtapre
olsecpeymmonljiowaoildot
ctzanntemrizqpwikdgjplav
wtejrrhtoyyooxqxgsjssgmm
pdumaocarddagiovmdxfnbhv
omomtvbumcohtsspjdjordny
tgdqelbnoeofuahdgbahjinf
zntbwpcigbnonhuctecntnmt
gnskseebksmbsroinikrrrme
"""
# joined = cipher.replace(" ", "").replace("\n", "")

# darkbricks = [
#     [6, 16],
#     [],
#     [8],
#     [5],
# ]

# for i in range(24):
#     out = ""
#     for j in range(16):
#         out += cipher.split("\n")[j][i]
#     print(out)

out = ""

for line in cipher.split("\n"):
    print(mtalk.encode(line))
    out += mtalk.encode(line)


print(out)
print(out.replace(" ", ""))
print(out.replace(" ", "").count("."))
print(out.replace(" ", "").count("-"))

# out2 = ""

# for o in out:
#     if o == ".":
#         out2 += "0"
#     elif o == "-":
#         out2 += "1"

# print(out2)

