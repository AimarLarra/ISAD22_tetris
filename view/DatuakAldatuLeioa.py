import tkinter as tk
from tkinter import *
import view.MenuLeioa as ml

class DatuakAldatuLeioa(object):

    def __init__(self):
        super(DatuakAldatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        Label(text="Aldatu izena: ").pack()

        entry = tk.Entry()
        entry.pack()

        Label(text="Aldatu pasahitza: ").pack()

        entry2 = tk.Entry(show="*")
        entry2.pack()

        buttonAldatu = tk.Button(self.window, text="ALDATU", command=self.clickEgin1)
        buttonAldatu.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        ml.MenuLeioa()