from PIL import Image, ImageFilter, ImageChops, ImageOps, ImageEnhance

img = Image.open("nami.jpg")

#コントラストを強調
img = ImageEnhance.Contrast(img).enhance(2.0)

#線が抽出
gray1 = img.convert("L")
gray2 = gray1.filter(ImageFilter.MaxFilter(5))
line_img = ImageChops.difference(gray1, gray2)
line_img2 = ImageOps.invert(line_img)#反転

gray1.save("nami_gray1.jpg")
gray2.save("nami_gray2.jpg")
line_img.save("nami_line.jpg")
line_img2.save("nami_line2.jpg")
print("保存しました")