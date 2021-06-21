text = """A.container{width: 100%;height: 100%; } iframe{min-width: 100vw; min-height:100vh; margin: 0; padding:0; overflow-x:hidden;}body, html {overflow-x:hidden; margin:0; padding:0; } div{position:relative; display:block;white-space: normal; border:0; background-color:#fedece;zoom: 1;} .container {margin: auto; white-space: inherit;backface-visibility:inherit;border: 0;padding-left:0;padding-right:0;padding-top:0;padding-bottom: 0; cursor: inherit;border-radius:0; -webkit-border-radius:0; -moz-border-border-radius: 0;background-clip:padding-box; -webkit-background-clip:padding-box;-moz-background-clip:padding-box; width: auto;height:auto; float: unset; clear:both;font-family: algerian, courier,monospace,Arial, Helvetica, sans-serif,Impact; font-size: 1.5em; font-weight:bold; border-spacing:0; border-collapse:collapse;text-align: left; color:#000;} div, .default{ margin: auto; padding:0; white-space: nowrap;color:#000000; background-color: gray;font-size:1.5rem; border-radius:0;}X"""

bins = ["0110"]
buf = [""]

def append(bit, i):
    bins[-1] += bit

    if len(bins[-1]) == 8:
        bins.append("")
        buf.append("")

for i,v in enumerate(text):
    if i == 0:
        continue
    if text[i] == "." or text[i] == "{":
        if text[i-1] == " ":
            append("1", i)
        else:
            append("0" ,i)
    if text[i] == "{" or text[i] == "}" or text[i] == ":" or text[i] == ";" or text[i] == ",":
        if text[i+1] == " ":
            append("1", i)
        else:
            append("0", i)
    buf[-1] += v

print("".join(bins))
#print(buf)


for i, v in enumerate(bins):
    char = chr(int(bins[i], 2))
    print(f"{bins[i]} { char:2} {buf[i]}")
