import FreeSimpleGUI as sg
import openpyxl as xl

#Excelファイルから人口統計情報を読み込む関数
def read_population():
	print("read_population")
	#Excelファイルを読み込む
	EXCEL_FILE = "./population_jp.xlsx"
	workbook = xl.load_workbook(EXCEL_FILE)
	#ブックの中のシート「A」を取得
	sheet = workbook["A"]
	columns_info = {
		"都道府県":"I",
		"婚姻率":"CJ",
		"離婚率":"CL"
	}
	#都道府県ごとの総人口を得る
	#メモ：都道府県名はI14からI60のセル
	#総人口はL14からL60のセル
	result = []

	#セル名から列番号を得る
	#連続でセルの値を取得する
	for row in range(14, 60 + 1):
		line = []
		for _, col_name in columns_info.items():
			col_no = xl.utils.column_index_from_string(col_name)
			val = sheet.cell(row, col_no).value
			line.append(val)
		result.append(line)
	workbook.close()
	#婚姻率と離婚率でソートする
	mar_list = list(sorted(result, key=lambda x: x[1],reverse=True))
	div_list = list(sorted(result, key=lambda x: x[2],reverse=True))
	top10 = [
		[
			f"{(i+1):2}", #順位
			f"{mar_list[i][0]}({mar_list[i][1]})",#婚姻率
			f"{div_list[i][0]}({div_list[i][2]})",#離婚率
			
		] for i in range(10)
	]
	return top10

#テーブルに結果を表示する関数
def show_table(data):
	layout = [
		[sg.Table(values=data,
			headings=["ランキング","婚姻率","離婚率"],
			auto_size_columns=True,
			expand_x=True,expand_y=True,
			justification="right",
			font=("Arial",14))],
		[sg.Button("閉じる")]
	]
	#ウィンドウを作成
	window = sg.Window("人口統計",layout, size=(600,400))
	while True:
		event, _ = window.read()
		if event in [sg.WIN_CLOSED, "閉じる"]:
			break
	window.close()

if __name__== "__main__":
	#メイン処理
	data = read_population()#人口統計情報を読み込む
	show_table(data)
	print("テスト")