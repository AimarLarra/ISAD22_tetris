import tkinter as tk
from tkinter import *
from tkinter import ttk

import view.HasieraLeioa as hl
from view.MenuLeioa import MenuLeioa

class SaioHasiLeioa(object):

    def __init__(self):
        super(SaioHasiLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        Label(text="Sartu zure erabiltzaile eta pasahitza jolasten hasteko: ").pack()

        Label(text="Erabiltzailea: ").pack()

        erab = StringVar()
        entry = Entry(self.window, width=30, textvariable=erab)
        entry.pack()

        Label(text="Pasahitza: ").pack()

        pasa = StringVar()
        entry2 = Entry(self.window, width=30, show="*", textvariable=pasa)
        entry2.pack()

        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("Errorea!")
            label = ttk.Label(popup, text=msg)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        def clickEgin1():
            if erab.get():
                if pasa.get():
                    file = open("erabiltzaile_zerrenda", "r")
                    aurkitua = False
                    for i in file:
                        a, b = i.split(",")
                        b = b.strip()
                        if (a == erab.get() and b == pasa.get()):
                            print("Erabiltzaile hori zuzena da!")
                            aurkitua = True
                            self.window.destroy()
                            MenuLeioa()
                    if not aurkitua:
                        file.close()
                        popupmsg("Erabiltzaile edo pasahitza okerra!")
                else:
                    popupmsg("Pasahitza sartu!")
            else:
                popupmsg("Erabiltzailea sartu!")


        buttonSartu = tk.Button(self.window, text="SARTU", command=clickEgin1)
        buttonSartu.pack()

        def clickEgin2():
            if erab.get():
                file = open("erabiltzaile_zerrenda", "r")
                aurkitua = False
                for i in file:
                    a, b = i.split(",")
                    b = b.strip()
                    if (a == erab.get()):
                        popupmsg(b)
                popupmsg("Erabiltzaile hori ez dago erregistratuta.")
            else:
                popupmsg("Sartu erabiltzailea!")

        buttonPasahitzaBerreskuratu = tk.Button(self.window, text="PASAHITZA BERRESKURATU", command=clickEgin2)
        buttonPasahitzaBerreskuratu.pack()

        def clickEgin3():
            self.window.destroy()
            hl.HasieraLeioa()

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin3)
        buttonItzuli.pack()

        self.window.mainloop()