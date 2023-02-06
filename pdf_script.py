from PIL import Image
import pytesseract
import PyPDF2
import os
from PIL import UnidentifiedImageError
from pdf2image import convert_from_path

def test2():
    print("texting in pdf_script")
def use_pdf(file):

    if os.path.exists("new1.txt"):
         os.remove("new1.txt")
        
    file1=open('new1.txt',"a") 

    pdffileobj=open(file,'rb')

    reader=PyPDF2.PdfReader(pdffileobj)

    num_pages=len(reader.pages)
    print(str(num_pages)+"nu,")
    for page in range(num_pages):

         pageobj=reader.pages[page]
         text=pageobj.extract_text()
         print(text)

        
         file1.writelines(text)
# the functions below are for PDFs which are just images so need converting first
def create_string(file):
   images = convert_from_path(file) # This returns a list even for a 1 page pdf
   for i in range(len(images)):
        images[i].save('ukr/ukr_page'+str(i)+'.jpg', 'JPEG')
def convert_to_text(file):
    img = Image.open(file)
    img.load()
    text = pytesseract.image_to_string(img, lang="ukr")  #Specify language to look after!
    print(text)
    return text
# create_string("ukr.pdf")
"""
(Below is how I converted image to readable text - make this into function)
convert_to_text("ukr_page1.jpg")
# with open("judaism_without_embellishments.txt")as file:
ukr=os.listdir("ukr/")
print(ukr[2])
ukr.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
print(ukr)
data1="dldl flflf"
with open("judaism_without_embellishments.txt","a")as file:
    for item in ukr:
        try:
            data=convert_to_text("ukr/"+item)
            
            file.write(data)
           
        except Exception as e:
            print("FAILED!")
            
            print(e)
"""


# define a regex pattern ukr_page/n*/


  



