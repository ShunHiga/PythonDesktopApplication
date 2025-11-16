import math
import FreeSimpleGUI as sg

#クイズ問題を定義
QUIZ = [
	{"問題":"TCP/IPはインターネット通信の基本的なプロトコルである。","答え":"Yes"},
	{"問題":"Javaはオブジェクト指向言語であるが、多重継承をサポートしている","答え":"No"},
]

#問題を出題
ok = 0
for i, qdata in enumerate(QUIZ):
	#問題を取り出し
	q = qdata["問題"]
	a = qdata["答え"]
	#ポップアップで問題を表示
	user = sg.popup_yes_no(q, title=f"クイズ {i + 1}問目")
	print(user)
	#答え合わせ
	if user == a:
		sg.popup("正解！")
		ok+=1
	else:
		sg.popup("不正解.")
	
sg.popup(f"あなたの点数は{ok}点です")