from tkinter import *
from tkinter import simpledialog
import time

window = Tk()
window.title("GUI")
window.geometry('400x275')
window.resizable(width=False, height=False)
sets = {}


class Setting:
    def __init__(self, text, master):
        self.var = BooleanVar(value=None)
        self.time = 0
        self.text = text
        self.master = master
        Checkbutton(self.master, text=self.text, variable=self.var).pack()
        sets[self.text] = self.time

    def ask(self):
        if self.var.get() and not self.time:
            self.time = simpledialog.askinteger("ask", "How much time between " + self.text + "? (in minutes)")
            sets[self.text] = self.time
        if not self.var.get():
            self.time = 0


def shut_down():
    window.destroy()
    f = open("settings.txt", 'w')

    for x in sets.keys():
        f.write(str(sets[x]) + '\n')


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

Button(window, text="START", fg="black", command=shut_down).pack(side='right', fill='x')




while 1:
    for i in settings:
        i.ask()

    try:
        window.update()
    except TclError:
        break

    time.sleep(0.01)
