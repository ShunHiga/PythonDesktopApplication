from PIL import Image, ImageFilter

img = Image.open("nami.jpg")

img = img.filter(ImageFilter.GaussianBlur(radius=3))

img.save("nami_blur.jpg")
print("保存しました")