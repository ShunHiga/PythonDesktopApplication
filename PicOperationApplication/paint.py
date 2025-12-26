import FreeSimpleGUI as sg
from PIL import ImageGrab

#キャンバスを定義
canvas = sg.Canvas(size =(400, 400), key="-canvas-", background_color="red")

#ウィンドウを作成
window = sg.Window("マウス操作で絵を描こう", layout=[
	[canvas],
	[sg.Button("閉じる"), sg.Button("保存")]
],finalize=True)

#マウスイベントが発生するように指定
canvas.bind("<ButtonPress-1>", "b_press")
canvas.bind("<ButtonRelease-1>", "b_release")
canvas.bind("<Motion>", "motion")
flag_on = False
while True:
	event, value = window.read()
	print("#event=", event, value)

	if event in ("閉じる", sg.WIN_CLOSED):
		break
	if event == "-canvas-b_press": #ボタンを押した時
		flag_on = True
	elif event == "-canvas-b_release": #ボタンを離した時
		flag_on = False
	elif event == "-canvas-motion": #マウスを動かした
		if not flag_on:
			continue
		#マウスイベントを取得
		e = canvas.user_bind_event
		x, y = e.x, e.y#マウスの位置を取り出す
		#円を描く
		canvas.tk_canvas.create_oval(x, y, x+10, y + 10, fill="white")
	
	##画像を保存
	elif event == "保存":
		x1 = canvas.tk_canvas.winfo_rootx()
		y1 = canvas.tk_canvas.winfo_rooty()
		x2 = x1 + canvas.tk_canvas.winfo_width()
		y2 = y1 + canvas.tk_canvas.winfo_height()
		print(f"x1:{x1},x2:{x2},y1:{y1},y2:{y2}")
		image = ImageGrab.grab((x1, y1, x2, y2))
		image.save("paint.png")
		sg.popup("保存しました")
	
window.close()
