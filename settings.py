from tkinter import *
from tkinter import simpledialog
import time

window = Tk()
window.title("GUI")
window.geometry('400x275')
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
        
    def _close(self):
        self.destroy()
        
        
          

def shut_down():
    window.destroy()

Label(window, text="Settings:", fg="black", width=20).pack()
Label(window, text="Notifications:").pack(anchor='w')
bored_eye = Setting("bored eye notifications", window)
act_noti = Setting("activity notifications", window)
dist_bool = Setting("distance from the monitor notifications", window)
drink_w = Setting("drink water reminders", window)
lunch_br = Setting("remind before lunchbreak", window)
post_r = Setting("remind me to imrove posture", window)
gym_r = Setting("remind me to do gymnastics", window)
end_r = Setting("notify me when there are 30 minutes left of the work day", window)

settings = [bored_eye, act_noti, dist_bool, drink_w, lunch_br, post_r, gym_r, end_r]


Button(window, text="START", fg="black", command = shut_down).pack(side='right', fill='x')

while 1:
    for i in settings:
        i.ask()
        
    try:
        window.update()
    except TclError:
        pass
        
    time.sleep(0.01)

window.mainloop()
time.sleep(0.01)
    





window.mainloop()
