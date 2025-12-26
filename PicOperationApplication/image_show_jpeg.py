import os
import FreeSimpleGUI as sg
from PIL import Image
import io

#JPEG画像のパス
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "fuji.jpeg")

#JPEG画像をPNG形式に変換する
def convert_png(image_path, size=(600, 600)):
	img = Image.open(image_path)
	img.thumbnail(size=size)
	#png形式に変換
	png = io.BytesIO()
	img.save(png, format="PNG")
	return png.getvalue()

window = sg.Window(
	'JPEG画像の表示',
	layout=[
		[sg.Image(convert_png(image_path))],
		[sg.Button("閉じる")]
	]
)

#イベントループ
while True:
	event, values = window.read()
	if event in (sg.WIN_CLOSED, "閉じる"):
		break
window.close()

