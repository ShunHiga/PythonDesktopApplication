import pyperclip
import FreeSimpleGUI as sg
import os
import json


#クリップボードの履歴を保存するファイルパス
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(ROOT_DIR, 'clipboard-history.json')
#保存する履歴の最大数
MAX_HISTORY = 20

#既存の履歴を読み込む
history = []
if os.path.exists(SAVE_FILE):
	with open(SAVE_FILE, "r", encoding="utf-8") as f:
		history = json.load(f)

#履歴を保存する
def save_history():
	with open(SAVE_FILE, "w", encoding="utf-8") as f:
		json.dump(history, f, ensure_ascii=False, indent = 2)

#履歴を整形する
def list_format(history):
	crlf = lambda v: v.strip().replace("\r","").replace("\n","GGG")
	short = lambda v: v[:20] + "..." if len(v) > 20 else v
	return[f"{i + 1:02}: {crlf(short(h))}" for i, h in enumerate(history)]
#レイアウトを指定
layout = [
	[sg.Txt("履歴を選んで「コピー」ボタンをクリックしてください。")],
	[sg.Listbox(#クリップボードの履歴
		values=list_format(history),
		size=(40, 15),
		font=("Arial", 14),
		key="-history-")],
	[
		#各種ボタン
		sg.Button("コピー"), sg.Button("削除") ,sg.Button("終了")
	]
]

#ウィンドウを作成する
window = sg.Window("クリップボード履歴管理",layout)

while True:
	event, values = window.read(timeout=100)
	#values, event = window.read(timeout=100)
	
	if event in [sg.WIN_CLOSED, "終了"]:
		break
	#コピーボタンを押した時
	if event == "コピー":
		#選択された履歴をクリップボードにコピー
		if not values["-history-"]:
			continue
		else:
			sel_text = values["-history-"][0]
			index = int(sel_text[0:2])
			text = history[index - 1]
			pyperclip.copy(text)
			sg.popup("クリップボードにコピーしました")
	#削除ボタンを押したら履歴を削除
	if event == "削除":
		#選択された履歴インデックスを取得
		print(f"value:{values["-history-"]}")
		if not values["-history-"]:
			continue
		else:
			sel_text = values["-history-"][0]
			#実際のデータを取り出す
			index = int(sel_text[0:2])
			del history[index - 1]
			window["-history-"].update(list_format(history))
			save_history()
			pyperclip.copy("") #重複登録しないようにクリア
			sg.popup("削除しました")
	#定期的にクリップボードの内容をチェック
	text = pyperclip.paste()
	if text == "":
		continue #空なら何もしない

	if text not in history:
		history.insert(0, text)
		if len(history) > MAX_HISTORY:
			history.pop()
		#リストボックスを更新
		window["-history-"].update(list_format(history))
		save_history()
		continue
	#履歴の順番を入れ替え
	index = history.index(text)
	if index > 0:
		del history[index]
		history.insert(0, text)
		window["-history-"].update(list_format(history))
		save_history()

window.close()