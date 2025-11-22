import FreeSimpleGUI as sg

layout = [[sg.Button(x*y,key=f"-btn{x}x{y}",size = (3,1)) for x in range(1,10)] for y in range(1,10)]

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