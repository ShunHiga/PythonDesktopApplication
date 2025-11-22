import FreeSimpleGUI as sg

layout = [[]]
for no in range(1, 10):
	#ボタンを作成
	nom = no * 2
	btn = sg.Button(
		f"{no}",
		key = f"-btn{nom}",
		size=(3,1))
	#レイアウトに追加
	layout[0].append(btn)

window = sg.Window("たくさんのボタン",layout)
while True:
	e, _ = window.read()
	if e == sg.WINDOW_CLOSED: break
	#ボタンが押された時
	if e.startswith("-btn"):
		#-数字のみ
		sg.popup('ボタン' + e[e.find("-btn") + 4:] + 'が押されました')

window.close