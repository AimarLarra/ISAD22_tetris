import tkinter as tk
import view.JokatuLeioa as jL
from Controller.DatuBasea import datuBasea
from PIL import ImageTk, Image

class JokatuKargatuLeioa(object):

    def __init__(self, pAdmin):
        super(JokatuKargatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")
        self.admin = pAdmin

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)
        img = Image.open("Irudiak/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)
        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        buttonBerria = tk.Button(self.window, text="PARTIDA BERRIA", command=self.clickEgin1)
        buttonBerria.place(x=15, rely=0.25, width=180)

        buttonKargatu = tk.Button(self.window, text="PARTIDA KARGATU", command=self.clickEgin2)
        buttonKargatu.place(x=15, rely=0.40, width=180)

    def clickEgin1(self):
        self.window.destroy()
        jL.JokatuLeioa(1, self.admin)


    def clickEgin2(self):
        db = datuBasea()
        file = open("unekoErab.txt", "r")
        zailtasuna = db.getZailtasuna(file.read())
        file.close()
        self.window.destroy()
        jL.JokatuLeioa(zailtasuna, self.admin)

