import wx
from translate import *
from pdf_script import *

import wx.html

test()
test2()



current_word="test"





class MyHtmlFrame(wx.Frame):




    def __init__(self, parent, title):


        items=["won","two","tree","b","a","b","a","b","a","b","a","b","a","b","a","b","c","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b","b","a","b"]
        wx.Frame.__init__(self, parent, -1, title, size=(400,400))

        panel=wx.Panel(self, size=(400,400),pos=(0,250))
    

   
                
        self.btn=wx.Button(panel,label="too", size=(100,100), pos=(60,0))
        self.text1=wx.TextCtrl(panel,1000,value="text", size=(150,20))
        self.btn2=wx.Button(panel,label="too", size=(100,100), pos=(60,53))
        def OnClickButton(e):
                   
                   print(e)
                   
                   
                   word=trans(current_word)
                   self.btn.SetLabel(word)
                   self.text1.SetLabel(word)


                        
                  
        self.btn2.Bind(wx.EVT_BUTTON,OnClickButton)


        self.html = wx.html.HtmlWindow(self, size=(400,250))
        """toolbar=wx.ToolBar(self, -1, size=(10,10),pos=(0,150),style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        toolbar.Realize()"""

        
       



        #if "gtk2" in wx.PlatformInfo:

        self.html.SetStandardFonts()
        dog="dppppg"
        cat="fafafaf"
        kitten="glglg"
        start=0

        self.html.SetPage(

        "<style>a {text-decoration: none;color: ; }</style>" #sorry no css support :/]
        

        
        "<a href="+dog+"\">"+dog+"</a> <a href=\"wizard\">wizard</a>.")
        for item in items:
            if(start==20):
                 self.html.AppendToPage("<br></br> <br></br>")
                
                 print("fourth")
                 start=0
            else:
                self.html.AppendToPage(
                    "<a href="+item+"> "+item+" </a>"


                    )
                start+=1








app = wx.PySimpleApp()

frm = MyHtmlFrame(None, "Simple HTML")
def OnClickWord(e):
                        use=e.GetEventObject()

                        print ("You Clicked:",e.GetLinkInfo().GetHref())
                        print(e.GetLinkInfo())
                        print(e.GetLinkInfo().GetEvent())
                        useText=e.GetLinkInfo().GetHref()
                        current_word=useText
                        print(current_word)
                        print("current="+current_word)
                        self.text1.SetLabel(current_word)
                        return current_word
frm.Bind(wx.html.EVT_HTML_LINK_CLICKED,OnClickWord)
frm.Show()

app.MainLoop()