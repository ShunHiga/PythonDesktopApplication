import FreeSimpleGUI as sg

#ボタン定義
calc_buttons=[
	["C", "←","//","/"],
	["7","8","9","*"],
	["4","5","6","-"],
	["1","2","3","+"],
	["0",".","%","="],
]
layout = [
	[sg.Text("0",
		  key='-output',
		  background_color="white",
		  text_color="black",
		  expand_x=True)]
	]
output = "0"
for row in calc_buttons:
	buttons = []
	for ch in row:
		btn = sg.Button(ch, key =f"-btn{ch}",size=(3,1))
		buttons.append(btn)
	layout.append(buttons)
window = sg.Window("計算機",layout)
while True:
	event,_ = window.read()
	if event == sg.WINDOW_CLOSED: break
	
	if event.startswith("-btn"):
		ch = window[event].GetText()
		if output == "0" or output.startswith("E:"):
			output = ""
		#押されたボタンごとの処理
		if ch == "C":
			output = ""
		elif ch == "←":
			output = output[:-1]
		elif ch == "=":
			try:
				output = str(eval(output))
			except Exception as e:
				output = "E:" + str(e)
		else:
			#それ以外のキーはそのまま追加
			output += ch
		window["-output"].update(output)
window.close()
