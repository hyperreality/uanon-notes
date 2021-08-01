cipher = """D<span class="b">r</span><span class="b">a</span>w<span class="b">i</span>n<span class="b">g</span> a <span class="b">b</span><span class="b">o</span>u<span class="b">n</span><span class="b">d</span>ary <span class="b">b</span>etw<span class="b">e</span>en p<span class="b">r</span><span class="b">i</span>vat<span class="b">e</span>*<span class="b">a</span>nd <span class="b">p</span><span class="b">u</span>blic, <span class="b">b</span>e<span class="b">t</span>wee<span class="b">n</span> an <span class="b">i</span>llicit b<span class="b">r</span>ibe a<span class="b">n</span>d <span class="b">l</span><span class="b">i</span>c<span class="b">i</span>t <span class="b">g</span><span class="b">i</span><span class="b">f</span>t i<span class="b">s</span>*<span class="b">h</span><span class="b">a</span>rd. <span class="b">G</span>ift giv<span class="b">i</span>ng <span class="b">w</span>as <span class="b">a</span>n int<span class="b">r</span><span class="b">i</span>n<span class="b">s</span>ic <span class="b">p</span>ar<span class="b">t</span> of s<span class="b">o</span><span class="b">c</span>ie<span class="b">t</span>y a<span class="b">n</span><span class="b">d</span>*<span class="b">c</span>omm<span class="b">o</span>n p<span class="b">r</span>actic<span class="b">e</span> among f<span class="b">r</span>i<span class="b">e</span>nd<span class="b">s</span>. <span class="b">D</span>o <span class="b">y</span>o<span class="b">u</span> tr<span class="b">u</span><span class="b">s</span>t <span class="b">y</span><span class="b">o</span>ur f<span class="b">r</span>iends?"""

out = ""

inspan = False
intags = False
for c in cipher:
    if c in "* .?,":
        continue
    if c == "<":
        intags = True
        inspan = True
        continue
    if c == "/":
        inspan = False
        continue
    if intags:
        if c == ">":
            intags = False
        continue

    if inspan:
        print(c, end="")
        out += "B"
    else:
        print(c, end="")
        out += "A"

print()
print(out)
# print(out.count("A"))
# print(out.count("B"))
