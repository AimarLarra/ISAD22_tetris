import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.DatuBasea import datuBasea

import view.MenuLeioa as ml

class DatuakAldatuLeioa(object):

    def __init__(self):
        super(DatuakAldatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        Label(text="Aurreko erabiltzailea: ").pack()

        erab = StringVar()
        entry = Entry(self.window, width=30, textvariable=erab)
        entry.pack()

        Label(text="Aurreko pasahitza: ").pack()

        pasa = StringVar()
        entry2 = Entry(self.window, width=30, show="*", textvariable=pasa)
        entry2.pack()

        Label(text="Erabiltzaile berria: ").pack()

        erab2 = StringVar()
        entry3 = Entry(self.window, width=30, textvariable=erab2)
        entry3.pack()

        Label(text="Pasahitza berria: ").pack()

        pasa2 = StringVar()
        entry4 = Entry(self.window, width=30, show="*", textvariable=pasa2)
        entry4.pack()

        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("Errorea!")
            label = ttk.Label(popup, text=msg)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack()
            popup.mainloop()

        def clickEgin1():
            db = datuBasea()
            if entry.get() and entry2.get() and entry3.get() and entry4.get():
                emaitza = db.erabiltzailearenDatuakEguneratu(entry.get(), entry2.get(), entry3.get(), entry4.get())
                if emaitza:
                    # Si esta bien
                    self.window.destroy()
                    ml.MenuLeioa()
                else:
                    popupmsg("Erabiltzailea edo pasahitza oker daude!")

            else:
                popupmsg("Datuak ondo sartu!")
                
        def clickEgin2():
            self.window.destroy()
            ml.MenuLeioa()

        buttonAldatu = tk.Button(self.window, text="ALDATU", command=clickEgin1)
        buttonAldatu.pack()

        buttonItzuli= tk.Button(self.window, text="ITZULI", command=clickEgin2)
        buttonItzuli.pack()

        self.window.mainloop()
