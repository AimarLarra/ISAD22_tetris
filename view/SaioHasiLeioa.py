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

        Label(text="Sartu zure erabiltzaile eta",bg="black",fg="white").place(x=20,rely=0.2,width=180)
        Label(text="pasahitza jolasten hasteko:",bg="black",fg="white").place(x=20,rely=0.25,width=180)

        Label(text="Erabiltzailea: ",bg="black",fg="white").place(x=20,rely=0.4,width=180)

        erab = StringVar()
        entry = Entry(self.window, textvariable=erab)
        entry.place(x=20,rely=0.45,width=180)

        Label(text="Pasahitza: ",bg="black",fg="white").place(x=20,rely=0.5,width=180)

        pasa = StringVar()
        entry2 = Entry(self.window, show="*", textvariable=pasa)
        entry2.place(x=20,rely=0.55,width=180)

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
        buttonSartu.place(x=20,rely=0.6,width=180)

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
        buttonPasahitzaBerreskuratu.place(x=20,rely=0.7,width=180)

        def clickEgin3():
            self.window.destroy()
            hl.HasieraLeioa()

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin3)
        buttonItzuli.place(x=10,y=420,height=30,width=50)

        self.window.mainloop()