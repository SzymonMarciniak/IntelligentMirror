from tkinter import *
from toolbar.display_toolbar import OpenToolbar

tk = Tk()
tk.configure(background="black")

OpenTool = OpenToolbar(tk)
OpenTool.pack(side=TOP, anchor=SW)

tk.mainloop()
