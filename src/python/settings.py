from tkinter import *
from tkinter import simpledialog
import time

window = Tk()
window.title("GUI")
window.geometry('400x200')
window.resizable(width=False, height=False)


class Setting:
    def __init__(self, text, master):
        self.var = BooleanVar(value=None)
        self.time = None
        self.text = text
        self.master = master
        Checkbutton(self.master, text=self.text, variable=self.var).pack()

    def ask(self):
        if self.var.get() and not self.time:
            self.time = simpledialog.askinteger("ask", "How much time between " + self.text + "? (in minutes)")
        if not self.var.get():
            self.time = None


Label(window, text="Settings:", fg="black", width=20).pack()
Label(window, text="Notifications:").pack(anchor='w')
bored_eye = Setting("Bored Eye notifications", window)
act_noti = Setting("Activity notifications", window)
dist_bool = Setting("Distance from the monitor notifications", window)
settings = [bored_eye, act_noti, dist_bool]


Button(window, text="START", fg="black", bg='blue').pack(side='right', fill='x')

while 1:
    for i in settings:
        i.ask()

    window.update()
    time.sleep(0.01)

window.mainloop()
