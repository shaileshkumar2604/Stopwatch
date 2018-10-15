from tkinter import *
import time

#main function
def Main():

    root = Tk()
    root.title("Stopwatch")
    height = 180
    width = 420
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sh/2) - (height/2)
    y = (sw/2) - (width/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)

    Bottom = Frame(root)
    Bottom.pack(side=BOTTOM)

    Start = Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)

    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)

    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)

    Exit = Button(Bottom, text='Close', command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=LEFT)

    root.config(bg="grey")
    root.mainloop()

class StopWatch(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.startT = 0.0
        self.nextT = 0.0
        self.Run = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="red", bg="black")
        self.SetTime(self.nextT)
        timeText.pack(expand = YES ,pady=2, padx=2)

    def Updater(self):
        self.nextT = time.time() - self.startT
        self.SetTime(self.nextT)
        self.timer = self.after(60, self.Updater)

    def SetTime(self, nextElap):
        hours = int(nextElap / 60 / 60.0)
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d:%02d' % (hours ,minutes, seconds, miliSeconds))

    def Start(self):
        if not self.Run:
            self.startT = time.time() - self.nextT
            self.Updater()
            self.Run = 1

    def Stop(self):
        if self.Run:
            self.after_cancel(self.timer)
            self.nextT = time.time() - self.startT
            self.SetTime(self.nextT)
            self.Run = 0

    def Exit(self):
        exit()

    def Reset(self):
        self.startT = time.time()
        self.nextT = 0.0
        self.SetTime(self.nextT)

Main()
