import tkinter as tk
from tkinter import *
from tkinter import ttk
from controller.DatuBasea import datuBasea
from PIL import Image, ImageTk
import view.RankingMenu as rM


class RankingGlobalaLeioa(object):

    def __init__(self):
        super(RankingGlobalaLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")
        db = datuBasea()
        datuak = db.getRankingGlobala()

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)

        img = Image.open("media/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)

        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        Label(text="Ranking pertsonala: ", bg="black", fg="white").place(x=20, rely=0.2, width=180)

        frame2 = tk.Frame(self.window, width=120, height=200)
        frame2.place(x=10, rely=0.30, width=200)

        scrollbar = ttk.Scrollbar(frame2, orient='vertical')
        scrollbar.pack(side=RIGHT, fill=Y)

        myList = Listbox(frame2, yscrollcommand=scrollbar.set)

        for partida in range(len(datuak)):
            myList.insert(END, " " + str(datuak[partida][1]) + " erabiltzailea " + str(datuak[partida][0]) + ". partidan " + str(datuak[partida][2]) + " puntuazioa lortu du, " + str(datuak[partida][3]) + " zailtasunean.")

        myList.pack(anchor=W, expand=YES, side=LEFT, fill=BOTH)
        scrollbar.config(command=myList.yview)

        def itzuli():
            self.window.destroy()
            rM.RankingMenu()

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=itzuli)
        buttonItzuli.place(x=10, y=420, height=30, width=50)

        self.window.mainloop()