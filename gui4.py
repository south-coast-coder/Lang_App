import wx
import wx.adv
from translate import *
from pdf_script import *

import wx.html

test()
test2()

wordslist={}



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


usefile="rus_3.pdf"
use_pdf(usefile)
current_word="test"
file=open("new.txt","r")
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
use_page="0"

app = wx.PySimpleApp()

frame1=wx.Frame(None, -1, size=(1000,400))

bitmap = wx.Bitmap('loading.png')
splash = wx.adv.SplashScreen(
             bitmap, 
             wx.adv.SPLASH_CENTER_ON_PARENT|wx.adv.SPLASH_NO_TIMEOUT, 
             10000,frame1)
splash.Show()

wx.Yield()



panel=wx.Panel(frame1, size=(400,400),pos=(0,250))



        
btn=wx.Button(panel,id=1,label="previous", size=(100,100), pos=(60,0))
text1=wx.TextCtrl(panel,1000,value="text", size=(150,20))
btn2=wx.Button(panel,id=2,label="next", size=(100,100), pos=(60,53))
def OnClickButton(e):

        global use_page
        global page_marker
        use=e.GetId()
        print("use_page="+str(use_page))
        
        
        
        
        if use==2:  
            if use_page==str(max_thous):
                    print("max thousand reached")
                    return
            html.SetPage("<style>a {text-decoration: none;color: red }</style><body></body>") 
            
            print("usepage" + use_page)
            
            if use_page=="0":
                page_marker=words[1000:2000]
                use_page="2000"
            else:
                use_int=int(use_page)
                page_marker=words[use_int:(use_int+1000)]
                
                use_page=str(use_int+1000)
               
            for item in page_marker:
              html.AppendToPage( "<a href="+item+"> "+item+" </a>")
        if use==1:
            if (use_page=="0") or (use_page=="1000"):
                print("cant go back at beggining")
                return
            else:
                html.SetPage("<style>a {text-decoration: none;color: red }</style><body></body>") 
                use_int=int(use_page)
                page_marker=words[(use_int-2000):(use_int-1000)]
                if use_page=="0":
                    print("already at beggining")
                    return
                use_page=str(use_int-1000)
           
            for item in page_marker:
              html.AppendToPage( "<a href="+item+"> "+item+" </a>")


        
        
        
              
        
               
          
btn2.Bind(wx.EVT_BUTTON,OnClickButton)
btn.Bind(wx.EVT_BUTTON,OnClickButton)


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

                        print ("You Clicked:",e.GetLinkInfo().GetHref())
                        print(e.GetLinkInfo())
                        print(e.GetLinkInfo().GetEvent())
                        useText=e.GetLinkInfo().GetHref()
                        current_word=useText
                        print(current_word)
                        print("current="+current_word)
                        word=trans(current_word)
                        text1.SetLabel(word)
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
app.MainLoop()


