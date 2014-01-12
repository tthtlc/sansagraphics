
import numpy as np
from scipy.misc import lena
import OpenGL.GL as gl
import wx
from wx.glcanvas import GLCanvas

PI = 3.141592653
theta= 2*PI/30
angle=0.0

class Canvas(GLCanvas):
    def __init__(self,parent):
        """ create the canvas """
        super(Canvas,self).__init__(parent)
        self.done_init_texture = False

        # execute self.onPaint whenever the parent frame is repainted 
        wx.EVT_PAINT(self,self.onPaint)

    def initTexture(self):
        """
        init the texture - this has to happen after an OpenGL context
        has been created
        """

        # make the OpenGL context associated with this canvas the current one
        self.SetCurrent()

        data = np.uint8(np.flipud(lena()))
        w,h = data.shape

        # generate a texture id, make it current
        self.texture = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D,self.texture)

        # texture mode and parameters controlling wrapping and scaling
        gl.glTexEnvf( gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE, gl.GL_MODULATE )
        gl.glTexParameterf( gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT )
        gl.glTexParameterf( gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT )
        gl.glTexParameterf( gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR )
        gl.glTexParameterf( gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR )


        # map the image data to the texture. note that if the input
        # type is GL_FLOAT, the values must be in the range [0..1]
        gl.glTexImage2D(gl.GL_TEXTURE_2D,0,gl.GL_RGB,w,h,0,
            gl.GL_LUMINANCE,gl.GL_UNSIGNED_BYTE,data)

    def onPaint(self,event):
        """ called when window is repainted """
        # make sure we have a texture to draw
        if not self.done_init_texture:
            self.initTexture()
            self.done_init_texture = True
        self.onDraw()

    def onDraw(self):
	global angle
        """ draw function """

        # make the OpenGL context associated with this canvas the current one
        self.SetCurrent()

        # set the viewport and projection       
        w,h = self.GetSize()
        gl.glViewport(0,0,w,h)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0,1,0,1,0,1)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glClear( gl.GL_COLOR_BUFFER_BIT )

        # enable textures, bind to our texture
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D,self.texture)

        gl.glColor3f( 1, 1, 1 )

        # draw a quad
	gl.glRotatef(angle, 1.0, 1.0, 1.0)
	angle+=theta
        gl.glBegin( gl.GL_QUADS )
        gl.glTexCoord2f( 0, 1 );    gl.glVertex2f( 0, 1 )
        gl.glTexCoord2f( 0, 0 );    gl.glVertex2f( 0, 0 )
        gl.glTexCoord2f( 1, 0 );    gl.glVertex2f( 1, 0 )
        gl.glTexCoord2f( 1, 1 );    gl.glVertex2f( 1, 1 )
        gl.glEnd(  )

        gl.glDisable(gl.GL_TEXTURE_2D)

        # swap the front and back buffers so that the texture is visible
        self.SwapBuffers()

def run():
    app = wx.App()
    fr = wx.Frame(None,size=(512,512),title='wxPython texture demo')
    canv = Canvas(fr)
    fr.Show()
    app.MainLoop()

if __name__ == "__main__":
    run()


