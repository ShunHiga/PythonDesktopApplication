from xhtml2pdf import pisa
#PDFを生成するHTML
html= """
<html><body>
	<h1 style="font-size: 8em">
		Keep on asking, and it will be given you.
	</h1>
</body></html>
"""

#ファイルを開く
with open('xhtml2pdf_hello.pdf', 'wb') as pdf_file:
	#PDFを生成
	pisa.CreatePDF(html, dest=pdf_file)