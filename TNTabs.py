#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    May 02, 2023 06:27:50 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import TNTabs_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 
font10 = "-family {DejaVu Sans} -size 10"

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='-family {DejaVu Sans} -size 10')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TRadiobutton',background =
           [('selected', _bgcolor), ('active', _ana2color)], indicatorcolor =
           [('selected', _fgcolor), ('!active', _bgcolor)])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("794x644+344+176")
        top.minsize(1, 1)
        top.maxsize(2545, 1410)
        top.resizable(0,  0)
        top.title("Toplevel 0")
        top.configure(highlightcolor="black")

        self.top = top
        self.TLabTab1 = tk.StringVar()
        self.TLabTab2 = tk.StringVar()
        self.TLabTab3 = tk.StringVar()
        self.TLabTab4 = tk.StringVar()
        self.selectedButton = tk.IntVar()

        _style_code()
        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(x=0, y=0, height=644, width=863)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")
        self.TLabelframe1 = ttk.Labelframe(self.TFrame1)
        self.TLabelframe1.place(x=17, y=75, height=74, width=758)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''TNotebook Tab Position''')
        self.TRadiobutton1 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton1.place(x=4, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton1.configure(variable=self.selectedButton)
        self.TRadiobutton1.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton1.configure(text='''NW''')
        self.TRadiobutton1.configure(compound='left')
        self.TRadiobutton2 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton2.place(x=65, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton2.configure(variable=self.selectedButton)
        self.TRadiobutton2.configure(value='2')
        self.TRadiobutton2.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton2.configure(text='''N''')
        self.TRadiobutton2.configure(compound='left')
        self.TRadiobutton3 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton3.place(x=126, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton3.configure(variable=self.selectedButton)
        self.TRadiobutton3.configure(value='3')
        self.TRadiobutton3.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton3.configure(text='''NE''')
        self.TRadiobutton3.configure(compound='left')
        self.TRadiobutton4 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton4.place(x=187, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton4.configure(variable=self.selectedButton)
        self.TRadiobutton4.configure(value='4')
        self.TRadiobutton4.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton4.configure(text='''EN''')
        self.TRadiobutton4.configure(compound='left')
        self.TRadiobutton5 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton5.place(x=248, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton5.configure(variable=self.selectedButton)
        self.TRadiobutton5.configure(value='5')
        self.TRadiobutton5.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton5.configure(text='''E''')
        self.TRadiobutton5.configure(compound='left')
        self.TRadiobutton6 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton6.place(x=309, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton6.configure(variable=self.selectedButton)
        self.TRadiobutton6.configure(value='6')
        self.TRadiobutton6.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton6.configure(text='''ES''')
        self.TRadiobutton6.configure(compound='left')
        self.TRadiobutton7 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton7.place(x=370, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton7.configure(variable=self.selectedButton)
        self.TRadiobutton7.configure(value='7')
        self.TRadiobutton7.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton7.configure(text='''SE''')
        self.TRadiobutton7.configure(compound='left')
        self.TRadiobutton8 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton8.place(x=431, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton8.configure(variable=self.selectedButton)
        self.TRadiobutton8.configure(value='8')
        self.TRadiobutton8.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton8.configure(text='''S''')
        self.TRadiobutton8.configure(compound='left')
        self.TRadiobutton9 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton9.place(x=479, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton9.configure(variable=self.selectedButton)
        self.TRadiobutton9.configure(value='9')
        self.TRadiobutton9.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton9.configure(text='''SW''')
        self.TRadiobutton9.configure(compound='left')
        self.TRadiobutton10 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton10.place(x=541, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton10.configure(variable=self.selectedButton)
        self.TRadiobutton10.configure(value='10')
        self.TRadiobutton10.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton10.configure(text='''WS''')
        self.TRadiobutton10.configure(compound='left')
        self.TRadiobutton11 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton11.place(x=614, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton11.configure(variable=self.selectedButton)
        self.TRadiobutton11.configure(value='11')
        self.TRadiobutton11.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton11.configure(text='''W''')
        self.TRadiobutton11.configure(compound='left')
        self.TRadiobutton12 = ttk.Radiobutton(self.TLabelframe1)
        self.TRadiobutton12.place(x=675, y=27, width=57, height=21
                , bordermode='ignore')
        self.TRadiobutton12.configure(variable=self.selectedButton)
        self.TRadiobutton12.configure(value='12')
        self.TRadiobutton12.configure(command=TNTabs_support.on_TRB_Click)
        self.TRadiobutton12.configure(text='''WN''')
        self.TRadiobutton12.configure(compound='left')
        self.TNotebook1 = ttk.Notebook(self.TFrame1)
        self.TNotebook1.place(x=120, y=200, height=316, width=554)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Standard Tk Widgets''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''ttk Widgets''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Enhanced Widgets''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Extra Stuff''', compound="left"
                ,underline='''-1''', )
        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(x=140, y=60, height=41, width=254)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(compound='left')
        self.Label2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label2.configure(text='''Just a Tk Label Widget''')
        self.TLabel1 = ttk.Label(self.TNotebook1_t1)
        self.TLabel1.place(x=130, y=150, height=39, width=262)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='center')
        self.TLabel1.configure(text='''Tlabel''')
        self.TLabel1.configure(textvariable=self.TLabTab1)
        self.TLabTab1.set('''Tlabel''')
        self.TLabel1.configure(compound='left')
        self.TLabel2 = ttk.Label(self.TNotebook1_t2)
        self.TLabel2.place(x=30, y=30, height=39, width=302)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Tlabel''')
        self.TLabel2.configure(textvariable=self.TLabTab2)
        self.TLabTab2.set('''Tlabel''')
        self.TLabel2.configure(compound='left')
        self.TLabel3 = ttk.Label(self.TNotebook1_t3)
        self.TLabel3.place(x=160, y=100, height=39, width=242)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Tlabel''')
        self.TLabel3.configure(textvariable=self.TLabTab3)
        self.TLabTab3.set('''Tlabel''')
        self.TLabel3.configure(compound='left')
        self.Label1 = tk.Label(self.TNotebook1_t4)
        self.Label1.place(x=140, y=60, height=31, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label1.configure(text='''Just a widget''')
        self.TLabel4 = ttk.Label(self.TNotebook1_t4)
        self.TLabel4.place(x=70, y=140, height=39, width=362)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Tlabel''')
        self.TLabel4.configure(textvariable=self.TLabTab4)
        self.TLabTab4.set('''Tlabel''')
        self.TLabel4.configure(compound='left')
        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(x=670, y=20, height=38, width=103)
        self.TButton1.configure(command=TNTabs_support.on_btnExit)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Exit''')
        self.TButton1.configure(compound='left')

def start_up():
    TNTabs_support.main()

if __name__ == '__main__':
    TNTabs_support.main()




