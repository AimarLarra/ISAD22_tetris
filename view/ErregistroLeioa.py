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

        Label(text="Sartu erabiltzaile izena eta",bg="black",fg="white").place(x=20,rely=0.2,width=180)
        Label(text="pasahitza kontu bat sortzeko:", bg="black", fg="white").place(x=20, rely=0.25,width=180)

        Label(text = "Erabiltzailea: ",bg="black",fg="white").place(x=20,rely=0.4,width=180)

        erab = StringVar()
        entry = Entry(self.window, textvariable=erab)
        entry.place(x=20,rely=0.45,width=180)

        Label(text = "Pasahitza: ", bg="black", fg="white").place(x=20,rely=0.50,width=180)

        pasa=StringVar()
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

        def clickEgin3():
            self.window.destroy()
            hl.HasieraLeioa()

        buttonErregistratu = tk.Button(self.window, text="ERREGISTRATU", command=clickEgin)
        buttonErregistratu.place(x=20,rely=0.60,width=180)

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin3)
        buttonItzuli.place(x=10,y=420,height=30,width=50)



        self.window.mainloop()
