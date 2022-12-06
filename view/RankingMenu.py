import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import view.MenuLeioa as mL
import view.RankingLeioa as rL
import view.RankingGlobalaLeioa as rGL


class RankingMenu(object):
    def __init__(self):
        super(RankingMenu, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)

        img = Image.open("media/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)

        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        def clickEgin1():
            self.window.destroy()
            rL.RankingLeioa()

        buttonRankingPertsonala = tk.Button(self.window, text="RANKING PERTSONALA", command=clickEgin1)
        buttonRankingPertsonala.place(x=15, rely=0.25, width=180)

        def clickEgin2():
            self.window.destroy()
            rGL.RankingGlobalaLeioa()


        buttonRankingGlobala = tk.Button(self.window, text="RANKING GLOBALA", command=clickEgin2)
        buttonRankingGlobala.place(x=15, rely=0.5, width=180)

        def clickEgin3():
            self.window.destroy()
            #MenuLeioa()

        buttonSariak = tk.Button(self.window, text="SARIAK", command=clickEgin3)
        buttonSariak.place(x=15, rely=0.75, width=180)

        def clickEgin4():
            self.window.destroy()
            mL.MenuLeioa()

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=clickEgin4)
        buttonItzuli.place(x=10, y=420, height=30, width=50)

        self.window.mainloop()
