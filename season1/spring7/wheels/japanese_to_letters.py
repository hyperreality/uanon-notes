import string

nums = [16, 24, 21, 3, 24, 5, 13, 3, 24, 9, 13, 5, 20, 14, 1, 24, 12, 20, 13, 12, 7, 10, 17, 16, 14, 24, 9, 14, 5, 3, 17, 15, 9, 24, 15, 13, 14, 16, 13, 24, 9, 14, 3, 10, 21, 23, 3, 14, 2, 14, 21, 24]

out = ""
seen = {}
cur = 0
for n in nums:
    if n not in seen:
        seen[n] = string.ascii_lowercase[cur]
        cur+=1
    out += seen[n]

print(out)
