import tkinter as tk
from tkinter import *
from tkinter import ttk
from controller.DatuBasea import datuBasea
from PIL import Image, ImageTk
import view.HasieraLeioa as hL


class ErregistroLeioa(object):

    def __init__(self):
        super(ErregistroLeioa, self).__init__()
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

        Label(text="Sartu erabiltzaile izena eta", bg="black", fg="white").place(x=20, rely=0.2, width=180)
        Label(text="pasahitza kontu bat sortzeko:", bg="black", fg="white").place(x=20, rely=0.25, width=180)

        Label(text="Erabiltzailea: ", bg="black", fg="white").place(x=20, rely=0.4, width=180)

        erab = StringVar()
        entry = Entry(self.window, textvariable=erab)
        entry.focus()
        entry.place(x=20, rely=0.45, width=180)

        Label(text="Pasahitza: ", bg="black", fg="white").place(x=20, rely=0.50, width=180)

        pasa = StringVar()
        entry2 = Entry(self.window, show="*", textvariable=pasa)
        entry2.place(x=20, rely=0.55, width=180)

        def popupmsg(msg):
            popup = tk.Tk()
            popup.wm_title("Errorea!")
            label2 = ttk.Label(popup, text=msg)
            label2.pack(side="top", fill="x", pady=10)
            b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            b1.pack()
            popup.mainloop()

        def clickegin():
            db = datuBasea()
            db.taulaSortu()
            if entry.get() and entry2.get():
                emaitza = db.erabiltzaileGehitu(entry.get(), entry2.get())
                if emaitza is False:
                    popupmsg("Erabiltzaile hori existitzen da, beste bat sartu!")
                #Crear la tabla de pertsonalizazio
                db.pertsonalizazioaSortu(entry.get())
                self.window.destroy()
                hL.HasieraLeioa()
            else:
                popupmsg("Datuak ondo sartu!")

        def clickegin3():
            self.window.destroy()
            hL.HasieraLeioa()

        buttonerregistratu = tk.Button(self.window, text="ERREGISTRATU", command=clickegin)
        buttonerregistratu.place(x=20, rely=0.60, width=180)

        buttonitzuli = tk.Button(self.window, text="ITZULI", command=clickegin3)
        buttonitzuli.place(x=10, y=420, height=30, width=50)

        self.window.mainloop()
