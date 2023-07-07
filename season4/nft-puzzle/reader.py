import math
from PIL import Image, ImageDraw
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

image = Image.open("ascended.png")
# image = Image.open("common1.png")
w, h = image.size
im = image.load()

out = []

for i in range(0, 100):
    for j in range(0, 4):
      r,g,b,a = im[i, j]
      print(r,g,b,a)
      # print(chr(255-b), end="")
      # parities.append(g % 2)

