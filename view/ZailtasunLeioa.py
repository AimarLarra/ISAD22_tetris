import tkinter as tk
import view.JokatuLeioa as jL
from PIL import Image, ImageTk


class ZailtasunLeioa(object):

    def __init__(self):
        super(ZailtasunLeioa, self).__init__()
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

        buttonErraza = tk.Button(self.window, text="ERRAZA", command=self.clickEgin1)
        buttonErraza.place(x=15, rely=0.35, width=180)
        buttonNormala = tk.Button(self.window, text="NORMALA", command=self.clickEgin2)
        buttonNormala.place(x=15, rely=0.50, width=180)
        buttonZaila = tk.Button(self.window, text="ZAILA", command=self.clickEgin3)
        buttonZaila.place(x=15, rely=0.65, width=180)

        self.window.mainloop()

    def clickEgin1(self):
        self.window.destroy()
        jL.JokatuLeioa(0, False, (11, 22))


    def clickEgin2(self):
        self.window.destroy()
        jL.JokatuLeioa(1, False, (10, 20))

    def clickEgin3(self):
        self.window.destroy()
        jL.JokatuLeioa(2, False, (9, 18))
