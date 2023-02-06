import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        test_arr=["afafl","fffff"]

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))
        edit_button = wx.Button(self, label='Edit', pos=(10,66))
        edit_button2 = wx.Button(self, label='Edit', pos=(15,70))
        initx=0
        inity=0
        for item in test_arr:
            self.quote = wx.StaticText(panel, label=item)
            initx+=1
            inity+=1
        self.CreateStatusBar()

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()