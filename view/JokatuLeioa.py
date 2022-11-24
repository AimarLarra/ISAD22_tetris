import random
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
from PIL import Image, ImageTk
import view.MenuLeioa as mL
from controller.DatuBasea import datuBasea
import pickle
tablerogordeta = []


class JokatuLeioa(object):
	"""docstring for JokatuLeioa"""

	def __init__(self, pZailtasuna):
		db = datuBasea()
		atzekoKolorea = db.getKolorea(db.getUnekoa())
		print(atzekoKolorea)
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
			atzekoKolorea ="White"
		elif atzekoKolorea == ' Berdea':
			atzekoKolorea = "Green"
		elif atzekoKolorea == ' Laranja':
			atzekoKolorea = "Orange"
		else:
			atzekoKolorea = "Black"
		print(atzekoKolorea)
		super(JokatuLeioa, self).__init__()
		self.window = tk.Tk()
		self.window.geometry('260x520')
		self.window.title("Tetris jokoa")
		self.window.config(bg=atzekoKolorea)

		frame = tk.Frame(self.window, width=1, height=1, bg=atzekoKolorea)
		frame.place(x=1, rely=0.01)

		img = Image.open("Irudiak/tetris-logo.png")
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

		canvas = TableroaPanela(master=self.window, puntuazioalabel=puntuazioa, zailtasuna=pZailtasuna)
		button.configure(command=canvas.jolastu)
		buttonGorde.configure(command=canvas.partidaGorde)
		canvas.pack()
		self.window.bind("<Up>", canvas.joku_kontrola)
		self.window.bind("<Down>", canvas.joku_kontrola)
		self.window.bind("<Right>", canvas.joku_kontrola)
		self.window.bind("<Left>", canvas.joku_kontrola)

		self.window.mainloop()

	def partida_jarraitu(self):
		global tablerogordeta
		db = datuBasea()
		puntuazioa = db.getPuntuazioa(db.getUnekoa())
		partidaZerrenda = db.partidaKargatu(db.getUnekoa())
		partida = pickle.loads(partidaZerrenda[0])
		tablerogordeta = partida
		tamaina = db.getZailtasuna(db.getUnekoa())
		JokatuLeioa(tamaina)

class TableroaPanela(tk.Frame):

	def __init__(self, gelazka_tamaina=20, puntuazioalabel=None, master=None, zailtasuna=None):
		tk.Frame.__init__(self, master)
		self.puntuazio_panela = puntuazioalabel
		if zailtasuna == 0:
			self.tamaina = (11, 22)
		elif zailtasuna == 1:
			self.tamaina = (10, 20)
		elif zailtasuna == 2:
			self.tamaina = (9, 18)

		self.gelazka_tamaina = gelazka_tamaina
		self.zailtasuna = zailtasuna

		self.canvas = tk.Canvas(
			width=self.tamaina[0] * self.gelazka_tamaina+1,
			height=self.tamaina[1] * self.gelazka_tamaina+1,
			bg='#eee', borderwidth=0, highlightthickness=0
		)
		self.canvas.pack(expand=tk.YES, fill=None)

		self.tab = Tableroa(zailtasuna)
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
				print("GAMEOVER")
				self.tab.hasieratu_tableroa()
				return
		if self.zailtasuna == 0:
			self.jokatzen = self.after(400, self.pausu_bat)
		elif self.zailtasuna == 1:
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
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
		self.tab.hasieratu_tableroa()
		pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
		self.tab.sartu_pieza(random.choice(pieza_posibleak)())
		self.marraztu_tableroa()
		if self.zailtasuna == 0:
			self.jokatzen = self.after(400, self.pausu_bat)
		elif self.zailtasuna == 1:
			self.jokatzen = self.after(200, self.pausu_bat)
		else:
			self.jokatzen = self.after(100, self.pausu_bat)

	def partidaGorde(self):
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
			gordetakoPartida = [[ None for x in range(self.tamaina[0])]for y in range(self.tamaina[1])]
			for i in range(self.tab.tamaina[1]):
				print("i", i)
				for j in range(self.tab.tamaina[0]):
					print("j", j)
					if self.tab.tab[i][j] is not None:
						gordetakoPartida[i][j] = self.tab.tab[i][j]
			zerrenda = pickle.dumps(gordetakoPartida)
			puntuaziopartida = self.tab.puntuazioa
			db = datuBasea()
			db.taulaSortuPartida()
			db.partidaGorde(db.getUnekoa(), zerrenda, str(self.zailtasuna), puntuaziopartida)
