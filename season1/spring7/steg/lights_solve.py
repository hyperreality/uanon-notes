from PIL import Image
image = Image.open("lights.png")
w, h = image.size
im = image.load()

image2 = Image.open("lights.png")
im2  = image2.load()

for i in range(w):
    for j in range(h):
      r,g,b,a = im[i,j]
      # print(f"x,y:{i},{j}: {im[i,j]}")

      if j < h - 4:
          b = im2[i,j+4][2]
      if i > 3 and j < h - 4:
          r = im2[i-3,j+4][0]

      im[i,j] = (
          r ^ b,
          r ^ g,
          b ^ g,
          a,
      )

image.save("out.png")

