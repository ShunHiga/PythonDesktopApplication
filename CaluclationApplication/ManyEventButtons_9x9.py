import FreeSimpleGUI as sg

layout = []
for y in range(1, 10):
	btns = []
	for x in range(1, 10):
		#ボタンを作成
		btn_label = x * y
		btn = sg.Button(
			f"{btn_label}",
			key = f"-btn{x}x{y}",
			size=(3,1))
		btns.append(btn)
	#レイアウトに追加
	layout.append(btns)

window = sg.Window("たくさんのボタン9*9",layout)
while True:
	event, _ = window.read()
	if event == sg.WINDOW_CLOSED: break
	#ボタンが押された時
	if event.startswith("-btn"):
		label = window[event].ButtonText
		#-数字のみ
		sg.popup('ボタン' + event[event.find("-btn") + 4:] +f'={label}が押されました')

window.close