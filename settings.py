from tkinter import *
from tkinter import simpledialog
import time

window = Tk()
window.title("GUI")
window.geometry('400x200')
window.resizable(width = False, height = False)

bored_eye = BooleanVar(value = False)
act_noti = BooleanVar(value = False)
dist_bool = BooleanVar(value = False)
bored_eye_time = None
act_noti_time = None
dist_bool_time = None


Label(window, text = "Settings:", fg = "black", width = 20).pack()
Label(window, text="Notifications:").pack(anchor='w')
Checkbutton(window, text="Bored Eye notifications", variable = bored_eye).pack()
Checkbutton(window, text = " Activity notifications   ", variable = act_noti).pack()
Checkbutton(window, text = "Distance from the monitor notifications", variable = dist_bool).pack()



Button(window, text = "START", fg = "black", bg = 'blue').pack(side = 'right', fill = 'x')

while 1:
    if bored_eye.get() == True and not bored_eye_time:
        bored_eye_time = simpledialog.askinteger("", "How much time between notifications? (in minutes)")
        
    if act_noti.get() == True and not act_noti_time:
        act_noti_time =  simpledialog.askinteger("", "How much time between notifications? (in minutes)")
        
    if dist_bool.get() == True and not dist_bool_time:
        dist_bool_time = simpledialog.askinteger("", "How much time between notifications? (in minutes)") 
    window.update()
    time.sleep(0.01)
    





window.mainloop()

