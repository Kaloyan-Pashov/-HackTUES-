from tkinter import *
from tkinter import simpledialog
import subprocess
from win10toast import ToastNotifier
import time


window = Tk()
window.title("GUI")
window.geometry('500x400')
window.resizable(width=False, height=False)
sets = {}
set = []
sleeping = 5

f = open("settings.txt", 'r')
for x in f.readlines():
    try:
        set.append(int(x))
    except ValueError:
        set.append(x)

f.close()


class Setting:
    def __init__(self, text, master, notifier, custom=False, absolute=False):
        self.var = BooleanVar(value=None)
        self.j = 1
        self.absolute = absolute
        self.time = 0
        self.notifier = notifier
        self.text = text
        self.master = master
        Checkbutton(self.master, text=self.text, variable=self.var).pack(anchor='w')
        self.time = set.pop(0)
        if self.time != 0:
            self.var.set(True)
            sets[self.text] = self.time
        self.custom = custom

    def ask(self):
        if self.var.get() and not self.time:
            if self.custom:
                self.time = simpledialog.askstring("ask", "What notification you want to be notified about?")
                self.notifier = self.time
            else:
                self.time = simpledialog.askinteger("ask", "How much time between " + self.text + "? (in minutes)")
            sets[self.text] = self.time
        if not self.var.get():
            self.time = 0
            sets[self.text] = self.time

    def uncheck(self):
        self.var.set(False)

    def run(self):
        return time.time()


def shut_down():
    window.destroy()
    f = open("settings.txt", 'w')

    for x in sets.keys():
        f.write(str(sets[x]) + '\n')


def uncheck():
    for x in settings:
        x.uncheck()


Label(window, text="Settings:", fg="black", width=20).pack()
Label(window, text="Notifications:").pack(anchor='w')

bored_eye = Setting("Bored eye notifications", window,
                    "Your eyes are bored! You need to rest them for at least 5 minutes!")
act_noti = Setting("Smiling notifications", window,
                   "You need to smile more! It gives you the hormone of happiness!")
dist_bool = Setting("Distance from the monitor notifications", window,
                    "Stay a bit more far from the monitor!")
drink_w = Setting("Drink water reminders", window,
                  "You may be thirsty! You need to get at least one glass of water!", absolute=True)
lunch_br = Setting("Lunchbreak reminders", window,
                   "Your lunchbreak coming soon! You need to eat something!", absolute=True)
post_r = Setting("Improve posture reminder", window,
                 "Try to improve your posture! You don't need to get back hurts!")
gym_r = Setting("Do gymnastics reminder", window,
                "Do some gymnastics! You need to move!")
end_r = Setting("End of the work day reminder", window,
                "End of the day! You need to rest at home", absolute=True)


settings = [bored_eye, act_noti, dist_bool, drink_w, lunch_br, post_r, gym_r, end_r]

Button(window, text='Uncheck all', fg='black', command=uncheck).pack(anchor='w')
Button(window, text="START", fg="black", command=shut_down).pack(side='right', fill='x')

while 1:
    for i in settings:
        i.ask()

    try:
        window.update()
    except TclError:
        break

    time.sleep(0.01)


def track():
    subprocess.Popen([r"test.exe"])
    f = open("test.txt", 'r')
    a = f.readline()
    f.close()
    f = open("test.txt", 'w')
    f.write('')
    f.close()
    return int(a)


notifications = []
for i in settings:
    if i.time != 0:
       notifications.append(i)

computeroff = 0
computeron = 0
t = time.time()
while 1:
    time.sleep(sleeping)
    print("time off computer is %s seconds"% computeroff)
    print("time on computer is %s seconds"% computeron)
    print("absolute time %s "% time.ctime())
    if track()/1000 > 5*60:
        computeroff += sleeping
    computeron += sleeping
    for i in notifications:
        if i.absolute:
            ct = time.time()
            if int(ct - t) > i.j*i.time*60:
                print("showing notification......")
                toaster = ToastNotifier()
                toaster.show_toast(i.text, i.notifier, duration=10)
                i.j += 1

        else:
            if i.j*(i.time)*60 < computeron:
                print("showing notification......")
                toaster = ToastNotifier()
                toaster.show_toast(i.text, i.notifier, duration=10)
                i.j += 1
    print("#######################################################")



