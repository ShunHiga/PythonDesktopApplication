import FreeSimpleGUI as sg
import os
import csv

file = sg.popup_get_file("CSVファイルを選択してください",
						  multiple_files=False,
						  no_window=False,
						  file_types=(("CSV Files", "*.csv"),("All Files","*.*")))

sg.popup(file, title="選択したファイル")

#複数ファイルの選択ダイアログ
files = sg.popup_get_file("CSVファイルを複数選択",
						  multiple_files=True,
						  no_window=True,
						  file_types=(("CSV Files", "*.csv"),("All Files","*.*")))

sg.popup("\n".join(files), title="選択したファイル一覧")

#保存用のファイル選択ダイアログ
file = sg.popup_get_file("保存先のCSVファイルを指定",
						 save_as=True,
						 no_window=True,
						 file_types=(("CSV Files", "*.csv"),("All Files","*.*")))

sg.popup(file, title="保存先のファイル")