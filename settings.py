from tkinter import *

window = Tk()
window.title("GUI")
window.geometry('200x100')



Button(window, text = "Settings", fg = "black").pack(fill = "x")


Button(window, text = "START", fg = "black").pack(fill = "x")

window.mainloop()
