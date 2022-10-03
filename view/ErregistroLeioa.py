import tkinter as tk
from tkinter import *
import view.HasieraLeioa as hl


class ErregistroLeioa(object):

    def __init__(self):
        super(ErregistroLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        Label(text = "Sartu erabiltzaile eta pasahitza bat kontu berri bat sortzeko: ").pack()

        Label(text = "Erabiltzailea: ").pack()

        entry = tk.Entry()
        entry.pack()

        Label(text = "Pasahitza: ").pack()


        entry2 = tk.Entry(show="*")
        entry2.pack()

        buttonSaioaHasi = tk.Button(self.window, text="ERREGISTRATU", command=self.clickEgin)
        buttonSaioaHasi.pack()

        self.window.mainloop()

    def clickEgin(self):
        self.window.destroy()
        hl.HasieraLeioa()

