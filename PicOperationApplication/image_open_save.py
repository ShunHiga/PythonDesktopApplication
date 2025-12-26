from PIL import Image
img = Image.open("image.png")

img.thumbnail((300,300))
img = img.convert("RGB")#RGB形式に変換

img = img.convert("RGB")

img.save("image_thumb.jpg", format="JPEG")
print("保存しました")