import tkinter as tk
import view.MenuLeioa as ml
class ZailtasunLeioa(object):

    def __init__(self):
        super(ZailtasunLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")

        buttonErraza = tk.Button(self.window, text="ERRAZA", command=self.clickEgin1)
        buttonErraza.pack()
        buttonNormala = tk.Button(self.window, text="NORMALA", command=self.clickEgin2)
        buttonNormala.pack()
        buttonZaila = tk.Button(self.window, text="ZAILA", command=self.clickEgin3)
        buttonZaila.pack()

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        ml.MenuLeioa()


    def clickEgin2(self):
        self.window.destroy()
        ml.MenuLeioa()

    def clickEgin3(self):
        self.window.destroy()
        ml.MenuLeioa()
