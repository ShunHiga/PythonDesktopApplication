from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait

#作成するファイル名を指定
pdf_file = "hello.pdf"

#A4サイズのPDFを作成
page = canvas.Canvas(pdf_file, pagesize=portrait(A4))
#ページに文字を描画
page.setFontSize(80)
page.drawString(390, 700, "Hello!")
#PDFを保存
page.save()