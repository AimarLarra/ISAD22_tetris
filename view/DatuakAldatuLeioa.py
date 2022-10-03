import tkinter as tk
from tkinter import *

class DatuakAldatuLeioa(object):

    def __init__(self):
        super(DatuakAldatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")


        buttonErraza = tk.Button(self.window, text="ALDATU", command=self.clickEgin1)
        buttonErraza.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()