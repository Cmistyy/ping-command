import wx
import subprocess



class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw, size=(725, 505))
        
        panel = wx.Panel(self)
        
        # Domena
        wx.StaticText(panel, label="Podaj domenę:", pos=(10, 10))
        self.domain = wx.TextCtrl(panel, pos=(150, 5), size = (100, 25))
        self.domain.Value = 'localhost'
        
        # Ile pakietów
        wx.StaticText(panel, label="Podaj ilość pakietów:", pos=(10, 40))
        self.requests = wx.TextCtrl(panel, pos=(150, 35), size = (100, 25))
        self.requests.Value = '4'

        # Wielkość pakietu
        wx.StaticText(panel, label="Podaj wielkość pakietów:", pos=(10, 70))
        self.buffer = wx.TextCtrl(panel, pos=(150, 65), size = (100, 25))
        self.buffer.Value = '32'

        # TTL
        wx.StaticText(panel, label="Time to Live:", pos=(10, 100))
        self.ttl = wx.TextCtrl(panel, pos=(150, 95), size = (100, 25))
        self.ttl.Value = '128'

        # Przycisk
        self.testBtn = wx.Button(panel, label='Testuj', pos=(350, 30), size = (200, 70))
        self.testBtn.Bind(wx.EVT_BUTTON, self.on_press)
        
        # Wynik
        self.result = wx.TextCtrl(panel, pos=(5, 160), size = (700, 300), style= wx.TE_MULTILINE | wx.TE_READONLY | wx.SUNKEN_BORDER)

    def on_press(self, event):    
        self.result.Value='Proszę czekać. Testowanie...'
        self.testBtn.Enabled = False
        self.Update()
        i = subprocess.run(
            ['ping', 
            '-n', self.requests.GetValue(),
            '-l', self.buffer.GetValue(), 
            '-i', self.ttl.GetValue(), 
            self.domain.GetValue()], 
            stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.result.Value=i
        self.testBtn.Enabled = True

app = wx.App()
frm = MyFrame(None, title='Ping')
frm.Show()
app.MainLoop()