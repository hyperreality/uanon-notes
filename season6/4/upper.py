with open("/usr/share/wordlists/entities3.txt") as f:
    bla = f.readlines()

for b in bla:
    print(b.upper().replace(" ", ""))
