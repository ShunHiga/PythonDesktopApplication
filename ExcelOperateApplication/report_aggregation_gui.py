import os
import FreeSimpleGUI as sg
import report_aggregation

while True:
	target_dir = sg.popup_get_folder(
		"処理対象のディレクトリを選択してください",
		title="部署ごとのExcelブックのフォルダーを選択",
		default_path=os.path.dirname(__file__),#初期ディレクトリ
		no_window=False
	)
	#キャンセルが押されたら終了
	if target_dir == "" or target_dir is None:
		quit()
	#集計した売り上げ報告書の保存ファイル名を自動的に決める
	dir_name = os.path.basename(target_dir)
	save_file = os.path.join(os.path.dirname(target_dir), f"{dir_name}-all.xlsx")

	#パスを表示する
	yesno = sg.popup_yes_no(
		"以下のディレクトリで良いですか？\n" +
		f"対象ディレクトリ：{target_dir}\n" + 
		f"売り上げ報告書の保存先：{save_file}", title="確認"
	)
	if yesno != "Yes":
		continue

	report_aggregation.make_report(target_dir, save_file)
	break