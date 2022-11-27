import tkinter as tk
from tkinter import *
import view.ErregistroLeioa as eL
from view.SaioHasiLeioa import SaioHasiLeioa
from PIL import Image, ImageTk

class HasieraLeioa(object):

    def __init__(self):
        super(HasieraLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")


        frame = tk.Frame(self.window, width=1, height=20, bg="black")
        frame.place(x=12, rely=0.10)

        img = Image.open("media/tetris-logo.png")
        resize_img = img.resize((140, 100))
        img = ImageTk.PhotoImage(resize_img)

        label = tk.Label(frame, image=img, fg="black", bg="black", width=200, height=100)
        label.pack()

        tk.Label(text="Saioa hasi jolasten hasteko", bg="black", fg="white").place(x=17, rely=0.4)

        buttonSaioaHasi = tk.Button(self.window, text="SAIOA HASI", command=self.clickEgin2)
        buttonSaioaHasi.place(x=20, rely=0.45, width=180)

        tk.Label(text="Konturik ez baduzu erregistratu", bg="black", fg="white").place(x=17, rely=0.55)

        buttonErregistro = tk.Button(self.window, text="ERREGISTRATU", command=self.clickEgin1)
        buttonErregistro.place(x=20, rely=0.6, width=180)

        egileak = tk.Label(text="Egileak:  Aimar Larrazabal", bg="black", fg="white")
        egileak.place(relx=0.05, rely=0.85)
        egileak2 = tk.Label(text="Eneko Perez", bg="black", fg="white")
        egileak2.place(relx=0.25, rely=0.89)
        egileak3 = tk.Label(text="Eneko Basauri", bg="black", fg="white")
        egileak3.place(relx=0.25, rely=0.93)

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        eL.ErregistroLeioa()

    def clickEgin2(self):
        self.window.destroy()
        SaioHasiLeioa()
