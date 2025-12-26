import os
import FreeSimpleGUI as sg

#画像ファイルのパスを指定
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'paint.png')

#レイアウトを定義
layout = [
	[sg.Image(image_path)],
	[sg.Button('閉じる')]
]

#ウィンドウを作成
window = sg.Window("画像表示",layout=layout)

#イベントループ
while True:
	event,values = window.read()
	if event in (sg.WIN_CLOSED, "閉じる"):
		break
window.close()