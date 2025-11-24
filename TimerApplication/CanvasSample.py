import FreeSimpleGUI as sg

layout = [[
	sg.Canvas(
		size = (400, 400),
		key = '-canvas-',
		background_color= "white"
	)]]

window = sg.Window("キャンバスのテスト", layout)
painted = False #描画したか判定

#イベントループ
while True:
	event,_ = window.read(timeout=10)
	if event == sg.WINDOW_CLOSED:
		break

	#描画する
	if not painted:
		painted = True
		#描画用のWidgetを取得
		widget = window["-canvas-"].Widget
		#長方形を描画
		widget.create_rectangle(10,10,300,300,fill = "yellow")
		#円を描画
		widget.create_oval(50,50,350,350, fill="blue")
		#線を描画
		widget.create_line(10,10,390,390,fill = "red",width = 5)

window.close()