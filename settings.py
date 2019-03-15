from tkinter import *

window = Tk()
window.title("GUI")
window.geometry('400x200')

bored_eye = BooleanVar()
act_noti = BooleanVar()
dist_bool = BooleanVar()

Label(window, text = "Settings:", fg = "black", width = 20).pack()
Label(window, text="Notifications:").pack(anchor='w')

Checkbutton(window, text="Bored Eye notifications", variable = bored_eye).pack()
Checkbutton(window, text = " Activity notifications   ", variable = act_noti).pack()
Checkbutton(window, text = "Distance from the monitor notifications", variable = dist_bool).pack()




Button(window, text = "START", fg = "black").pack(side = 'right', fill = "x")
window.mainloop()
