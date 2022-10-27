import tkinter as tk
import view.JokatuLeioa as jl
import view.ZailtasunLeioa as zl
import view.DatuakAldatuLeioa as dal
import view.HasieraLeioa as hl
import view.ErabEzabatuLeioa as eel
from PIL import ImageTk,Image

class MenuLeioa(object):

    def __init__(self, admin):
        super(MenuLeioa, self).__init__()
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
        self.admin = admin

        tk.Label(text="Lehenetsitako zailtasuna ertaina da", bg="black", fg="white").place(x=12, rely=0.45)

        buttonJolastu = tk.Button(self.window, text="JOLASTU", command=self.clickEgin1)
        buttonJolastu.place(x=15, rely=0.25, width=180)

        buttonZailtasuna = tk.Button(self.window, text="ZAILTASUNA", command=self.clickEgin2)
        buttonZailtasuna.place(x=15, rely=0.40, width=180)

        if admin==1:
            buttonDatuakAldatu = tk.Button(self.window, text="DATUAK ALDATU", command=self.clickEgin3Admin)
            buttonDatuakAldatu.place(x=15, rely=0.55, width=180)

            buttonErabEzabatu = tk.Button(self.window, text="ERABILTZAILEAK EZABATU", command=self.clickEgin5)
            buttonErabEzabatu.place(x=15, rely=0.70, width=180)
        else:
            buttonDatuakAldatu = tk.Button(self.window, text="DATUAK ALDATU", command=self.clickEgin3)
            buttonDatuakAldatu.place(x=15, rely=0.55, width=180)



        buttonItzuli = tk.Button(self.window, text="ITZULI", command=self.clickEgin4)
        buttonItzuli.place(x=10, rely=0.90, width=70)
        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        jl.JokatuLeioa(1, 0)

    def clickEgin2(self):
        self.window.destroy()
        zl.ZailtasunLeioa(self.admin)

    def clickEgin3(self):
        self.window.destroy()
        dal.DatuakAldatuLeioa(0)

    def clickEgin3Admin(self):
        self.window.destroy()
        dal.DatuakAldatuLeioa(1)

    def clickEgin4(self):
        self.window.destroy()
        hl.HasieraLeioa()

    def clickEgin5(self):
        self.window.destroy()
        eel.ErabEzabatuLeioa()

