import wx
import wx.adv
import smtplib
import wx.html
import json 

from email.message import EmailMessage
from translate import *
from pdf_script import *


test()
test2()

wordslist={}

# access projects so user can choose
proj_list=[]
with open('projects.json',"r") as file_object:  
  data = json.load(file_object)  
print( data["projects"])
print(data["projects"][0])
print(len(data["projects"]))
for i in range (len(data["projects"])):
    print(data["projects"][i]["name"])
    proj_list.append(data["projects"][i]["name"])

print(proj_list)






class Word:

 def __init__(self, original,trans,times=1):
        self.original=original
        self.trans=trans
        self.times=times
        wordslist[self.original]=self
 def inc(self):
        self.times+=1

Word("wizard","guerre",1)
for key, value in wordslist.items():
    print(key)
    print(value.times)
def checkFreq():
    for key, value in wordslist.items():
                            print(key)
                            print(value.times)
pronun=None
word=None
print("!!!!!FITST !!!!!")
#usefile="rus_long.pdf"
#use_pdf(usefile)
current_word="test"
file=open("judaism_without_embellishments.txt","r")
data=file.read()   
print('length file'+str(len(data)))
words = data.split()
print(len(words))
words_len=len(words)
pages_list=[]
print("thousand words"+str(words_len/1000))
thousands=words_len/1000
for i in range (int(thousands)):  # change this to change no of words per page
    use_i=i+1
    ind=use_i*1000
    pages_list.append(ind)
print("pages list now"+str(pages_list))
max_thous=pages_list[-1] 
print("last thou"+str(max_thous)) # if here then check when forward button clicked and make it do nothing (ie pass)

ten=words[0:1000] # this is extracting words for current page
twenty=words[1000:2000]
# print("ten ----- \n"+str(ten))
page_marker=None
use_page="1000"

app = wx.PySimpleApp()

frame1=wx.Frame(None, -1, size=(2000,800))
frame2=wx.Frame(None, -1, size=(2000,800))


bitmap = wx.Bitmap('loading.png')
splash = wx.adv.SplashScreen(
             bitmap, 
             wx.adv.SPLASH_CENTER_ON_PARENT|wx.adv.SPLASH_NO_TIMEOUT, 
             10000,frame1)
splash.Show()

wx.Yield()


panel2=wx.Panel(frame2, size=(750,400),pos=(0,600))

choice=wx.ComboBox(panel2, choices=proj_list, size=(150,20), pos=(500,0))
def screen_change(self):
    print("change")
    print(self)
    use=self.GetEventObject()
    print(use)
    exit()
    frame2.Destroy()
    frame1.Show()
choice.Bind(wx.EVT_COMBOBOX,screen_change) 

text_c=wx.StaticText(panel2,label="choose a project", size=(150,20),pos=(350,0))


panel=wx.Panel(frame1, size=(750,400),pos=(0,250))

text1=wx.TextCtrl(panel,1000,value="text", size=(150,20))
text2=wx.TextCtrl(panel,1000,value="text", size=(150,20), pos=(400,0))
text3=wx.TextCtrl(panel,1000,value="text", size=(150,20), pos=(190,0))
btn3=wx.Button(panel,label="store", size=(150,20), pos=(600,0))
btn=wx.Button(panel,id=1,label="previous", size=(100,100), pos=(60,0))
btn2=wx.Button(panel,id=2,label="next", size=(100,100), pos=(200,0))
text4=wx.TextCtrl(panel,1000,value="1", size=(150,20), pos=(250,100))
btn4=wx.Button(panel,label="go", size=(150,20), pos=(0,100))
control=wx.TextCtrl(frame1, style=wx.TE_MULTILINE, size=(500,500), pos=(1010,0))
try:
    f = open("1000.txt", "r")
    data=f.read()
    control.SetValue(data)

except:
    print("failed!")
    pass

def OnClickButton(e):

        global use_page
        global page_marker
        use=e.GetId()
        print("use_page="+str(use_page))
        
        
        
        
        if use==2:  
            if use_page==str(max_thous):
                    print("max thousand reached")
                    return
            translation=control.GetValue()
            check_text=str(int(use_page))
            check_text2=str(int(use_page)+1000)
            print("text2 ....")
            print(check_text2)
            with open(check_text+".txt","w") as file:
                file.write(translation)
            print("translation ....")
            print(translation)
           
            
            
            control.SetValue("")
            html.SetPage("<style>a {text-decoration: none;color: red }</style><body></body>") 
            
            try: 
                print("check_text2"+check_text2)
                f = open(check_text2+".txt", "r")
                data=f.read()
                control.SetValue(data)
            except:
                pass
             
            if use_page=="1000":
                page_marker=words[1000:2000]
                
                use_page="2000"
            else:
                print("Else!!!")
                use_int=int(use_page)
                page_marker=words[use_int:(use_int+1000)]

               
                use_page=str(use_int+1000)
               
            for item in page_marker:
              html.AppendToPage( "<a href="+item+"> "+item+" </a>")
            use_int=int((int(use_page))/1000)
            text4.SetValue(str(use_int))
        if use==1:
            if (use_page=="1000") :
                print("cant go back at beggining")
                return
            else:
                translation=control.GetValue()
                check_text=str(int(use_page))
                check_text2=str(int(use_page)-1000)
                print("text2 ....")
                print(check_text2)
                with open(check_text+".txt","w") as file:
                    file.write(translation)
                control.SetValue("")
                html.SetPage("<style>a {text-decoration: none;color: red }</style><body></body>") 
                use_int=int(use_page)
                page_marker=words[(use_int-2000):(use_int-1000)]
                try: 
                    print("check_text2"+check_text2)
                    f = open(check_text2+".txt", "r")
                    data=f.read()
                    control.SetValue(data)
                except:
                    pass
                if use_page=="1000" or use_page=="0":
                    print("already at beggining")
                    return
                use_page=str(use_int-1000)
           
            for item in page_marker:
              html.AppendToPage( "<a href="+item+"> "+item+" </a>")
            use_int=int(int(use_page)/1000)
            text4.SetValue(str(use_int))


        
        
        
              
        
               
btn.Bind(wx.EVT_BUTTON,OnClickButton)         
btn2.Bind(wx.EVT_BUTTON,OnClickButton)
def page_change(e):
   global use_page
   print("clicked!")
   page_no=text4.GetValue()
   page=(int(page_no)*1000)
   print("page="+str(page))
   if page not in pages_list:
    print("invalid page no")
    return
   print(page_no)
   print(page)
   translation=control.GetValue()
   print("translation ....")
   print(translation)
   print("page")
   print(page)
   control.SetValue("")
   html.SetPage("<style>a {text-decoration: none;color: red }</style><body></body>") 
   use_int=page
   page_marker=words[(use_int-1000):use_int]
   
   use_page=str(use_int+1000)

   for item in page_marker:
       html.AppendToPage( "<a href="+item+"> "+item+" </a>")
   use_int=int(use_page)
   print("use int -----")
   print(use_int)
   text4.SetValue(str(int((use_int-1000)/1000)))


    
btn4.Bind(wx.EVT_BUTTON,page_change)
def Store(self):
    global word
    global current_word
    global pronun
    print(word)
    print(pronun)
    print(current_word)
    file=open("stored.txt","a")
    file.write(word+" "+pronun+" "+current_word+"\n")
    file.close()
    
btn3.Bind(wx.EVT_BUTTON,Store)



html = wx.html.HtmlWindow(frame1, size=(1000,250))
html.SetStandardFonts(25)

"""toolbar=wx.ToolBar(self, -1, size=(10,10),pos=(0,150),style=wx.TB_HORIZONTAL | wx.NO_BORDER)
toolbar.Realize()"""






#if "gtk2" in wx.PlatformInfo:


dog="dppppg"
cat="fafafaf"
kitten="glglg"
start=0

html.SetPage(

"<style>a {text-decoration: none;color: red }</style>" #sorry no css support :/]



)
for item in ten:
       html.AppendToPage(
            "<a href="+item+"> "+item+" </a>"
            )













def OnClickWord(e):
                        use=e.GetEventObject()

                        print("clicked word")
                        global current_word
                        global word
                        global pronun
                        print ("You Clicked:",e.GetLinkInfo().GetHref())
                        print(e.GetLinkInfo())
                        print(e.GetLinkInfo().GetEvent())
                        useText=e.GetLinkInfo().GetHref()
                        current_word=useText
                        print(current_word)
                        print("current="+current_word)
                        word, pronun=trans(current_word)
                        text1.SetLabel(current_word.strip(","))
                        text2.SetLabel(word.strip(","))
                        text3.SetLabel(pronun.strip(","))
                        for key, value in wordslist.items():
                            if key==current_word:
                                print("already listed")
                                value.inc()
                                print("value now="+str(value.times))
                                return
                        Word(current_word,word)
                        checkFreq()




                        return current_word
html.Bind(wx.html.EVT_HTML_LINK_CLICKED,OnClickWord)
frame1.Show()  #this and below WERE at bottom
frame2.Show()


app.MainLoop()

#Add code that offers the option to send stored vocab on window close (ask for password rather than storing in the code)


