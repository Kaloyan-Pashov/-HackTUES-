from win10toast import ToastNotifier
import time
import sys


toaster = ToastNotifier()
toaster.show_toast(sys.argv[1], sys.argv[2], icon_path=sys.argv[3], duration=int(sys.argv[4]))

while toaster.notification_active(): time.sleep(0.1)
