import tkinter as tk
import view.ZailtasunLeioa as zL
import view.DatuakAldatuLeioa as dAL
import view.HasieraLeioa as hL
import view.ErabEzabatuLeioa as eEL
import view.JokatuKargatuLeioa as jKL
from controller.DatuBasea import datuBasea
import view.PertsonalizazioLeioa as pL
from PIL import ImageTk, Image
from pygame import mixer


class MenuLeioa(object):

    def __init__(self):
        super(MenuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")
        db = datuBasea()
        mixer.init()
        musika = db.getMusika(db.getUnekoa())
        print(musika)
        if musika == "BaxuGogorra":
            print("hola")
        if musika == " Klasikoa":
            print("Klasikoa")
            mixer.music.load("Irudiak/Klasikoa.mp3")
            mixer.music.play(loops=-1)
        if musika == " Kunbia":
            print("Kunbia")
            mixer.music.load("Irudiak/Kunbia.mp3")
            mixer.music.play(loops=-1)
        if musika == " Regetoia":
            print("Regetoia")
            mixer.music.load("Irudiak/Regetoia.mp3")
            mixer.music.play(loops=-1)
        if musika == " Metal":
            print("Metal")
            mixer.music.load("Irudiak/Metala.mp3")
            mixer.music.play(loops=-1)
        if musika == " BaxuGogorra":
            print("Baxugogor")
            mixer.music.load("Irudiak/BaxuGogorra.mp3")
            mixer.music.play(loops=-1)
        if musika == " Txalaparta":
            print("Txalaparta")
            mixer.music.load("Irudiak/Txalaparta.mp3")
            mixer.music.play(loops=-1)

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)
        img = Image.open("Irudiak/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)
        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        tk.Label(text="Lehenetsitako zailtasuna ertaina da", bg="black", fg="white").place(x=12, rely=0.45)

        buttonJolastu = tk.Button(self.window, text="JOLASTU", command=self.clickEgin1)
        buttonJolastu.place(x=15, rely=0.25, width=180)

        buttonZailtasuna = tk.Button(self.window, text="ZAILTASUNA", command=self.clickEgin2)
        buttonZailtasuna.place(x=15, rely=0.40, width=180)

        buttonDatuakAldatu = tk.Button(self.window, text="DATUAK ALDATU", command=self.clickEgin3)
        buttonDatuakAldatu.place(x=15, rely=0.55, width=180)

        if db.getAdmin(db.getUnekoa()):
            buttonErabEzabatu = tk.Button(self.window, text="ERABILTZAILEAK EZABATU", command=self.clickEgin5)
            buttonErabEzabatu.place(x=15, rely=0.80, width=180)

        buttonPertsonalizazioa = tk.Button(self.window, text="PERTSONALIZAZIOA", command=self.clickEgin6)
        buttonPertsonalizazioa.place(x=15, rely=0.70, width=180)

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=self.clickEgin4)
        buttonItzuli.place(x=10, rely=0.90, width=70)
        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        jKL.JokatuKargatuLeioa()

    def clickEgin2(self):
        self.window.destroy()
        zL.ZailtasunLeioa()

    def clickEgin3(self):
        self.window.destroy()
        dAL.DatuakAldatuLeioa()

    def clickEgin4(self):
        db = datuBasea()
        db.setUnekoa(db.getUnekoa(), "Ez")
        self.window.destroy()
        hL.HasieraLeioa()

    def clickEgin5(self):
        self.window.destroy()
        eEL.ErabEzabatuLeioa()

    def clickEgin6(self):
        self.window.destroy()
        pL.PertsonalizazioLeioa()
