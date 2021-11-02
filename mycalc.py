'''
Created on 2021. 7. 21.

@author: pc346
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from gettext import gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,25 ), 0 )
        bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,100 ), 0 )
        bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,125 ), wx.HSCROLL|wx.TE_MULTILINE )
        bSizer3.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer1 = wx.GridSizer( 6, 4, 0, 0 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"<=", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"²√x", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button7, 0, wx.ALL, 5 )
        
        self.m_button8 = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button8, 0, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button9, 0, wx.ALL, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button10, 0, wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button11, 0, wx.ALL, 5 )
        
        self.m_button12 = wx.Button( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button12, 0, wx.ALL, 5 )
        
        self.m_button13 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button13, 0, wx.ALL, 5 )
        
        self.m_button14 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button14, 0, wx.ALL, 5 )
        
        self.m_button15 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button15, 0, wx.ALL, 5 )
        
        self.m_button16 = wx.Button( self, wx.ID_ANY, u"ㅡ", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button16, 0, wx.ALL, 5 )
        
        self.m_button17 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button17, 0, wx.ALL, 5 )
        
        self.m_button18 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button18, 0, wx.ALL, 5 )
        
        self.m_button19 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button19, 0, wx.ALL, 5 )
        
        self.m_button20 = wx.Button( self, wx.ID_ANY, u"┼", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button20, 0, wx.ALL, 5 )
        
        self.m_button21 = wx.Button( self, wx.ID_ANY, u"x/-", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button21, 0, wx.ALL, 5 )
        
        self.m_button22 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button22, 0, wx.ALL, 5 )
        
        self.m_button23 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button23, 0, wx.ALL, 5 )
        
        self.m_button24 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button24, 0, wx.ALL, 5 )
        
        
        bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_textCtrl1.Bind( wx.EVT_TEXT, self.top )
        self.m_textCtrl2.Bind( wx.EVT_TEXT, self.mid )
        self.m_textCtrl3.Bind( wx.EVT_TEXT, self.bot )
        self.m_button1.Bind( wx.EVT_BUTTON, self.hobackbunyulV2 )
        self.m_button2.Bind( wx.EVT_BUTTON, self.hoce )
        self.m_button3.Bind( wx.EVT_BUTTON, self.hoc )
        self.m_button4.Bind( wx.EVT_BUTTON, self.hoback )
        self.m_button5.Bind( wx.EVT_BUTTON, self.hobackbunyul )
        self.m_button6.Bind( wx.EVT_BUTTON, self.homulmul )
        self.m_button7.Bind( wx.EVT_BUTTON, self.horoot )
        self.m_button8.Bind( wx.EVT_BUTTON, self.hodiv )
        self.m_button9.Bind( wx.EVT_BUTTON, self.ho7 )
        self.m_button10.Bind( wx.EVT_BUTTON, self.ho8 )
        self.m_button11.Bind( wx.EVT_BUTTON, self.ho9 )
        self.m_button12.Bind( wx.EVT_BUTTON, self.homul )
        self.m_button13.Bind( wx.EVT_BUTTON, self.ho4 )
        self.m_button14.Bind( wx.EVT_BUTTON, self.ho5 )
        self.m_button15.Bind( wx.EVT_BUTTON, self.ho6 )
        self.m_button16.Bind( wx.EVT_BUTTON, self.hosub )
        self.m_button17.Bind( wx.EVT_BUTTON, self.ho1 )
        self.m_button18.Bind( wx.EVT_BUTTON, self.ho2 )
        self.m_button19.Bind( wx.EVT_BUTTON, self.ho3 )
        self.m_button20.Bind( wx.EVT_BUTTON, self.hosum )
        self.m_button21.Bind( wx.EVT_BUTTON, self.hoplema )
        self.m_button22.Bind( wx.EVT_BUTTON, self.ho0 )
        self.m_button23.Bind( wx.EVT_BUTTON, self.hopoint )
        self.m_button24.Bind( wx.EVT_BUTTON, self.hoset )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def top( self, event ):
        event.Skip()
    
    def mid( self, event ):
        event.Skip()
    
    def bot( self, event ):
        event.Skip()
    
    def hobackbunyulV2( self, event ):
        x = eval(self.m_textCtrl2.GetValue()+'/100')
        self.m_textCtrl2.SetValue(str(x))
        event.Skip()
            
    def hoce( self, event ):
        self.m_textCtrl1.Clear()
        self.m_textCtrl2.Clear()
        event.Skip()
    
    def hoc( self, event ):
        self.m_textCtrl1.Clear()
        self.m_textCtrl2.Clear()
        event.Skip()
    
    def hoback( self, event ):
        x = self.m_textCtrl2.GetValue()
        self.m_textCtrl2.Clear()
        self.m_textCtrl2.SetValue(x[:-1])
        event.Skip()
    
    def hobackbunyul( self, event ):
        x = eval('1/'+self.m_textCtrl2.GetValue())
        self.m_textCtrl2.SetValue(str(x))
        event.Skip()
    
    def homulmul( self, event ):
        x = eval(self.m_textCtrl2.GetValue())
        self.m_textCtrl2.SetValue(str(x*x))
        event.Skip()
    
    def horoot( self, event ):
        x = eval(self.m_textCtrl2.GetValue()+'**0.5')
        self.m_textCtrl2.SetValue(str(x))
        event.Skip()
    
    def hodiv( self, event ):
        x = self.m_textCtrl2.GetValue()
        self.m_textCtrl2.Clear()
        self.m_textCtrl1.AppendText(x+"/")
        event.Skip()
    
    def ho7( self, event ):
        self.m_textCtrl2.AppendText('7')
        event.Skip()
    
    def ho8( self, event ):
        self.m_textCtrl2.AppendText('8')
        event.Skip()
    
    def ho9( self, event ):
        self.m_textCtrl2.AppendText('9')
        event.Skip()
    
    def homul( self, event ):
        x = self.m_textCtrl2.GetValue()
        self.m_textCtrl2.Clear()
        self.m_textCtrl1.AppendText(x+"*")
        event.Skip()
    
    def ho4( self, event ):
        self.m_textCtrl2.AppendText('4')
        event.Skip()
    
    def ho5( self, event ):
        self.m_textCtrl2.AppendText('5')
        event.Skip()
    
    def ho6( self, event ):
        self.m_textCtrl2.AppendText('6')
        event.Skip()
    
    def hosub( self, event ):
        x = self.m_textCtrl2.GetValue()
        self.m_textCtrl2.Clear()
        self.m_textCtrl1.AppendText(x+"-")
        event.Skip()
    
    def ho1( self, event ):
        self.m_textCtrl2.AppendText('1')
        event.Skip()
    
    def ho2( self, event ):
        self.m_textCtrl2.AppendText('2')
        event.Skip()
    
    def ho3( self, event ):
        self.m_textCtrl2.AppendText('3')
        event.Skip()
    
    def hosum( self, event ):
        x = self.m_textCtrl2.GetValue()
        self.m_textCtrl2.Clear()
        self.m_textCtrl1.AppendText(x+"+")
        event.Skip()
    
    def hoplema( self, event ):
        x = eval(self.m_textCtrl2.GetValue())
        self.m_textCtrl2.SetValue(str(-x))
        event.Skip()
    
    def ho0( self, event ):
        self.m_textCtrl2.AppendText('0')
        event.Skip()
    
    def hopoint( self, event ):
        self.m_textCtrl2.AppendText('.')
        event.Skip()
    
    def hoset( self, event ):
        x = self.m_textCtrl1.GetValue()
        y = self.m_textCtrl2.GetValue()
        z = x+y
        a = eval(z)
        self.m_textCtrl3.AppendText(x + y + '=' + str(a)+'\n')
            
        event.Skip()

if __name__=='__main__':
    app = wx.App()
    frame = MyFrame1(parent=None)
    frame.Show()
    app.MainLoop()