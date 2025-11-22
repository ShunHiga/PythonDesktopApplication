import FreeSimpleGUI as sg

layout = [[]]
for no in range(1, 10):
	#ボタンを作成
	btn = sg.Button(f"{no}",size=(3,1))
	#レイアウトに追加
	layout[0].append(btn)

print(f"button:{btn}")
print(f"layout:{layout}")
window = sg.Window("たくさんのボタン",layout)
while True:
	e, _ = window.read()
	if e == sg.WINDOW_CLOSED: break

window.close