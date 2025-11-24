import FreeSimpleGUI as sg
import datetime
import pygame as pg

#音声再生の準備
pg.mixer.init()
#再生ファイルの読み込み
pg.mixer.music.load("beep.mp3")

TIMER_SEC = 20
#時間を取得
def get_time_str():
	now = datetime.datetime.now()
	return now.strftime("%H:%M:%S")

layout = [[sg.Text("00:00:00",
		  key='-output',
		  background_color="white",
		  text_color="black",
		  font=("Helvetica",80))], 
		  [sg.Button("Start",key='-btn_start',font=("Helvetica",20))],
		  [sg.Button("Reset",key='-btn_reset',font=("Helvetica",20))]]

window = sg.Window("3分タイマー", layout)
timer_flg = False
while True:
	e,_ = window.read(timeout=10)
	if e == sg.WINDOW_CLOSED: break
	if e.startswith("-btn"):
		if e == "-btn_start":
			#フラグセット + 開始時間保存
			start_time = datetime.datetime.now()
			timer_flg = True
			window["-output"].update("00:00:00")
		elif e == "-btn_reset":
			#フラグクリア
			timer_flg = False
			if pg.mixer.music.get_busy():
				pg.mixer.music.stop()
	#タイマー起動中なら
	if timer_flg:
		cur_time = datetime.datetime.now()
		past_time = cur_time - start_time
		remain = TIMER_SEC - past_time.seconds
		if remain <= 0:
			#3分経過
			pg.mixer.music.play()
			timer_flg = False
			window["-output"].update("00:00:00")
		else:
			window["-output"].update("0" + str(datetime.timedelta(seconds=remain)))
	else:
		continue
window.close()