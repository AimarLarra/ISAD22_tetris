import tkinter as tk
from tkinter import *
from tkinter import ttk
from controller.DatuBasea import datuBasea
from PIL import Image, ImageTk
import view.RankingMenu as rM


class sariLeioa(object):

    def __init__(self):
        super(sariLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('220x460')
        self.window.title("Tetris jokoa")
        self.window.config(bg="black")
        db = datuBasea()
        datuak = db.getSaria(db.getUnekoa())

        frame = tk.Frame(self.window, width=1, height=1, bg="black")
        frame.place(x=1, rely=0.01)

        img = Image.open("media/tetris-logo.png")
        resize_img = img.resize((60, 40))
        img = ImageTk.PhotoImage(resize_img)

        label = tk.Label(frame, image=img, fg="black", bg="black", width=80, height=60)
        label.pack()

        Label(text="Sariak: ", bg="black", fg="white").place(x=20, rely=0.1, width=180)

        frame2 = tk.Frame(self.window, width=120, height=400, bg="black")
        frame2.place(x=10, rely=0.15, width=200)

        if len(datuak) == 0:
            Label(text="Ez ditu saririk lortu oraindik.", bg="black", fg="white").place(x=20, rely=0.4, width=180)
        else:
            for partida in range(len(datuak)):
                print(datuak[partida][0])
                print(datuak[partida][2])

                if datuak[partida][0] == "10 partidaJokatu":
                    if datuak[partida][2] == "0":
                        img2 = Image.open("media/trofeoEB-removebg-preview.png")
                        resize_img2 = img2.resize((60, 40))
                        img2 = ImageTk.PhotoImage(resize_img2)
                        label2 = tk.Label(frame2, image=img2, fg="black", bg="black", width=80, height=60)
                        label2.place(x=15, y=0)
                        Label(text="10 joko errazan", bg="black", fg="white").place(x=15, y=120, width=80)
                    elif datuak[partida][2] == "1":
                        img3 = Image.open("media/MedallaE2-removebg-preview.png")
                        resize_img3 = img3.resize((60, 40))
                        img3 = ImageTk.PhotoImage(resize_img3)
                        label3 = tk.Label(frame2, image=img3, fg="black", bg="black", width=80, height=60)
                        label3.place(x=95, y=0)
                        Label(text="10 joko ertainan", bg="black", fg="white").place(x=95, y=120, width=120)
                    elif datuak[partida][2] == "2":
                        img4 = Image.open("media/MedallaOro.png")
                        resize_img4 = img4.resize((60, 40))
                        img4 = ImageTk.PhotoImage(resize_img4)
                        label4 = tk.Label(frame2, image=img4, fg="black", bg="black", width=80, height=60)
                        label4.place(x=15, y=60)
                        Label(text="10 joko zailan", bg="black", fg="white").place(x=15, y=180, width=90)
                if datuak[partida][0] == "100 partidaJokatu":
                    if datuak[partida][2] == "0":
                        img8 = Image.open("media/trofeoEB-removebg-preview.png")
                        resize_img8 = img8.resize((60, 40))
                        img8 = ImageTk.PhotoImage(resize_img8)
                        label8 = tk.Label(frame2, image=img8, fg="black", bg="black", width=80, height=60)
                        label8.place(x=95, y=60)
                        Label(text="100 joko errazan ", bg="black", fg="white").place(x=95, y=180, width=120)
                    elif datuak[partida][2] == "1":
                        img9 = Image.open("media/MedallaE2-removebg-preview.png")
                        resize_img9 = img9.resize((60, 40))
                        img9 = ImageTk.PhotoImage(resize_img9)
                        label9 = tk.Label(frame2, image=img9, fg="black", bg="black", width=80, height=60)
                        label9.place(x=15, y=120)
                        Label(text="100 joko ertainan ", bg="black", fg="white").place(x=5, y=240, width=120)
                    elif datuak[partida][2] == "2":
                        img0 = Image.open("media/MedallaOro.png")
                        resize_img0 = img0.resize((60, 40))
                        img0 = ImageTk.PhotoImage(resize_img0)
                        label0 = tk.Label(frame2, image=img0, fg="black", bg="black", width=80, height=60)
                        label0.place(x=95, y=120)
                        Label(text="100 joko zailan ", bg="black", fg="white").place(x=115, y=240, width=90)
                elif datuak[partida][0] == "10000-ko puntuazioa":
                    img5 = Image.open("media/trofeoEB-removebg-preview.png")
                    resize_img5 = img5.resize((60, 40))
                    img5 = ImageTk.PhotoImage(resize_img5)
                    label5 = tk.Label(frame2, image=img5, fg="black", bg="black", width=80, height=60)
                    label5.place(x=15, y=190)
                    Label(text="10000 puntu ", bg="black", fg="white").place(x=5, y=310, width=120)
                elif datuak[partida][0] == "100000-ko puntuazioa":
                    img6 = Image.open("media/MedallaE2-removebg-preview.png")
                    resize_img6 = img6.resize((60, 40))
                    img6 = ImageTk.PhotoImage(resize_img6)
                    label6 = tk.Label(frame2, image=img6, fg="black", bg="black", width=80, height=60)
                    label6.place(x=95, y=190)
                    Label(text="100000 puntu ", bg="black", fg="white").place(x=95, y=310, width=120)
                elif datuak[partida][0] == "1000000-ko puntuazioa":
                    img7 = Image.open("media/MedallaOro.png")
                    resize_img7 = img7.resize((60, 40))
                    img7 = ImageTk.PhotoImage(resize_img7)
                    label7 = tk.Label(frame2, image=img7, fg="black", bg="black", width=80, height=60)
                    label7.place(x=60, y=260)
                    Label(text="1000000 puntu ", bg="black", fg="white").place(x=60, y=380, width=120)

        def itzuli():
            self.window.destroy()
            rM.RankingMenu()

        buttonItzuli = tk.Button(self.window, text="ITZULI", command=itzuli)
        buttonItzuli.place(x=10, y=420, height=30, width=50)

        self.window.mainloop()
