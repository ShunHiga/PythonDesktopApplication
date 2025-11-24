import FreeSimpleGUI as sg
import math
import datetime

#時計の中心座標を指定
CENTER_X = 200
CENTER_Y = 200
def main():
	layout = [[
		sg.Canvas(
			size = (CENTER_X * 2, CENTER_Y * 2),
			key = '-canvas-',
			background_color= "white"
		)],
		[sg.Button("終了",key="-btn_end")]]

	window = sg.Window("アナログ時計", layout)
	#キャンバスを取得
	canvas = window["-canvas-"]

	#イベントループ
	while True:
		event,_ = window.read(timeout=100)
		#終了ボタンを押されたら終了
		if event in (sg.WINDOW_CLOSED, "-btn_end"): break
		#現在時刻を取得して時計を描画する
		draw_clock(canvas.Widget, datetime.datetime.now())
	window.close()

#時計の針の座標を計算する関数
def calc_hand_coords(angle, rate):
	x = CENTER_X + CENTER_X * rate * math.cos(angle)
	y = CENTER_Y + CENTER_Y * rate * math.sin(angle)
	return x, y

#時計の針を描画する関数
def draw_hand(widget, angle, rate, width, color):
	x,y = calc_hand_coords(angle, rate)
	widget.create_line(
		CENTER_X, CENTER_Y, x, y, width=width, fill=color
	)
#時計を描画する関数
def draw_clock(widget, draw_time):
	#時、分、秒をえる
	h,m,s = draw_time.hour, draw_time.minute, draw_time.second
	h = h % 12 #12時間表示
	#キャンパスをクリアして時計の外枠を描画
	widget.delete('all')
	widget.create_oval(10,10,CENTER_X*2 - 10, CENTER_Y*2 - 10, width = 2)
	#目盛りを表示
	for i in range(12):
		angle = math.radians(i * 30 - 90)
		x1,y1 = calc_hand_coords(angle, 0.8)
		x2,y2 = calc_hand_coords(angle, 0.95)
		widget.create_line(x1,y1,x2,y2,width = 1, fill="silver")
	#各針を描画
	h_angle = math.radians((h / 12 + m / 60 / 12) * 360 - 90)
	draw_hand(widget,h_angle, 0.5, 20,'black')
	min_angle = math.radians(( m / 60 ) * 360 - 90)
	draw_hand(widget, min_angle, 0.7, 15, 'black')
	s_angle = math.radians(s/60 * 360 - 90)
	draw_hand(widget, s_angle, 0.9, 2, 'red')
if __name__ == '__main__':
	main()