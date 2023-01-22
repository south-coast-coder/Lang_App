from googletrans import Translator
def test():
    print("tested in translate.py")
def trans(word):
    print("word="+word)
    translator=Translator()
    
    
    newtrans=translator.translate(word, src="ru", dest="en") 
    print(newtrans)
    print(newtrans.pronunciation)
    translator2=Translator()
    orig=translator2.translate(word,src="ru",dest="ru")
    print(orig.pronunciation)
    return newtrans.text, orig.pronunciation
    
#IMPORTANT! After a certain amount of text the Google API locks your API out -
# - if code is refusing to translate (usually throws JSON error) this is probably
# reason, try using diff IP (i.e in cafe) to check.

#note in order to read Russian files need to save in Open Office as txtencoded (option under TXT) once done it will pop up
#wit dialogue and ask for format- tell it UTF - 8, python can handle this!


    

