import random
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
from PIL import Image, ImageTk
import view.MenuLeioa as mL
from controller.DatuBasea import datuBasea
import pickle
from pygame import mixer


class JokatuLeioa(object):
	"""docstring for JokatuLeioa"""

	def __init__(self, pZailtasuna, partidaJarraitu, tamaina):
		db = datuBasea()
		mixer.init()
		musika = db.getMusika(db.getUnekoa())
		if musika == " Klasikoa":
			mixer.music.load("media/Klasikoa.mp3")
			mixer.music.play(loops=-1)
		if musika == " Kunbia":
			mixer.music.load("media/Kunbia.mp3")
			mixer.music.play(loops=-1)
		if musika == " Zulagailua":
			mixer.music.load("media/Zulagailua.mp3")
			mixer.music.play(loops=-1)
		if musika == " Metala":
			mixer.music.load("media/Metala.mp3")
			mixer.music.play(loops=-1)
		if musika == " BaxuGogorra":
			mixer.music.load("media/BaxuGogorra.mp3")
			mixer.music.play(loops=-1)
		if musika == " Txalaparta":
			mixer.music.load("media/Txalaparta.mp3")
			mixer.music.play(loops=-1)

		atzekoKolorea = db.getKolorea(db.getUnekoa())
		if atzekoKolorea == ' Gorria':
			atzekoKolorea = "Red"
		elif atzekoKolorea == ' Horia':
			atzekoKolorea = "Yellow"
		elif atzekoKolorea == ' Morea':
			atzekoKolorea = "Purple"
		elif atzekoKolorea == ' Larrosa':
			atzekoKolorea = "Pink"
		elif atzekoKolorea == ' Urdina':
			atzekoKolorea = "Blue"
		elif atzekoKolorea == ' Zuria':
			atzekoKolorea = "White"
		elif atzekoKolorea == ' Berdea':
			atzekoKolorea = "Green"
		elif atzekoKolorea == ' Laranja':
			atzekoKolorea = "Orange"
		else:
			atzekoKolorea = "Black"
		super(JokatuLeioa, self).__init__()
		self.window = tk.Tk()
		self.window.geometry('260x600')
		self.window.title("Tetris jokoa")
		self.window.config(bg=atzekoKolorea)

		frame = tk.Frame(self.window, width=1, height=1, bg=atzekoKolorea)
		frame.place(x=1, rely=0.01)

		img = Image.open("media/tetris-logo.png")
		resize_img = img.resize((60, 40))
		img = ImageTk.PhotoImage(resize_img)

		label = tk.Label(frame, image=img, fg=atzekoKolorea, bg=atzekoKolorea, width=80, height=60)
		label.pack()

		button = tk.Button(self.window, text="Partida hasi")
		button.pack()

		buttonGorde = tk.Button(self.window, text="Partida gorde")
		buttonGorde.pack()

		def itzuli():
			self.window.destroy()
			mL.MenuLeioa()

		buttonItzuli = tk.Button(self.window, text="Menura itzuli", command=itzuli)
		buttonItzuli.pack()

		puntuazioa = tk.StringVar()
		puntuazioa.set("Puntuazioa: 0")

		puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa)
		puntuazioalabel.pack()

		canvas = TableroaPanela(master=self.window, puntuazioalabel=puntuazioa, zailtasuna=pZailtasuna, parJarraitu=partidaJarraitu, tamaina=tamaina)
		button.configure(command=canvas.jolastu)
		buttonGorde.configure(command=canvas.partidaGorde)
		canvas.pack()
		self.window.bind("<Up>", canvas.joku_kontrola)
		self.window.bind("<Down>", canvas.joku_kontrola)
		self.window.bind("<Right>", canvas.joku_kontrola)
		self.window.bind("<Left>", canvas.joku_kontrola)

		self.window.mainloop()


class TableroaPanela(tk.Frame):

	def __init__(self, gelazka_tamaina=20, puntuazioalabel=None, master=None, zailtasuna=None, parJarraitu=None, tamaina=None):
		tk.Frame.__init__(self, master)
		self.tamaina = tamaina
		self.puntuazio_panela = puntuazioalabel
		self.partidaJarraitu = parJarraitu
		self.gelazka_tamaina = gelazka_tamaina
		self.zailtasuna = zailtasuna
		db = datuBasea()
		db.taulaSortuPartida()
		zailtasunadb = db.getZailtasuna(db.getUnekoa())
		if zailtasunadb is not None:
			self.zailtasuna = zailtasunadb[0]

		self.canvas = tk.Canvas(
			width=self.tamaina[0] * self.gelazka_tamaina+1,
			height=self.tamaina[1] * self.gelazka_tamaina+1,
			bg='#eee', borderwidth=0, highlightthickness=0
		)
		self.canvas.pack(expand=tk.YES, fill=None)

		self.tab = Tableroa(self.partidaJarraitu, self.tamaina)
		if self.partidaJarraitu:
			self.jolastu()
		self.jokatzen = None
		self.tableroa_ezabatu()

	def marratu_gelazka(self, x, y, color):
		self.canvas.create_rectangle(x*self.gelazka_tamaina, y*self.gelazka_tamaina,
									(x+1)*self.gelazka_tamaina, (y+1)*self.gelazka_tamaina, fill=color)

	def tableroa_ezabatu(self):
		self.canvas.delete("all")
		self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina, self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

	def marraztu_tableroa(self):
		self.tableroa_ezabatu()
		for i in range(self.tab.tamaina[1]):
			for j in range(self.tab.tamaina[0]):
				if self.tab.tab[i][j]:
					self.marratu_gelazka(j, i, self.tab.tab[i][j])
		if self.tab.pieza:
			for i in range(4):
				x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
				y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
				self.marratu_gelazka(y, x, self.tab.pieza.get_kolorea())
		self.puntuazioa_eguneratu()

	def pausu_bat(self):
		try:
			self.tab.betetako_lerroak_ezabatu()
			self.tab.mugitu_behera()
		except Exception as error:
			try:
				self.tab.pieza_finkotu(self.tab.posizioa)
				pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
				self.tab.sartu_pieza(random.choice(pieza_posibleak)())
			except Exception as e:
				db = datuBasea()
				db.taulaSortuRanking()
				unekoa = db.getUnekoa()
				partZenb = db.getNextId(db.getUnekoa())
				if partZenb[0] is None:
					db.gordeRanking(unekoa, str(1), str(self.zailtasuna), str(self.tab.puntuazioa))
				else:
					db.gordeRanking(unekoa, str(partZenb[0] + 1), str(self.zailtasuna), str(self.tab.puntuazioa))
					partKop = db.getZenbatPartida(unekoa, str(self.zailtasuna))
					print(partKop[0])
					db.taulaSortuSaria()
					if partKop[0] == 10:
						db.gordeSaria("10 partidaJokatu", unekoa, str(self.zailtasuna))
					elif partKop[0] == 100:
						db.gordeSaria("100 partidaJokatu", unekoa, str(self.zailtasuna))
				if 10000 <= self.tab.puntuazioa < 100000:
					db.gordeSaria("10000-ko puntuazioa", unekoa, "")
				elif 100000 <= self.tab.puntuazioa < 1000000:
					db.gordeSaria("100000-ko puntuazioa", unekoa, "")
				elif 1000000 <= self.tab.puntuazioa:
					db.gordeSaria("1000000-ko puntuazioa", unekoa, "")
				print("GAMEOVER")
				self.tab.hasieratu_tableroa()
				return
		if self.tamaina[0] == 11:
			self.jokatzen = self.after(400, self.pausu_bat)
		elif self.tamaina[0] == 10:
			self.jokatzen = self.after(200, self.pausu_bat)
		else:
			self.jokatzen = self.after(100, self.pausu_bat)
		self.marraztu_tableroa()

	def puntuazioa_eguneratu(self):
		if self.puntuazio_panela:
			self.puntuazio_panela.set(f"Puntuazioa: {self.tab.puntuazioa}")

	def joku_kontrola(self, event):
		try:
			if event.keysym == 'Up':
				self.tab.biratu_pieza()
			if event.keysym == 'Down':
				self.tab.pieza_kokatu_behean()
			if event.keysym == 'Right':
				self.tab.mugitu_eskumara()
			if event.keysym == 'Left':
				self.tab.mugitu_ezkerrera()
		except Exception as error:
			pass
		finally:
			self.marraztu_tableroa()

	def jolastu(self):
		if not self.partidaJarraitu:
			if self.jokatzen:
				self.after_cancel(self.jokatzen)
			self.tab.hasieratu_tableroa()
		pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
		self.tab.sartu_pieza(random.choice(pieza_posibleak)())
		self.marraztu_tableroa()
		if self.tamaina[0] == 11:
			self.jokatzen = self.after(400, self.pausu_bat)
		elif self.tamaina[0] == 10:
			self.jokatzen = self.after(200, self.pausu_bat)
		else:
			self.jokatzen = self.after(100, self.pausu_bat)

	def partidaGorde(self):
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
			gordetakoPartida = [[None for x in range(self.tab.tamaina[0])]for y in range(self.tab.tamaina[1])]
			for i in range(self.tab.tamaina[1]):
				for j in range(self.tab.tamaina[0]):
					if self.tab.tab[i][j] is not None:
						gordetakoPartida[i][j] = self.tab.tab[i][j]
			zerrenda = pickle.dumps(gordetakoPartida)
			puntuaziopartida = self.tab.puntuazioa
			db = datuBasea()
			db.taulaSortuPartida()
			db.partidaGorde(db.getUnekoa(), zerrenda, str(self.zailtasuna), puntuaziopartida, self.tab.tamaina[0], self.tab.tamaina[1])
			self.master.destroy()
			mL.MenuLeioa()
