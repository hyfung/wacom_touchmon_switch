#!/usr/bin/python3
import subprocess, tkinter, os

ENA = "xinput enable "
DIS = "xinput disable "

touch_id = 0
stylus_id = 0

res = subprocess.check_output("xinput").decode().split("\n")
#print(res)

touch_id = str([x for x in res if "Finger touch" in x])
stylus_id = str([x for x in res if "Pen stylus" in x])

touch_id = touch_id[touch_id.index("id=")+3:touch_id.index("\\t[")]
stylus_id = stylus_id[stylus_id.index("id=")+3:stylus_id.index("\\t[")]
# print(touch_id)
# print(stylus_id)
top = tkinter.Tk()
top.title("")
top.geometry("140x150")
top.resizable(0,0)

def EN_TOUCH():
    os.system(ENA + touch_id)
def DIS_TOUCH():
    os.system(DIS + touch_id)
def EN_PEN():
    os.system(ENA + stylus_id)
def DIS_PEN():
    os.system(DIS + stylus_id)
def FLAMESHOT():
    os.system("flameshot gui")


enable_touch = tkinter.Button(top, text="Enable Touch", command=EN_TOUCH)
disable_touch = tkinter.Button(top, text="Disable Touch", command=DIS_TOUCH)
enable_pen = tkinter.Button(top, text="Enable Pen", command=EN_PEN)
disable_pen = tkinter.Button(top, text="Disable Pen", command=DIS_PEN)
flameshot = tkinter.Button(top, text="Flameshot", command=FLAMESHOT)

enable_touch.pack()
disable_touch.pack()
enable_pen.pack()
disable_pen.pack()
flameshot.pack()

top.mainloop()
