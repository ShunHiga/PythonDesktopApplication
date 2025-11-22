import FreeSimpleGUI as sg
#import TkEasyGUI as sg

#ラベルを配置したウィンドウを表示する
layout = [[sg.Text("怠け者は欲しがるが何も得ず、勤勉な人は十分に満たされる。")],
		  [sg.Button("OK")],
		  [sg.Button("No")],
		  [sg.Button("だめ")]]
window = sg.Window("格言", layout)

while True:
	event, values = window.read()
	print(event)
	#画面クローズした時の処理
	if event == sg.WINDOW_CLOSED:
		break
	#OKボタンをが押された時の処理
	if event == "OK":
		sg.popup("OKボタンが押されました")
		break
#終了処理
window.close()
