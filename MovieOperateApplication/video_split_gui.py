import FreeSimpleGUI as sg
import video_split

#ウィンドウを表示する関数
def show_window():
	options = [
		[
			sg.Text("無音最小長(ミリ秒)"),
			sg.InputText('500', key='min_silence_len'),
		],
		[
			sg.Text("無音のしきい値(dB)"),
			sg.InputText('-60', key='silence_thresh')
		]
	]

	layout = [
		[sg.Text('対象となる動画ファイルを選択してください')],
		[
			sg.InputText(key = "infile", enable_events=True),
			sg.FileBrowse()
		],
		[sg.Text("保存先フォルダーを選択シエtください")],
		[sg.InputText(key="outpath"), sg.FolderBrowse()],
		[sg.Frame("無音認識オプション", options)],
		[sg.Button("実行")]
	]
	win = sg.Window("無音で動画分割ツール", layout=layout)

	while True:
		event, values = win.read()
		if event == sg.WIN_CLOSED:
			break

		if event == "実行":
			video_path = values['infile']
			output_path = values['outpath']
			if output_path =="":
				sg.popup("保存先を指定してください")
				continue
			#オプションを指定して動画分割実行
			video_split.min_silence_len = int(values["min_silence_len"])
			video_split.silence_thresh = int(values["silence_thresh"])
			video_split.split_video(video_path, output_path)
			sg.popup("実行完了しました")
		
		if event == 'infile':
			#入力ファイルから出力ファイルを自動設定
			video_path = values['infile']
			output_path = video_path.replace('.mp4', "") + "_parts"
			win['outpath'].update(output_path)
	win.close()

if __name__ == "__main__":
	show_window()