import TkEasyGUI as sg


#ユーザに値を尋ねる
while True:
	inch_str = sg.popup_get_text(
		"インチからセンチに変換します。何インチですか？")
	if inch_str == "" :
		sg.popup("何も入力されていません")
		continue
	#Cancelボタン、終了ボタンクリック時はNoneが返ってくるため終了させる
	elif inch_str is None:
		quit()
	#センチに変換して表示
	try:
		inch_val = float(inch_str)
		cm_val = inch_val * 2.54
		#答えを表示
		sg.popup(f"{inch_val}インチは{cm_val}センチになります")
		break
	except ValueError:
		inch_val = 0
		sg.popup("数字を入力してください")