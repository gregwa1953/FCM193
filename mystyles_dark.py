#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     mystyles_dark.py
#  ------------------------------------------------------
# Created for Learning PAGE
# Written by G.D. Walters
# Copyright (c) 2022 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Version 2.04
# ======================================================
# Version history
#    Pre-2.0 proof of concept
#    2.02 - 29 November, 2022 - First Alpha release
#    2.03 - 29 November, 2022 - Changed globals to shared module
#    2.04 - 30 November, 2022 - Added Dark style, global color definitions
# ======================================================
import sys
import shared
import tkinter as tk
import os.path

_script = sys.argv[0]
location = os.path.dirname(_script)

# ===================================================
# Global Color definitions
# ===================================================
bgcolor = 'gray24'
fgcolor = 'gray78'
activebgcolor = 'gray66'
activefgcolor = 'gray5'
troughcolor = 'gray43'
barcolor = 'gray82'
_darkcolor = bgcolor
_lightcolor = fgcolor
disabledcolor = 'gray27'
disabledfgcolor = 'gray3'
fieldbgcolor = 'gray20'
fieldfgcolor = 'gray79'
_bordercolor = 'dimgray'


def create_styles(sty):
    sty.configure(
        "Formatted.TLabel",
        font="Ubuntu 12 bold",
        # anchor=tk.CENTER,
        background=bgcolor,
        foreground=fgcolor)

    # ===================================================
    # Style for ALL TButton widgets
    # ===================================================
    sty.map("TButton",
            background=[('disabled', '#d9d9d9'), ('active', activebgcolor)],
            foreground=[('disabled', disabledfgcolor),
                        ('active', activefgcolor)])
    sty.configure("TButton",
                  foreground=fgcolor,
                  background=bgcolor,
                  padding=[4, 4, 4, 4],
                  font="Ubuntu 12 bold")
    # ===================================================
    # Style for Exit button
    # ===================================================
    sty.configure("Custom.TButton",
                  foreground=fgcolor,
                  background=bgcolor,
                  pading=[10, 10, 10, 10],
                  font="Veranda 12 bold")
    sty.map('Custom.TButton',
            background=[('disabled', '#d9d9d9'), ('active', activebgcolor)],
            foreground=[('disabled', 'snow'), ('active', activefgcolor)])

    # ===================================================
    # Style for TCombobox (in progress)
    # ===================================================
    sty.configure("TCombobox",
                  background=bgcolor,
                  foreground=fgcolor,
                  fieldbackground=fieldbgcolor,
                  fieldforeground=fieldfgcolor)
    sty.configure("ComboboxPopdownFrame",
                  background=bgcolor,
                  foreground=fgcolor,
                  fieldbackground=fieldbgcolor,
                  fieldforeground=fieldfgcolor,
                  borderwidth=2,
                  relief="sunken")

    # ===================================================
    # Style for TEntry (in progress)
    # Entry images borrowed from Sun-Valley-Ttk-Theme-Master
    # ===================================================
    sty.configure('TEntry',
                  foreground=fieldfgcolor,
                  fieldbackground=fieldbgcolor)

    # ===================================================
    # This layout will replace the standard indicator
    # from TCheckbuttons that are told to use this style
    # ===================================================
    shared.on_image = tk.PhotoImage(
        file=os.path.join(location, 'Assets/chk16.png'))
    shared.off_image = tk.PhotoImage(
        file=os.path.join(location, 'Assets/unchk16.png'))
    shared.dis_image = tk.PhotoImage(
        file=os.path.join(location, 'Assets/Disabled1.png'))
    sty.element_create('custom.CBindicator', 'image', shared.off_image,
                       ('selected', shared.on_image),
                       ('disabled', shared.dis_image))
    sty.configure('TCheckbutton',
                  background=bgcolor,
                  foreground=fgcolor,
                  padding=[5, 1, 5, 1])
    sty.layout('TCheckbutton', [('Checkbutton.padding', {
        'sticky':
        'nswe',
        'children': [('custom.CBindicator', {
            'side': 'left',
            'sticky': ''
        }),
                     ('Checkbutton.focus', {
                         'side': 'left',
                         'sticky': '',
                         'children': [('Checkbutton.label', {
                             'sticky': 'nswe'
                         })]
                     })]
    })])
    sty.map('TCheckbutton',
            background=[('disabled', disabledcolor),
                        ('pressed', activebgcolor), ('active', activebgcolor),
                        ('hover', activebgcolor)],
            foreground=[('disabled', disabledfgcolor),
                        ('pressed', activefgcolor), ('active', activefgcolor),
                        ('hover', activefgcolor)])
    # ===================================================
    # This layout will replace the standard indicator
    # from TRadiobuttons that are told to use this style
    # ===================================================
    shared.on_image3 = tk.PhotoImage(
        file=os.path.join(location, 'Assets/radio-nc.png'))
    shared.off_image3 = tk.PhotoImage(
        file=os.path.join(location, 'Assets/radio-nu.png'))
    shared.dis_image2 = tk.PhotoImage(
        file=os.path.join(location, 'Assets/Alternate1.png'))

    sty.element_create('custom.indicator', 'image', shared.off_image3,
                       ('selected', shared.on_image3),
                       ('disabled', shared.dis_image2))
    sty.configure('TRadiobutton',
                  background=bgcolor,
                  foreground=fgcolor,
                  padding=[5, 1, 5, 1])
    sty.layout('TRadiobutton', [('Radiobutton.padding', {
        'sticky':
        'nswe',
        'children': [('custom.indicator', {
            'side': 'left',
            'sticky': ''
        }),
                     ('Radiobutton.focus', {
                         'side': 'left',
                         'sticky': '',
                         'children': [('Radiobutton.label', {
                             'sticky': 'nswe'
                         })]
                     })]
    })])
    sty.map('TRadiobutton',
            background=[('disabled', disabledcolor),
                        ('pressed', activebgcolor), ('active', activebgcolor),
                        ('hover', activebgcolor)],
            foreground=[('disabled', disabledfgcolor),
                        ('pressed', activefgcolor), ('active', activefgcolor),
                        ('hover', activefgcolor)])
    # ===================================================
    # Style for ALL TProgressbars
    # ===================================================
    # TROUGH_COLOR = 'lightblue2'
    # BAR_COLOR = 'navajowhite2'
    sty.configure("bar.Horizontal.TProgressbar",
                  troughcolor=troughcolor,
                  bordercolor=troughcolor,
                  background=barcolor,
                  lightcolor=barcolor,
                  darkcolor=barcolor)

    # ===================================================
    # Style for ALL TScale widgets
    # ===================================================
    # TROUGH_COLOR = 'lightblue2'
    # BAR_COLOR = 'navajowhite2'
    sty.configure("bar.Horizontal.TScale",
                  troughcolor=troughcolor,
                  bordercolor=troughcolor,
                  background=barcolor,
                  lightcolor=barcolor,
                  darkcolor=barcolor)
    # ===================================================
    # Style for ALL TSpinbox Widgets
    # ===================================================
    sty.configure("Custom.TSpinbox",
                  bordercolor=_bordercolor,
                  background=bgcolor,
                  foreground=fgcolor,
                  lightcolor=_lightcolor,
                  darkcolor=_darkcolor,
                  selectbackground='springgreen2',
                  selectforeground='black',
                  fieldbackground=fieldbgcolor,
                  fieldforeground=fieldfgcolor)

    # ===================================================
    # Style for ALL TFrame widgets
    # ===================================================
    sty.configure('TFrame', background='gray24', relief=tk.SUNKEN)

    # ===================================================
    # Style for ALL TLabelframe widgets
    # ===================================================
    sty.configure('TLabelframe',
                  background=bgcolor,
                  bordercolor=_bordercolor,
                  borderwidth=3,
                  darkcolor=_darkcolor,
                  labelmargins=10,
                  labeloutside=False,
                  lightcolor=_lightcolor,
                  relief=tk.GROOVE)
    sty.configure('TLabelframe.Label',
                  font=('Ubuntu 10 bold'),
                  foreground=fgcolor,
                  background=bgcolor,
                  padding=[12, 6])
    # sty.theme_settings("default",
    #                    {'TLabelframe.Label': {
    #                        'configure': {
    #                            "padding": 7
    #                        }
    #                    }})
