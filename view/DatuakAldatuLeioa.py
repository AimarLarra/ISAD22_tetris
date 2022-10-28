import tkinter as tk
from tkinter import *
from tkinter import ttk
from Controller.DatuBasea import datuBasea
from PIL import Image,ImageTk
import view.MenuLeioa as ml


class DatuakAldatuLeioa(object):
    def __init__(self, admin):
        super(DatuakAldatuLeioa, self).__init__()
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

        erab1Label = Label(text="Aurreko erabiltzailea: ",  bg="black", fg="white")
        erab1Label.place(x=15, rely=0.30)

        erab = StringVar()
        entry = Entry(self.window, width=30, textvariable=erab)
        entry.place(x=15, rely=0.35)

        pasa1Label = Label(text="Aurreko pasahitza: ", bg="black", fg="white")
        pasa1Label.place(x=15, rely=0.40)

        pasa = StringVar()
        entry2 = Entry(self.window, width=30, show="*", textvariable=pasa)
        entry2.place(x=15, rely=0.45)

        erab2Label = Label(text="Erabiltzaile berria: ",  bg="black", fg="white")
        erab2Label.place(x=15, rely=0.50)

        erab2 = StringVar()
        entry3 = Entry(self.window, width=30, textvariable=erab2)
        entry3.place(x=15, rely=0.55)

        pasa2Label = Label(text="Pasahitza berria: ", bg="black", fg="white")
        pasa2Label.place(x=15, rely=0.60)

        pasa2 = StringVar()
        entry4 = Entry(self.window, width=30, show="*", textvariable=pasa2)
        entry4.place(x=15, rely=0.65)

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
                if entry.get()!="admin":
                    emaitza = db.erabiltzailearenDatuakEguneratu(entry.get(), entry2.get(), entry3.get(), entry4.get())
                    if emaitza:
                        # Si esta bien
                        self.window.destroy()
                        ml.MenuLeioa(0)
                    else:
                        popupmsg("Erabiltzailea edo pasahitza oker daude!")
                else:
                    popupmsg("Ezin dira administratzaile datuak aldatu!")
            else:
                popupmsg("Datuak ondo sartu!")

        def clickEgin1Admin():
            db = datuBasea()
            if entry.get() and entry2.get() and entry3.get() and entry4.get():
                if entry.get() != "admin":
                    emaitza = db.erabiltzailearenDatuakEguneratu(entry.get(), entry2.get(), entry3.get(), entry4.get())
                    if emaitza:
                        # Si esta bien
                        self.window.destroy()
                        ml.MenuLeioa(1)
                    else:
                        popupmsg("Erabiltzailea edo pasahitza oker daude!")
                else:
                    popupmsg("Ezin dira administratzaile datuak aldatu!")
            else:
                popupmsg("Datuak ondo sartu!")
        def clickEgin2():
            self.window.destroy()
            ml.MenuLeioa(0)

        def clickEgin2Admin():
            self.window.destroy()
            ml.MenuLeioa(1)



        if admin==1:
            buttonAldatu = tk.Button(self.window, text="ALDATU", command=clickEgin1Admin)
            buttonAldatu.place(x=15, rely=0.75)

            buttonItzuli= tk.Button(self.window, text="ITZULI", command=clickEgin2Admin)
            buttonItzuli.place(x=15, rely=0.90)
        else:
            buttonAldatu = tk.Button(self.window, text="ALDATU", command=clickEgin1)
            buttonAldatu.place(x=15, rely=0.75)

            buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin2)
            buttonItzuli.place(x=15, rely=0.90)
        self.window.mainloop()
