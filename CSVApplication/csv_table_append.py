import FreeSimpleGUI as sg
import os
import csv

def main():
	while True:
		#CSVファイルを選ぶ
		files = sg.popup_get_file(
			"複数のCSVファイルを選択",
			multiple_files= True,
			no_window= True,
		)
	
		if len(files) == 0 or files == "":
			break
		#複数のCSVファイルをまとめる
		all_data = []
		for filename in files:
			data = read_csv(filename)
			if data is None:
				sg.popup_error(filename + "が読み込めません。")
				continue
			#もしヘッダーが行が同じなら省略する
			if len(all_data) >= 2 and len(data) >= 2:
				if all_data[0] == data[0]:
					data = data[1:]
			all_data += data
		#結合したデータをテーブルに表示する
		if show_csv(all_data) == False:
			break

#CSVファイルを読み込む
def read_csv(filename):
	encodings = ["UTF-8", "CP932", "EUC-JP"]
	for enc in encodings:
		try:
			with open(filename, "r", encoding=enc) as f:
				reader = csv.reader(f)
				data = [row for row in reader]
			return data
		except:
			pass
	return None

#c CSVをテーブルに表示する
def show_csv(data):
	if len(data) == 0:
		data =[["空"],["空"]]
	#レイアウトを定義
	layout = [
		[sg.Table(
			key="-table-",
			values=data[1:],
			headings=data[0],
			expand_x=True,expand_y=True,
			justification='left',
			auto_size_columns=True,
			max_col_width=30,
			font=("Arial",14)
		)],
		[sg.Button('ファイル選択'),sg.Button('保存'),sg.Button('終了')]
	]
	#ウィンドウを作成
	window = sg.Window("CSVビュワー",layout,size=(500,300),resizable=True,finalize=True)

	#イベントループ
	flag_continue = False
	while True:
		event,_=window.read()
		if event in [sg.WIN_CLOSED, "終了"]:
			break
		#ファイル追加ボタンを押した時
		if event == "ファイル選択":
			flag_continue = True
			break
		
		if event == "保存":
			filename = sg.popup_get_file(
				"保存するCSVファイルを選択",
				save_as= True,
				no_window=True
			)
			if filename == "" or filename is None:
				continue
			with open(filename,"w", encoding="utf-8") as f:
				writer =csv.writer(f)
				writer.writerow(data)
	window.close()
	return flag_continue

if __name__ == "__main__":
	main()