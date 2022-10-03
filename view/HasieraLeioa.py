import tkinter as tk
from tkinter import *
from view.ErregistroLeioa import ErregistroLeioa
from view.SaioHasiLeioa import SaioHasiLeioa


class HasieraLeioa(object):

    def __init__(self):
        super(HasieraLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        buttonErregistro = tk.Button(self.window, text="ERREGISTRATU", command=self.clickEgin1)
        buttonErregistro.pack()

        buttonSaioaHasi = tk.Button(self.window, text="SAIOA HASI", command=self.clickEgin2)
        buttonSaioaHasi.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        ErregistroLeioa()

    def clickEgin2(self):
        self.window.destroy()
        SaioHasiLeioa()

