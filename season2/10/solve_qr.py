import math
from PIL import Image, ImageDraw

image = Image.open("china-girl-puzzle.png")
w, h = image.size
im = image.load()

out = []

for j in range(12, h-12, 32):
    for i in range(12, w-12, 32):
      parities = []

      for n in range(0,32):
          for m in range(0,32):
              r,g,b = im[i+m, j+n]
              parities.append(g % 2)

      out.append(parities.count(1) % 2)

print(len(out))
print("".join(str(i) for i in out))

def draw_qr(binary):
    width = math.sqrt(len(binary))
    assert width == int(width), "Number of bits not square"
    width = int(width)
    height = width

    im = Image.new('1', (width, height), color=1)
    draw = ImageDraw.Draw(im)

    for y in range(height):
        for x in range(width):
            bit = binary[y * height + x]
            draw.point((x, y), bit)
    im.save("qr.png")

draw_qr(out)

