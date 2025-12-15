import FreeSimpleGUI as sg
import csv

#CSVファイルを読み込む
with open("fruits.csv", "r", encoding="utf-8") as fp:
	reader = csv.reader(fp)
	data = [row for row in reader]

#レイアウト定義
layout = [
	[sg.Table(
		values=data[1:], #テーブルに表示するデータを指定
		headings = data[0],#ヘッダをしてい
		expand_x=True,
		expand_y=True,
		justification='center',#セルを中央揃えにする
		auto_size_columns = True,
		max_col_width=30,
		font=("Arial", 14))]
]

#ウィンドウを作成
windows = sg.Window("CSVビュワー", layout,size=(500,300),resizable=True,finalize=True)

#イベントループ
while True:
	event, values = windows.read()
	if event == sg.WIN_CLOSED:
		break

windows.close()