# TODO: replace
# TODO: settings: whole word, case sensitive
# TODO: gui
# TODO:

import wx
import recherchepy

output = ""

def a(args):
    pass

def recherche_(args):
    output = recherchepy.recherche(dirctrl.GetValue(), strctrl.GetValue(), int(extctrl.GetValue()), casebox.GetValue())
    outputlbl.SetLabel(output)

app = wx.App()
frame = wx.Frame(None, id=0, title="Recherche", size=(500,500))
window = wx.Window(frame)

button = wx.Button(window, label="dab", pos=(200, 420), size=(100, 50))
button.Bind(wx.EVT_BUTTON, recherche_)

dirctrl = wx.TextCtrl(window, pos=(0,0), size=(200,30), value='Directoire')
strctrl = wx.TextCtrl(window, pos=(0,35), size=(200,30), value='Phrase')
extctrl = wx.TextCtrl(window, pos=(0,70), size=(50,30), value='2')

casebox = wx.CheckBox(window, pos=(0,105))

dirtxt = wx.StaticText(window, label='Dans quelle directoire voulez vous chercher?', pos=(200,0))
strtxt = wx.StaticText(window, label='Quelle mot ou phrase cherches-tu?', pos=(200,35))
exttxt = wx.StaticText(window, label='Combien de mots sur chaque cote de la phrase veut tu dans l\'extrait?', pos=(50,70))
casetxt = wx.StaticText(window, label='Sensible aux majuscules et minuscules?', pos=(50,105))

outputlbl = wx.StaticText(window, label='', pos=(0,140))

frame.Show()
app.MainLoop()
