import itertools
import string
import wordninja
from collections import Counter

# lm = wordninja.LanguageModel('greek.txt.gz')

def caesar(inp, amount):
    return [(i+amount) % 26 for i in inp]

def rotate(wheel, amount):
    return wheel[amount:] + wheel[:amount]


def flip(wheel):
    new = [wheel[0]]
    new.extend(wheel[1:][::-1])
    return new
    return wheel[::-1]

def ic(ctext):
    num = 0.0
    den = 0.0
    for val in Counter(ctext).values():
        i = val
        num += i * (i - 1)
        den += i
    if den == 0.0:
        return 0.0
    else:
        return num / (den * (den - 1))

def nums_to_letters(arr, alphabet=string.ascii_lowercase):
    return "".join([alphabet[n % len(alphabet)] for n in arr])

def letters_to_nums(arr, alphabet=string.ascii_lowercase):
    return [alphabet.index(n) % len(alphabet) for n in arr]

def all_shifts(inp):
    return [caesar(inp, i) for i in range(26)]

def print_stats(arr, label=None):
    if label:
        print(f"{label} Stats")
    print(f"Frequencies: {Counter(arr).most_common()}")
    print(f"Set: {sorted(set(arr))}")
    print(f"Set length: {len(set(arr))}")
    print()

def print_if_valid(candidate, level=21):
    splat = wordninja.split(candidate)
    if len(splat) < level:
        print(splat)

def print_if_good_ic(inp, threshold=0.05):
    if not ic(inp) < threshold:
        print(nums_to_letters(inp))


CHARS_SIZE = 52
DISK_SIZE = 26
top = "エオオアオイウアオイウイオウアオウオウウイウエエウオイウイアエエイオエウウエウオイウアウオオアウアウオオ" # katakana
bot = "いおいえおあええおおえああおいおうあえううあういおおおおあえうあおおあえおいえおおおえあいええおうおいお" # hiragana
assert len(top) == CHARS_SIZE and len(bot) == CHARS_SIZE
left = ["20", "13", "20", "19", "14", "25", "23", "11", "13", "1", "5", "21", "5", "9", "1", "16", "9", "9", "14", "8", "15", "18", "20", "9", "4", "0"]
right = ["10", "9", "23", "1", "17", "15", "7", "25", "2", "24", "14", "9", "6", "22", "25", "19", "1", "7", "9", "11", "8", "21", "3", "13", "25", "19"]
assert len(left) == DISK_SIZE and len(right) == DISK_SIZE
top_set = set(top)
bot_set = set(bot)
assert len(top_set) == 5 and len(bot_set) == 5
DIRECTIONS = "startnorthonleftclockwisethenrightgoesotherwayrepeat"
DIRECTIONS_INT = letters_to_nums("startnorthonleftclockwisethenrightgoesotherwayrepeat")


top_vowels = top.replace("エ","e").replace("オ", "o").replace("ア", "a").replace("イ", "i").replace("ウ","u")
bot_vowels = bot.replace("あ","a").replace("お", "o").replace("え", "e").replace("い", "i").replace("う","u")

left_int = [int(i) for i in left]
right_int = [int(i) for i in right]
print(f"Left wheel: {nums_to_letters(left_int)}")
print_stats(left_int, "Left wheel")
print(f"Right wheel: {nums_to_letters(right_int)}")
print_stats(right_int, "Right wheel")

print_stats(DIRECTIONS_INT, "Directions")

# start north on left clockwise then right goes other way repeat
left_transforms = [
    left_int,
    flip(left_int), # counter-clockwise
]
right_transforms = [
    flip(right_int),
    right_int, # clockwise
    rotate(flip(right_int), 13), # start from south
    rotate(right_int, 13), # clockwise, start from south
]

# combined = left_int + flip(right_int)
# top_nums = letters_to_nums(top_vowels)
# bot_nums = letters_to_nums(bot_vowels)
# out = []
# for i, c in enumerate(combined):
#     r = (c + top_nums[i]) % 26
#     r = (r + bot_nums[i]) % 26
#     out.append(r)
# print(nums_to_letters(out))

# mpeg index
# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
#         out = ""
#         for i in range(DISK_SIZE):
#             ind = left_wheel[i] + right_wheel[i]
#             out += DIRECTIONS[ind+2]
#             # print(ind)
#         print(out)

# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
#         out = []
#         for i, c in enumerate(combined):
#             r = (c + top_nums[i]) % 26
#             r = (r + bot_nums[i]) % 26
#             out.append(r)
#         print(nums_to_letters(out))

# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
#         combined = left_wheel
#         out = []
#         for i, c in enumerate(combined):
#             r = (c + top_nums[i])
#             r = (r + top_nums[i+26]) % 26
#             r = (r + bot_nums[i]) % 26
#             r = (r + bot_nums[i+26]) % 26
#             out.append(r)
#         print(nums_to_letters(out))

# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
#         combined = left_wheel
#         out = []
#         for i, c in enumerate(combined):
#             r = (c + top_nums[i])
#             r = (r + top_nums[i+26]) % 26
#             r = (r + bot_nums[i]) % 26
#             r = (r + bot_nums[i+26]) % 26
#             out.append(r)
#         print(nums_to_letters(out))

# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
# current_left = left_int
# current_right = right_int
# out = []
# out1 = []
# out2 = []
# for i in range(DISK_SIZE*2):
#     if i % 2 == 0:
#         c = current_left[0]
#     else:
#         c = current_right[0]
#     # print(c)
#     current_left = rotate(current_left, c)
#     current_right = rotate(current_right, -c)
#     out.append(current_left[0])
#     out.append(current_right[0])
#     out1.append(current_left[0])
#     out2.append(current_right[0])
# print(nums_to_letters(out))
# print(nums_to_letters(out1))
# print(nums_to_letters(out2))

# print(nums_to_letters(flip(right_int))[20])

# out = []
# current_left = left_int
# current_right = right_int
# for i in range(DISK_SIZE*2):
#     if i % 2 == 0:
#         c = current_left[0]
#         current_right = rotate(current_right, c)
#         out.append(current_right[0])
#     else:
#         c = current_right[0]
#         current_left = rotate(current_left, -c)
#         out.append(current_left[0])
# print(nums_to_letters(out))


# current_left = left_int
# current_right = right_int
# out = []
# out1 = []
# out2 = []
# for i in range(DISK_SIZE*2):
#     if i % 2 == 0:
#         c = current_left[0]
#         current_left = rotate(current_left, c)
#         out.append(current_left[0])
#     else:
#         c = current_right[0]
#         current_right = rotate(current_right, -c)
#         out.append(current_right[0])
#     # print(c)
#     # out1.append(current_left[0])
#     # out2.append(current_right[0])
# print(nums_to_letters(out))
# # print(nums_to_letters(out1))
# # print(nums_to_letters(out2))


# current_left = left_int
# current_right = right_int
# out = []
# for i in range(DISK_SIZE*2):
#     # if i % 2 == 0:
#         c = current_left[0]
#         current_left = rotate(current_left, DIRECTIONS_INT[i])
#         out.append(current_left[0])
#     # else:
#     #     c = current_right[0]
#     #     current_right = rotate(current_right, -DIRECTIONS_INT[i])
#     #     out.append(current_right[0])
#     # print(c)
#     # out1.append(current_left[0])
#     # out2.append(current_right[0])
# print(nums_to_letters(out))
# # print(nums_to_letters(out1))
# # print(nums_to_letters(out2))


# print(nums_to_letters(flip(right_int))[20])

# current_left = left_int
# current_right = right_int
# out = []
# out1 = []
# out2 = []
# for i in range(DISK_SIZE*2):
#     c = current_left[0]
#     current_left = rotate(current_left, DIRECTIONS_INT[i])
#     current_right = rotate(current_right, -DIRECTIONS_INT[i])
#     if c == 0:
#         break
#     out.append(current_left[0])
#     out.append(current_right[0])
#     out1.append(current_left[0])
#     out2.append(current_right[0])
# print(nums_to_letters(out))
# print(nums_to_letters(out1))
# print(nums_to_letters(out2))

current_left = left_int
current_right = right_int
out = []
out1 = []
out2 = []
for i in range(DISK_SIZE):
    l = current_left[0]
    r = current_right[0]
    if i % 2 == 0:
        c = l
    else:
        c = r
    current_left = rotate(current_left, c)
    current_right = rotate(current_right, -c)
    out.append(current_left[0])
    out.append(current_right[0])
    out1.append(current_left[0])
    out2.append(current_right[0])
print(nums_to_letters(out))
print(nums_to_letters(out1))
print(nums_to_letters(out2))

current_left = left_int
current_right = right_int
out = []
out1 = []
out2 = []
l = current_left[0]
r = current_right[13]
for i in range(DISK_SIZE):
    if i % 2 == 0:
        c = l
    else:
        c = r
    if i % 2 == 0:
        current_left = rotate(current_left, c)
    else:
        current_right = rotate(current_right, -c)
    l = current_left[0]
    r = current_right[13]
    out.append(current_left[0])
    out.append(current_right[13])
    out1.append(current_left[0])
    out2.append(current_right[13])
print(nums_to_letters(out))
print(nums_to_letters(out1))
print(nums_to_letters(out2))

# current_left = left_int
# current_right = flip(right_int)
# out1 = []
# out2 = []
# for i in range(DISK_SIZE):
#     l = current_left[i]
#     print(l)
#     if l == 0:
#         break
#     current_right = rotate(current_right, l)
#     out2.append(current_right[0])
# print(nums_to_letters(out2))

# import sys
# sys.exit(0)

# All possible ways that the two wheels could be interlaced
# interlacings = []
# for left_wheel in left_transforms:
#     for right_wheel in right_transforms:
#         left = True
#         out = []
#         for i in range(DISK_SIZE*2):
#             if left:
#                 out.append(left_wheel[i//2])
#                 left = False
#             else:
#                 out.append(right_wheel[i//2])
#                 left = True
#         interlacings.append(out)
# for n in [nums_to_letters(i) for i in interlacings]:
#     print(n)


# # Simple addition of wheels to japanese decoding
# for interlacing in interlacings:
#     res = [(interlacing[i] + DIRECTIONS_INT[i]) % 26 for i in range(CHARS_SIZE)]
#     shifted = [nums_to_letters(s) for s in all_shifts(res)]
#     # print(shifted)
#     # print_if_good_ic(res)
#     for r in shifted:
#         print(r)

# # Plus/minus alternation of wheels to japanese decoding
# for interlacing in interlacings:
#     res = []
#     for i in range(CHARS_SIZE):
#         if i % 2 == 0:
#             c = (interlacing[i] + DIRECTIONS_INT[i]) % 26
#         else:
#             c = (interlacing[i] - DIRECTIONS_INT[i]) % 26
#         res.append(c)
#     print(nums_to_letters(res))
    # print_if_good_ic(res)


# print("caesar of each wheel for murdock")
# for m in range(26):
#     for n in range(26):

#         left = True
#         out = ""
#         for i in range(DISK_SIZE*2):
#             if left:
#                 out += string.ascii_lowercase[caesar(left_int, m)[i//2]]
#                 left = False
#             else:
#                 out += string.ascii_lowercase[caesar(flip(right_int), n)[i//2]]
#                 left = True
#         print(out)

# Stage 1 shit below no longer relevant

# for top_perm in itertools.permutations(top_set, r=5):
#     for bot_perm in itertools.permutations(bot_set, r=5):
#         for rotation in range(DISK_SIZE):
#             left_rotated = rotate(left_int, rotation)
#             left_shifted = [(left_rotated[i] + top_perm.index(t)) for i, t in enumerate(top[:DISK_SIZE])]
#             left_shifted = [(left_shifted[i] + bot_perm.index(t)) for i, t in enumerate(bot[:DISK_SIZE])]
#             left_chars = "".join([string.ascii_lowercase[(n) % 26] for n in left_shifted])
#             print_if_valid(left_chars)

# print(rotate(left, 2))

# for top_perm in itertools.permutations(top_set, r=5):
#     for bot_perm in itertools.permutations(bot_set, r=5):
#         left_shifted = [(interlaced[i] + top_perm.index(t)) for i, t in enumerate(top)]
#         left_shifted = [(left_shifted[i] + bot_perm.index(t)) for i, t in enumerate(bot)]
#         left_chars = "".join([string.ascii_lowercase[(n) % 26] for n in left_shifted])
#         print_if_valid(left_chars)
# print(sol)
# print([string.ascii_lowercase[(n) % 26] for n in left_int])
# print([string.ascii_lowercase[(n) % 26] for n in flip(right_int)])

# print("LEFT")
seen = []
l_cur = left_int
r_cur = right_int
cur = 0
for i in range(DISK_SIZE):
    l_cur = rotate(l_cur, -cur)
    r_cur = rotate(r_cur, -cur)
    cur = l_cur[0]
    seen.append(cur)
    l_cur = rotate(l_cur, cur)
    r_cur = rotate(r_cur, cur)
    cur = r_cur[0]
    seen.append(cur)
print(seen)
print(nums_to_letters([a for a in caesar(seen, -1)]))

