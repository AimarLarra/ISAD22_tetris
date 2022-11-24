import tkinter as tk
from tkinter import *
from tkinter import ttk
import controller.DatuBasea as dB
import view.MenuLeioa as mL
from PIL import Image, ImageTk
from pygame import mixer
from controller.DatuBasea import datuBasea


class PertsonalizazioLeioa(object):

    def __init__(self):
        super(PertsonalizazioLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)
        img = Image.open("Irudiak/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)
        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        tk.Label(text="Aukeratu atzeko kolorea", bg="black", fg="white").place(x=17, rely=0.15)

        boxKolorea = ttk.Combobox(self.window, state="readonly", textvariable=tk.StringVar())
        boxKolorea['values'] = (' Beltza',
                                ' Zuria',
                                ' Urdina',
                                ' Gorria',
                                ' Horia',
                                ' Berdea',
                                ' Larrosa',
                                ' Laranja',
                                ' Morea',)
        boxKolorea.place(x=20, rely=0.20, width=180)

        tk.Label(text="Aukeratu musika", bg="black", fg="white").place(x=17, rely=0.30)

        boxMusika = ttk.Combobox(self.window, state="readonly", textvariable=tk.StringVar())
        boxMusika['values'] = (' Klasikoa',
                               ' Kunbia',
                               ' Regetoia',
                               ' Metala',
                               ' BaxuGogorra',
                               ' Txalaparta')
        boxMusika.place(x=20, rely=0.35, width=180)

        tk.Label(text="Aukeratu adreilua", bg="black", fg="white").place(x=17, rely=0.45)

        boxAdreilua = ttk.Combobox(self.window, state="readonly", textvariable=tk.StringVar())
        boxAdreilua['values'] = (' Lforma',
                                 ' LformaAlderantzizko',
                                 ' Zforma',
                                 ' ZformaAlderantzizko',
                                 ' Zutabea',
                                 ' Laukia',
                                 ' Tforma')
        boxAdreilua.place(x=17, rely=0.50, width=180)

        tk.Label(text="Aukeratu adreiluaren kolorea", bg="black", fg="white").place(x=17, rely=0.60)

        boxAdrKolore = ttk.Combobox(self.window, state="readonly", textvariable=tk.StringVar())
        boxAdrKolore['values'] = (' Beltza',
                                  ' Zuria',
                                  ' Urdina',
                                  ' Gorria',
                                  ' Horia',
                                  ' Berdea',
                                  ' Larrosa',
                                  ' Laranja',
                                  ' Morea',)
        boxAdrKolore.place(x=17, rely=0.65, width=180)



        def clickEgin1():
            # no se va a cerrar cada vez que le demos a guardar.
            db = datuBasea()
            db.taulaSortuPertsonalizazioa()
            #db.pertsonalizazioaSortu(db.getUnekoa())
            mixer.init()
            db.pertsonalizazioaEguneratu(boxKolorea.get(), boxMusika.get(), boxAdreilua.get(), boxAdrKolore.get(), db.getUnekoa())
            label = tk.Label(text="Zure pertsonalizazioa gorde da", fg="white", bg="black").place(x=20, rely=0.7)
            # para el menu (musika=datuBasea.getMusika())
            #musika = db.getMusika(db.getUnekoa())
            musika=boxMusika.get()
            if musika==' Klasikoa':
                mixer.music.load("Irudiak/Klasikoa.mp3")
                mixer.music.play(loops=1)
            if musika==' Kunbia':
                mixer.music.load("Irudiak/Kunbia.mp3")
                mixer.music.play(loops=1)
            if musika == ' Regetoia':
                mixer.music.load("Irudiak/Regetoia.mp3")
                mixer.music.play(loops=1)
            if musika == ' Metala':
                mixer.music.load("Irudiak/Metala.mp3")
                mixer.music.play(loops=1)
            if musika == ' BaxuGogorra':
                mixer.music.load("Irudiak/BaxuGogorra.mp3")
                mixer.music.play(loops=1)
            if musika ==' Txalaparta':
                mixer.music.load("Irudiak/Txalaparta.mp3")
                mixer.music.play(loops=1)

        def clickEgin2():
            self.window.destroy()
            mL.MenuLeioa()

        buttonGorde = tk.Button(self.window, text="GORDE", command=clickEgin1)
        buttonGorde.place(x=15, rely=0.75, width=180)

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin2)
        buttonItzuli.place(x=15, rely=0.90, width=50)
        self.window.mainloop()

