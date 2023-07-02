from Crypto.Util.number import *

a = """The room is filled with weapons.
Approaching one, shaped like a gun,
On closer inspection you find it's
just harmless words:

de
at thlifedeathlifedeathlife.isGRandW E
_th|ifedea 3,thlifedeathl7if;ed,ea,th,li,f2edeathlife==death/
|lifedeaths\ ;65;65; ; ;7\li,fe\de,athli0--fe,d.\ *$& ((
`lifedeaths|de,73/63,ath__/ 6)=))~(( '-\ F72 \\
\ DEATH\ \\~~\\ \ 65 \\
`| IS= | ))~~\\ '''"" "=,))
|LIFE | |DEATH)
/ LIE / `WOUND'"""

nums = "6"
nums += "".join([b for b in a if b in "0123456789F"])
nums += "7"

print(nums)
print(bytes.fromhex(nums))

morse = [b for b in a if b in ".-"]
print("".join(morse))
