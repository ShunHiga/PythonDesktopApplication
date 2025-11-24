import FreeSimpleGUI as sg
import datetime


#時間を取得
def get_time_str():
	now = datetime.datetime.now()
	return now.strftime("%H:%M:%S")

layout = [[sg.Text(get_time_str(),
		  key='-output',
		  background_color="white",
		  text_color="black",
		  font=("Helvetica",80))], [sg.Button("時間の更新",key='-btn',font=("Helvetica",20))]]

window = sg.Window("手動時計", layout)

while True:
	#e,_ = window.read(timeout=10)
	e,_ = window.read()
	if e == sg.WINDOW_CLOSED: break
	now = datetime.datetime.now()
	window['-output'].update(now.strftime("%H:%M:%S"))
window.close()