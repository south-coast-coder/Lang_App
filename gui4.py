import wx
from translate import *
from pdf_script import *

import wx.html

test()
test2()



current_word="test"


app = wx.PySimpleApp()
items=["won","two","tree","b","a","b","a","b","a","b","a","b","a","b","a","b","c","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b"]
frame1=wx.Frame(None, -1, size=(400,400))

panel=wx.Panel(frame1, size=(400,400),pos=(0,250))



        
btn=wx.Button(panel,label="too", size=(100,100), pos=(60,0))
text1=wx.TextCtrl(panel,1000,value="text", size=(150,20))
btn2=wx.Button(panel,label="too", size=(100,100), pos=(60,53))
def OnClickButton(e):
           
           print(e)
           
           
           word=trans(current_word)
           btn.SetLabel(word)
           text1.SetLabel(word)


                
          
btn2.Bind(wx.EVT_BUTTON,OnClickButton)


html = wx.html.HtmlWindow(frame1, size=(400,250))
"""toolbar=wx.ToolBar(self, -1, size=(10,10),pos=(0,150),style=wx.TB_HORIZONTAL | wx.NO_BORDER)
toolbar.Realize()"""






#if "gtk2" in wx.PlatformInfo:

html.SetStandardFonts()
dog="dppppg"
cat="fafafaf"
kitten="glglg"
start=0

html.SetPage(

"<style>a {text-decoration: none;color: ; }</style>" #sorry no css support :/]



"<a href="+dog+"\">"+dog+"</a> <a href=\"wizard\">wizard</a>.")
for item in items:
    if(start==20):
         html.AppendToPage("<br></br> <br></br>")
        
         print("fourth")
         start=0
    else:
        html.AppendToPage(
            "<a href="+item+"> "+item+" </a>"


            )
        start+=1











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
                        return current_word
html.Bind(wx.html.EVT_HTML_LINK_CLICKED,OnClickWord)

frame1.Show()
app.MainLoop()