from tkinter import*
import random
import time

root= Tk()
root.geometry("1600x800+0+0")
root.title('Restaurant Management Systems')

Tops = Frame(root, width=1600, height=50, bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

fi = Frame(root, width=800, height= 700, bg="powder blue",relief=SUNKEN)
fi.pack(side=LEFT)

f2 = Frame(root, width=300, height= 700, bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

root.mainloop()