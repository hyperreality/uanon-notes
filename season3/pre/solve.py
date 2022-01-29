lyrics = """My blood in the Kingdom
My blood  next the window
I tore my  leg off
You were whole and clean
I tore my  leg off
The air was clear and clean
My blood in the  Kingdom
We lied we  here we lay
I  just dropped a wish in your fountain
Closed the safe in the room of the Paalace
We don't need  a key, what is our secret?
Something we know only when we  C it"""

out = ""
for i, l in enumerate(lyrics):
    if l == " " and lyrics[i+1] == " ":
        out += "1"
    elif l == " ":
        out += "0"

print(out)
print(len(out))

skip = 8
out2 = [out[i:i+skip] for i in range(0, len(out), skip)]
print(out2)
print([int(i, 2) for i in out2])


