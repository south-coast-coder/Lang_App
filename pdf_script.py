from PIL import Image
import pytesseract
import PyPDF2
import os
import shutil
from PIL import UnidentifiedImageError
from pdf2image import convert_from_path
from pypdf import PdfReader


def test2():
    print("texting in pdf_script")
def use_pdf(file, proj_folder):
    EOF_MARKER= b'%%EOF'
    print("file="+file)
    file_name=file.strip(".")[-1]
    print("file_name"+file_name)
    if os.path.exists(proj_folder+"new1.txt"):
         os.remove(proj_folder+"new1.txt")
    with open(file,'rb') as f:
         contents=f.read()
   
    

    file1=proj_folder+'new1.txt'
    

    pdffileobj=open(file,'rb')

    reader=PdfReader(pdffileobj)
    text=""

    for page in reader.pages:
        text+= page.extract_text() + "\n"
        
    print(text)
    
    with open(file1,'wb') as f:
        f.write(text.encode('utf8'))
   

        
         
# the functions below are for PDFs which are just images so need converting first
def create_string(file,proj_folder):
   print("BELOW")
   print(file)
   print(proj_folder)
   proj_name=proj_folder.strip("/")
   file_name=file.split("/")[-1]
   print(file_name)
   use_path=proj_folder+file_name
   split=use_path.split("/",2)
   new=split[0]+"/"+split[1]+"/"
   print(new)
   print("usepath="+use_path)
   print("file="+file)
   proj_folder+file
   shutil.copy2(file, use_path)
   print("proj_folder+file:")
   print(proj_folder+file)
   print(new)
   print("new+file")
   print(new+file_name)
   images = convert_from_path(new+file_name) # This returns a list even for a 1 page pdf

   for i in range(len(images)):
        images[i].save(new+"page"+str(i)+'.jpg', 'JPEG')
   print("DONE!")
def convert_to_text(file,lang): #language take from main then comapre with list of pytesseract langs and convert
    use_lang=None
   
    tess_langs={"ru":"rus","uk":"ukr","fr":"fra","ar":"ara","de":"deu"}
 
    if lang in tess_langs:
        use_lang=tess_langs[lang]
       
        
       
  
    img = Image.open(file)
    img.load()
    text = pytesseract.image_to_string(img, lang=use_lang)  #Specify language to look after!
   
    return text

"""
(Below is how I converted image to readable text - make this into function)
convert_to_text("ukr_page1.jpg")
"""
if __name__=='__main__':
   
    

    
    robes=os.listdir("frenchtest/")

    robes.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))


    with open("robes_test.txt","a")as file:
        for item in robes:
            try:
                data=convert_to_text("frenchtest/"+item)
                
                file.write(data)
               
            except Exception as e:
                print("FAILED!")
                
                print(e)
   


    