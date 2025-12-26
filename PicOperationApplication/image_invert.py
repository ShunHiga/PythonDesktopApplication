from PIL import Image, ImageOps

img = Image.open("nami.jpg")

img = ImageOps.invert(img)

img.save("nami_invert.jpg")
print("保存しました")