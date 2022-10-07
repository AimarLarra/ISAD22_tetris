import tkinter as tk
from tkinter import *
from tkinter import ttk

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
        entry = Entry(self.window, width=30, textvariable=erab2)
        entry.pack()

        Label(text="Pasahitza berria: ").pack()

        pasa2 = StringVar()
        entry2 = Entry(self.window, width=30, show="*", textvariable=pasa2)
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
            if erab.get() and pasa.get() and erab2.get() and pasa2.get():
                file = open("erabiltzaile_zerrenda", "r")
                aurkitua = False
                for i in file:
                    a, b = i.split(",")
                    b = b.strip()
                    if (a == erab.get() and b == pasa.get()):
                        aurkitua = True
                        #borrarlos
                if aurkitua:
                    file.close()
                    file = open("erabiltzaile_zerrenda", "a")
                    file.write("\n" + erab.get() + "," + pasa.get())
                    file.close()
                    self.window.destroy()
                    ml.MenuLeioa()
            else:
                popupmsg("Daturen bat hutsik dago!")

        buttonAldatu = tk.Button(self.window, text="ALDATU", command=clickEgin1)
        buttonAldatu.pack()

        self.window.mainloop()