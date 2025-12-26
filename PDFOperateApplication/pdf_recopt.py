import os
import datetime
import math
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import B6, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

#ひな形ファイルなどの指定
script_dir = os.path.dirname(__file__)
template_file = os.path.join(script_dir, "receipt.png")
font_file = os.path.join(script_dir, "ipaexg00401", "ipaexg.ttf")
tax_rate = 0.1 #税率の指定

#領収書を作成する関数
def make_recipt(output_file, name, memo, price):
	#税込金額を計算
	tax = math.ceil(price * tax_rate)
	price_n_tax = price + tax
	#日付を取得
	date_a = datetime.datetime.now().strftime("%Y-%m-%d").split("-")
	#フォントの埋め込み
	pdfmetrics.registerFont(TTFont("IPAexGothic", font_file))
	#容姿サイズを指定してキャンバスを作成
	page = canvas.Canvas(output_file, pagesize=landscape(B6))
	#キャンバスに合わせて画像を描画
	w, h = Image.open(template_file).size
	r = B6[1] / w
	pdf_h, pdf_w = int(h * r), int(w * r)
	page.drawImage(template_file, 0, 0, width=pdf_w,height=pdf_h)
	#領収証に書き込みを行う
	page.setFont("IPAexGothic", 20)
	page.drawCentredString(150,240, name)
	page.drawString(120, 185, f"¥{price_n_tax:,}-")
	page.setFont("IPAexGothic", 12)
	page.drawString(85, 153, f"{memo}")
	page.drawRightString(215, 65, f"¥{price:,}-")
	page.drawRightString(215,39,f"¥{tax:,}-")
	page.drawString(55,55,f"{int(tax_rate * 100)}")
	page.drawString(327,287,f"{date_a[0]}")
	page.drawString(380,287,f"{date_a[1]}")
	page.drawString(420,287,f"{date_a[2]}")
	page.save()


if __name__ == "__main__":
	output_file = os.path.join(script_dir, "pdf_recipt.pdf")
	make_recipt(
		output_file,
		name="山田　太郎",
		memo="文房具代として",
		price=1000
	)
