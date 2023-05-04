#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    May 02, 2023 06:03:45 AM CDT  platform: Linux
#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     TNTabs_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #193
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

import sys
import os.path
import mystyles_dark

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import TNTabs

_debug = True  # False to eliminate debug printing from callback functions.
location = TNTabs._location

def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = TNTabs.Toplevel1(_top1)
    startup()
    root.mainloop()

def startup():
    global sty
    sty = ttk.Style()
    os_default_theme = sty.theme_use()
    last_style = os_default_theme
    mystyles_dark.create_styles(sty)
    global background1
    background1 = mystyles_dark.bgcolor
    # load_tcl_themes()
    # themelist = sty.theme_names()
    # print(f"{themelist=}")
    # ===================================================
    # For information on styling the TNotebook tab colours
    # see http://thedesignatedgeek.xyz/python/page/tkinter/gui/book/full%20circle%20magazine/2023/04/29/Tkinter-TNotebook-Tricks-1.html
    # ===================================================
    setup_base_style()
    color_notebook_pages()
    fix_labels()

    # ===================================================
    # The function set_tab_position() will set the tab position
    #  to one of the following options:
    #   "nw","n","ne","en","e","es","sw","s","se","wn","w","ws"
    #  The default position is "nw"
    # ===================================================
    set_tab_position("nw")
    _w1.selectedButton.set(1)
    _top1.title("TNotebook Tab Position Demo")
    centre_screen(794, 644)

def fix_labels():
    global background1
    _w1.Label1.configure(background=background1, foreground="white")
    _w1.Label2.configure(background=background1, foreground="white")
    _w1.TLabel1.configure(background=background1, foreground="white")
    _w1.TLabel2.configure(background=background1, foreground="white")
    _w1.TLabel3.configure(background=background1, foreground="white")
    _w1.TLabel4.configure(background=background1, foreground="white")
    _w1.TLabTab1.set("This is a TLabel")
    _w1.TLabTab2.set("This is a TLabel")
    _w1.TLabTab3.set("This is a TLabel")
    _w1.TLabTab4.set("This is a TLabel")

def color_notebook_pages():
    global background1
    #    background1 = mystyles_dark.bgcolor
    print(f"{background1=}")
    _w1.TNotebook1_t1.configure(background=background1)
    _w1.TNotebook1_t2.configure(background=background1)
    _w1.TNotebook1_t3.configure(background=background1)
    _w1.TNotebook1_t4.configure(background=background1)

def setup_base_style():
    global debug
    # ===================================================
    # Sets up a base style for the TNotebook.
    #   I blatently stole this from Don and hacked it to make it work
    #   for me.  You can use this as a guide to make your own.
    # ===================================================
    style = ttk.Style()

    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", "gray54"),
            ("active", "gray86"),
            ("!active", "sandybrown"),
        ],
        foreground=[("selected", "white"), ("active", "black"), ("!active", "black")],
    )

def set_tab_position(which):
    style = ttk.Style()
    positions = ["nw", "n", "ne", "en", "e", "es", "sw", "s", "se", "wn", "w", "ws"]
    if which in positions:
        style.configure("TNotebook", tabposition=which)
    else:
        print(f"parameter {which} is not a valid position!")
        style.configure("TNotebook", tabposition="nw")
    _top1.update()

def on_TRB_Click(*args):
    if _debug:
        print("TNotebookTabs_support.on_TRB_Click")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()

    which = _w1.selectedButton.get()
    if _debug:
        print(f"{which=}")
    # positions = ["nw", "n", "ne", "en", "e", "es", "sw", "s", "se", "wn", "w", "ws"]
    if which == 1:
        set_tab_position("e")
        set_tab_position("nw")
    elif which == 2:
        set_tab_position("e")
        set_tab_position("n")
    elif which == 3:
        set_tab_position("e")
        set_tab_position("ne")
    elif which == 4:
        set_tab_position("n")
        set_tab_position("en")
    elif which == 5:
        set_tab_position("n")
        set_tab_position("e")
    elif which == 6:
        set_tab_position("n")
        set_tab_position("es")
    elif which == 7:
        set_tab_position("e")
        set_tab_position("se")
    elif which == 8:
        set_tab_position("e")
        set_tab_position("s")
    elif which == 9:
        set_tab_position("e")
        set_tab_position("sw")
    elif which == 10:
        set_tab_position("n")
        set_tab_position("ws")
    elif which == 11:
        set_tab_position("n")
        set_tab_position("w")
    elif which == 12:
        set_tab_position("n")
        set_tab_position("wn")

def on_btnExit(*args):
    if _debug:
        print("TNTabs_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()

def centre_screen(wid, hei):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (wid / 2)
    y = (hs / 2) - (hei / 2)
    root.geometry("%dx%d+%d+%d" % (wid, hei, x, y))

if __name__ == "__main__":
    TNTabs.start_up()




