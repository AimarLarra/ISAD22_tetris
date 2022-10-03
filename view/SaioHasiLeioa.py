import tkinter as tk
from tkinter import *
import view.HasieraLeioa as hl
from view.MenuLeioa import MenuLeioa

class SaioHasiLeioa(object):

    def __init__(self):
        super(SaioHasiLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        buttonSartu = tk.Button(self.window, text="SARTU", command=self.clickEgin1)
        buttonSartu.pack()

        buttonPasahitzaBerreskuratu = tk.Button(self.window, text="PASAHITZA BERRESKURATU", command=self.clickEgin2)
        buttonPasahitzaBerreskuratu.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        #Si la contraseña y el usuario estan bien
        MenuLeioa()

    def clickEgin2(self):
        self.window.destroy()
        #Una pantalla con la contraseña
        hl.HasieraLeioa()
