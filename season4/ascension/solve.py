import string

num1 = "012345680124368001246385021468020124356701243571012435760123465701234568012463850123465802146802012436850124357601234657012436850124638001246385021468020124357"

num2 = "90124635802146802012345670123465702146802012468300124638501246357012468030124357602146802012468030123465702146802012468030214680201246830012468030124683001235467"

def chunks(l, n):
    """break up into groups of n
    >>> chunks("hello", 2)
    ['he', 'll', 'o']"""
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]


num3 = chunks(num1+num2, 8)

# print(num3)

phrase = "the monster inside of us began as a baby"

# print(len(num3))
# print(len(phrase))

trans = {}
for i, n in enumerate(num3):
    # trans[n] = phrase[i]
    if phrase[i] in trans and trans[phrase[i]] != n:
        print(f"Dup for {phrase[i]}: {trans[phrase[i]]}")
    trans[phrase[i]] = n

print(trans)

trans["k"] = "01243657"
trans["w"] = "01234579"



for a in string.ascii_lowercase:
    if a in trans:
        print(f"{a}    {trans[a]}     {str(bin(ord(a))).replace('0b', '0')}")


for i in "unknown":
    print(trans[i], end='')
