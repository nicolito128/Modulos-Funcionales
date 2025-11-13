import tkinter as tk

_root: tk.Tk = None

MIN_WINDOW_WIDTH = 640
MIN_WINDOW_HEIGHT = 480

_MAIN_WINDOW_TITLE = "Sistema de Biblioteca Digital"

def start_gui():
    _root = tk.Tk()
    _root.title(_MAIN_WINDOW_TITLE)
    _root.minsize(width=MIN_WINDOW_WIDTH, height=MIN_WINDOW_HEIGHT)

    make_sidepanel(_root)

    _root.mainloop()

def make_sidepanel(win: tk.Tk):
    panel = tk.Frame(win, bg="skyblue", width=200, height=MIN_WINDOW_HEIGHT)
    panel.grid(row=0, column=0)
