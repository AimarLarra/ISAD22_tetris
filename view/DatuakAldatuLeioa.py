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
                #Mirar si el nuevo usuario existe.
                file = open("erabiltzaile_zerrenda", "r")
                for k in file:
                    e, f = k.split(",")
                    if (e == erab2.get()):
                        popupmsg("Erabiltzaile hori erregistratuta dago!")
                        break
                file.close()
                file = open("erabiltzaile_zerrenda", "r")
                file2 = open("erabiltzaile-zerrenda2", "w")
                lehena=TRUE
                ezdago=TRUE
                for i in file:
                    a, b = i.split(",")
                    b = b.strip()
                    if (a != erab.get() or b != pasa.get()):
                        if (lehena):
                            file2.write( a + "," + b)
                            lehena=FALSE
                        else:
                            file2.write("\n" +  a + "," + b)
                    else:
                        if(lehena):
                            file2.write(erab2.get() + "," + pasa2.get())
                            lehena=FALSE
                            ezdago=FALSE
                        else:
                            file2.write("\n" + erab2.get() + "," + pasa2.get())
                            ezdago=FALSE
                file.close()
                file2.close()
                file = open("erabiltzaile_zerrenda", "w")
                file2 = open("erabiltzaile-zerrenda2", "r")
                lehena = TRUE
                for j in file2:
                    c, d = j.split(",")
                    d = d.strip()
                    if lehena:
                        file.write(c + "," + d )
                        lehena=FALSE
                    else:
                        file.write("\n" + c + "," + d )
                file2.close()
                file.close()
                popupmsg("Erabiltzaile edo pasahitza txarto daude.")
            else:
                popupmsg("Daturen bat hutsik dago!")

        def clickEgin2():
            self.window.destroy()
            ml.MenuLeioa()

        buttonAldatu = tk.Button(self.window, text="ALDATU", command=clickEgin1)
        buttonAldatu.pack()

        buttonItzuli= tk.Button(self.window, text="ITZULI", command=clickEgin2)
        buttonItzuli.pack()

        self.window.mainloop()