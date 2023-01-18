import PyPDF2

def test2():
	print("texting in pdf_script")
def use_pdf(file):

	pdffileobj=open('file','rb')

	reader=PyPDF2.PdfReader(pdffileobj)

	x = len(reader.pages)

	pageobj=reader.pages[0]

	text=pageobj.extract_text()

	file1=open('temp.txt',"a") 

	file1.writelines(text)