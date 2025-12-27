import FreeSimpleGUI as sg
import subprocess

#FFmpegのパスを指定
FFMPEG_PATH = "ffmpeg"

#GUI画面を表示する関数を定義
def show_gui():
	#GUIレイアウトを定義
	layout = [
		[sg.Text("入力：動画ファイルの指定")],
		[
			#テキストが変更されたときにイベントが発生するようにする
			sg.Input(key="infile", enable_events=True),
			sg.FileBrowse()
		],
		[sg.Text("出力：音声ファイルの指定")],
		[sg.Input(key="outfile"), sg.FileSaveAs()],
		[sg.Button("実行"),sg.Button("終了")]
	]
	win = sg.Window("動画から音声を抽出する", layout)

	#イベントループ
	while True:
		event, values = win.read()
		if event in (sg.WIN_CLOSED, "終了"):
			break

		if event == "infile":
			#入力ファイルが指定されたら出力ファイル名を設定
			if values["infile"]:
				f = values["infile"].replace(".mp4", "") + ".mp3"
				win["outfile"].update(f)
		if event == "実行":
			#MP3の抽出を実行
			extract_mp3(values["infile"], values["outfile"])
			sg.popup("処理が完了しました")
	win.close()

def extract_mp3(input_file, output_file):
	subprocess.run([
		FFMPEG_PATH, "-y", "-i", input_file,
		"-vn", "-acodec", "libmp3lame", "-ab", "320k",
		output_file
	])

if __name__ == "__main__":
	show_gui()