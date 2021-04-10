from PIL import Image
image = Image.open("lights.png")
# image = Image.open("background.png")
w, h = image.size
im = image.load()

arr = []

out = []

for i in range(w):
    for j in range(h):
      # print(f"x,y:{i},{j}")
      r,g,b,a = im[i,j]
      # print(im[i,j])

      # im[i,j] = (
      #     r^im[(1599-i),j][0],
      #     g^im[(1599-i),j][1],
      #     b^im[(1599-i),j][2],
      #     a
      # )
      # out = g
      # if g == 0:
      #     out = 1
      # if g == 2:
      #     out = 1
      im[i,j] = (
          255 if (2^g) % 2 == 0 else 0,
          255 if (2^b) % 2 == 0 else 0,
          255 if (2^r) % 2 == 0 else 0,
          a,
      )
      # im[i,j] = (
      #     r^im[1599-i,1066-j][2],
      #     g^im[1599-i,1066-j][1],
      #     b^im[1599-i,1066-j][0],
      #     a,
      # )
      # im[i,j] = (
      #     r^b,
      #     g^b,
      #     r^g,
      #     a
      # )

      # lsb_r = 0 if (r & 1) else 1
      # lsb_b = b & 1
      # lsb_g = g & 1
      # print(lsb_b)
      # out.append(lsb_r ^ lsb_b ^ lsb_g)
      # if a != 255:
      #     print(f"x,y: {i,j}")
      #     print(im[i,j])

# print(out)
# print("".join([str(o) for o in out]))

image.save("out.png")

