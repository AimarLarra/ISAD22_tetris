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

        buttonSaioaHasi = tk.Button(self.window, text="SAIOA HASI", command=self.clickEgin2)
        buttonSaioaHasi.place(x=20, rely=0.6, width= 180)

        buttonErregistro = tk.Button(self.window, text="ERREGISTRATU", command=self.clickEgin1)
        buttonErregistro.place(x=20, rely=0.4,width=180)

        egileak = tk.Label(text="Egileak:  Aimar Larrazabal",bg="black",fg="white")
        egileak.place(relx=0.05, rely=0.85)
        egileak2 = tk.Label(text="Eneko Perez", bg="black", fg="white")
        egileak2.place(relx=0.25, rely=0.89)
        egileak3 = tk.Label(text="Eneko Basauri", bg="black", fg="white")
        egileak3.place(relx=0.25, rely=0.93)

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        ErregistroLeioa()

    def clickEgin2(self):
        self.window.destroy()
        SaioHasiLeioa()

