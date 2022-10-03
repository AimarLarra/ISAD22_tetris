import tkinter as tk
import view.HasieraLeioa as hl


class ErregistroLeioa(object):

    def __init__(self):
        super(ErregistroLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        buttonSaioaHasi = tk.Button(self.window, text="ERREGISTRATU", command=self.clickEgin)
        buttonSaioaHasi.pack()

        self.window.mainloop()

    def clickEgin(self):
        self.window.destroy()
        hl.HasieraLeioa()

