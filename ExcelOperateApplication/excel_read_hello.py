import FreeSimpleGUI as sg
import openpyxl as xl

#Excelファイルを読み込む
workbook = xl.load_workbook("./excel_hello.xlsx")

#アクティブなシートを取得
sheet = workbook.active

#セルA1の内容を読む
val = sheet["A1"].value
sg.popup(val, title="A1の内容")

#ワークブックを閉じる
workbook.close()