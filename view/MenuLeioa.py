import tkinter as tk
import view.JokatuLeioa as jl
import view.ZailtasunLeioa as zl
import view.DatuakAldatuLeioa as dal

class MenuLeioa(object):

    def __init__(self):
        super(MenuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")


        buttonJolastu = tk.Button(self.window, text="JOLASTU", command=self.clickEgin1)
        buttonJolastu.pack()
        buttonZailtasuna = tk.Button(self.window, text="ZAILTASUNA", command=self.clickEgin2)
        buttonZailtasuna.pack()
        buttonDatuakAldatu = tk.Button(self.window, text="DATUAK ALDATU", command=self.clickEgin3)
        buttonDatuakAldatu.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        jl.JokatuLeioa()

    def clickEgin2(self):
        self.window.destroy()
        zl.ZailtasunLeioa()

    def clickEgin3(self):
        self.window.destroy()
        dal.DatuakAldatuLeioa()