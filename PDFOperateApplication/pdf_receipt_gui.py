import FreeSimpleGUI as sg
import pdf_recopt

#ウィンドウを作成
window = sg.Window("領収書PDF作成", layout=[
	[sg.Text("名前"),sg.InputText(key="name")],
	[sg.Text("用途"),sg.InputText(key="memo")],
	[sg.Text("金額"),sg.InputText(key="price")],
	[sg.Button("PDF作成")]
])

#イベントループ
while True:
	event, val = window.read()
	if event == sg.WINDOW_CLOSED:
		break
	if event == "PDF作成":
		#保存先を選択するダイアログを表示
		save_file = sg.popup_get_file("保存先を選択してください", save_as=True, no_window= True)
		if save_file is None or save_file == "":
			continue
		#PDFを作成
		pdf_recopt.make_recipt(
			save_file,
			val["name"],
			val["memo"],
			int(val["price"]),
		)
		sg.popup("PDFファイルを作成しました")

window.close()
