import openpyxl as xl

#新しいワークブックを作成
workbook = xl.Workbook()

#アクティブなシートを取得
sheet = workbook.active

#セルA1に格言を書き込む
sheet["A1"] = "多くの富よりも良い名を選べ。尊ばれることは銀や金に勝る。"

#Excelファイルを保存
workbook.save("excel_hello.xlsx")

#ワークブックを閉じる
workbook.close()