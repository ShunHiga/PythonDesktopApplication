import FreeSimpleGUI as sg
#import TkEasyGUI as sg
import os
from datetime import datetime

#保存ファイル名を指定
DAY = datetime.now().strftime("%Y-%m-%d")
#DAY = datetime.now()
SCRIPT_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(SCRIPT_DIR, f"notepad-save-data-{DAY}.txt")
print(SAVE_FILE)
layout = [
	[sg.Multiline(size=(40,15), key="text")],
	[sg.Button("保存"), sg.Button("開く")],
]

window = sg.Window("メモ帳", layout=layout)

#イベントループ
while True:
	event, value = window.read()
	#画面を閉じた時
	if event == sg.WINDOW_CLOSED:
		break
	#保存ボタンを押した時
	if event == "保存":
		#ファイルに保存
		with open(SAVE_FILE, "w",encoding="utf-8") as f:
			f.write(value["text"])
			sg.popup("保存しました")
	if event == "開く":
		if not os.path.exists(SAVE_FILE):
			sg.popup("一度も保存されていません")
			continue
		#保存されたファイルを読み込む
		with open(SAVE_FILE, "r", encoding="utf-8") as f:
			text = f.read()
		#テキストボックスに反映
			window["text"].update(text)
#終了処理
window.close()