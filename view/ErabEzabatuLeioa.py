import tkinter as tk
from tkinter import *
from tkinter import ttk
from model.DatuBasea import datuBasea
from PIL import Image, ImageTk
import view.MenuLeioa as ml


class ErabEzabatuLeioa(object):

    def __init__(self):
        super(ErabEzabatuLeioa, self).__init__()
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

        ezabatuLabel = Label(text="Ezabatzeko erabiltzailea: ", bg="black", fg="white")
        ezabatuLabel.place(x=12, rely=0.35)
        erab = StringVar()
        entry = Entry(self.window, width=30, textvariable=erab)
        entry.place(x=15, rely=0.40)


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
            db.taulaSortu()
            if entry.get():
                if entry.get()!="admin":
                    emaitza = db.erabiltzaileaKonprobatu2(entry.get())
                    if emaitza:
                        db.erabiltzaileEzabatu(entry.get())
                        popupmsg("Erabiltzailea ezabatu da")
                    else:
                        popupmsg("Erabiltzaile hori ez da existitzen")
                else:
                    popupmsg("Ezin duzu administratzailea ezabatu!!")
            else:
                popupmsg("Datuak ondo sartu!")

            self.window.destroy()

            popupmsg("Erabiltzaile hori ez da existitzen")
            ml.MenuLeioa(1)

        def clickEgin2():
            self.window.destroy()
            ml.MenuLeioa(1)

        buttonAldatu = tk.Button(self.window, text="EZABATU", command=clickEgin1)
        buttonAldatu.place(x=15, rely=0.45)

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin2)
        buttonItzuli.place(x=10, rely=0.90)

        self.window.mainloop()
