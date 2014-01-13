import wx

#### apt-get install python-wxglade 


class MandelbrotFrame(wx.Frame):
 def __init__(self, parent):
  wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Mandelbrot!', style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
  
  self.DrawingPanel = DrawingPanel(self)
  
  sizer = wx.BoxSizer(wx.VERTICAL)
  sizer.Add(self.DrawingPanel, 1, wx.EXPAND|wx.ALL, 5)
  self.SetSizer(sizer)
  self.Fit()
  self.Show(True)
  
class DrawingPanel(wx.Panel):
 def __init__(self, parent):
  wx.Panel.__init__(self, parent, id=wx.ID_ANY, size=(600,500), style=wx.SIMPLE_BORDER)
  
  self.Bind(wx.EVT_PAINT, self.OnPaint)
  self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
  
 def OnEraseBackground(self, event):
  pass
 
 def OnPaint(self, event):
  dc = wx.BufferedPaintDC(self)
  self.Draw(dc)
  
 def Draw(self, dc):
  dc.SetBrush(wx.WHITE_BRUSH)
  dc.DrawRectangle(-1,-1,600,500)
  
  for x in range(0, 600):
   real = -2 + x * ((1 - -2.0) / 600.0) 
   for y in range(0, 500):
    img = 1.2 - y * ((1.2 - -1.2) / 500.0)
    c = complex(real, img)
    z = 0
    for i in range(0, 30):
     z = z**2 + c
     if abs(z) > 2:
      break
      
    if abs(z) >= 2:
     dc.SetPen(wx.Pen(wx.Colour(0, 8.5*i, 8.5*i)))
     dc.DrawPoint(x, y)
    else:
     dc.SetPen(wx.Pen(wx.Colour(0, 5, 5)))
     dc.DrawPoint(x, y)

if __name__ == '__main__':
 print 'Mandelbrot starting...'
 app = wx.App(0)
 frame = MandelbrotFrame(None)
 app.MainLoop()
