import secrets
import pyperclip
import FreeSimpleGUI as sg
import random

#パスワード候補の文字列を記載
upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_str = "abcdefghijklmnopqrstuvxxyz"
number_str = "1234567890"
flag_str = "#!@_-"
password_chars = upper_str + lower_str + number_str + flag_str

#パスワードの文字数を指定
password_length = 16

#パスワード作成
while True:
	p = [secrets.choice(password_chars) for _ in range(password_length)]
	r = [random.choice(password_chars) for _ in range(password_length)]
	password = "".join(p)
	r_password = "".join(r)
	#パスワードをコピー
	pyperclip.copy(password)

	#情報を画面に表示
	yesno = sg.popup_yes_no(
		"以下のパスワードを作成し、クリップボードにコピーしました\n" + 
		f"パスワード：{password}\n Rパスワード：{r_password} \n気に入りましたか？",
		title="作成しました"
	)
	if yesno == "Yes":
		break
	print("パスワードを再生成します")