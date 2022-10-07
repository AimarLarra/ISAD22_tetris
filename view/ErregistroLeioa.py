import tkinter as tk
from tkinter import *
from tkinter import ttk

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

        erab = StringVar()
        entry = Entry(self.window, width=30, textvariable=erab)
        entry.pack()

        Label(text = "Pasahitza: ").pack()

        pasa=StringVar()
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

        def clickEgin():
            if erab.get():
                if pasa.get():
                    file = open("erabiltzaile_zerrenda", "r")
                    aurkitua = False
                    for i in file:
                        a, b = i.split(",")
                        b = b.strip()
                        if (a == erab.get()):
                            print("Erabiltzaile hori jada existitzen da!")
                            aurkitua = True
                            popupmsg("Erabiltzaile hori erregistratuta dago!")
                            break
                    if not aurkitua:
                        file.close()
                        file = open("erabiltzaile_zerrenda", "a")
                        file.write("\n" + erab.get() + "," + pasa.get())
                        file.close()
                        self.window.destroy()
                        hl.HasieraLeioa()
                else:
                    popupmsg("Pasahitza sartu!")
            else:
                popupmsg("Erabiltzailea sartu!")


        buttonSaioaHasi = tk.Button(self.window, text="ERREGISTRATU", command=clickEgin)
        buttonSaioaHasi.pack()

        self.window.mainloop()
