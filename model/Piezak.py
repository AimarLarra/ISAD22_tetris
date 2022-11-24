from controller.DatuBasea import datuBasea
class Pieza:
	def __init__(self, forma, kolorea):
		self.forma = forma
		self.kolorea = kolorea

	def get_kolorea(self):
		return self.kolorea

	def get_x(self, i):
		return self.forma[i][0]

	def get_y(self, i):
		return self.forma[i][1]

	def set_x(self, i, b):
		self.forma[i][0] = b

	def set_y(self, i, b):
		self.forma[i][1] = b

	def biratuEzkerrera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, aurr_y)
			self.set_y(i, -aurr_x)

	def biratuEskuinera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, -aurr_y)
			self.set_y(i, aurr_x)

	def min_x(self):
		return min([x[0] for x in self.forma])

	def min_y(self):
		return min([x[1] for x in self.forma])


class Laukia(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("Laukia", db.getUnekoa())
		if piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		else:
			piezaKolorea = "Yellow"
		super(Laukia, self).__init__([[0,0],[0,1],[1,0],[1,1]], kolorea=piezaKolorea)


class Zutabea(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("Zutabea", db.getUnekoa())
		if piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Cyan"
		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea=piezaKolorea)



class Lforma(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("Lforma", db.getUnekoa())
		if piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Blue"
		super(Lforma, self).__init__([[-1, -1], [0, -1], [0, 0], [0, 1]], kolorea=piezaKolorea)


class LformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("LformaAlderantzizko", db.getUnekoa())
		if piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Orange"
		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea=piezaKolorea)


class Zforma(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("Zforma", db.getUnekoa())
		if piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Green"
		super(Zforma, self).__init__([[0, -1], [0, 0], [-1, 0], [-1, 1]], kolorea=piezaKolorea)


class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("ZformaAlderantzizko", db.getUnekoa())
		if piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Morea':
			piezaKolorea = "Purple"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Red"
		super(ZformaAlderantzizko, self).__init__([[0, -1], [0, 0], [1, 0], [1, 1]], kolorea=piezaKolorea)


class Tforma(Pieza):
	def __init__(self, kolorea=None):
		db = datuBasea()
		piezaKolorea = db.getAdreiluKolorea("Tforma", db.getUnekoa())
		if piezaKolorea == ' Berdea':
			piezaKolorea = "Green"
		elif piezaKolorea == ' Gorria':
			piezaKolorea = "Red"
		elif piezaKolorea == ' Larrosa':
			piezaKolorea = "Pink"
		elif piezaKolorea == ' Zian':
			piezaKolorea = "Cyan"
		elif piezaKolorea == ' Beltza':
			piezaKolorea = "Black"
		elif piezaKolorea == ' Zuria':
			piezaKolorea = "White"
		elif piezaKolorea == ' Laranja':
			piezaKolorea = "Orange"
		elif piezaKolorea == ' Urdina':
			piezaKolorea = "Blue"
		elif piezaKolorea == ' Horia':
			piezaKolorea = "Yellow"
		else:
			piezaKolorea = "Purple"
		super(Tforma, self).__init__([[-1, 0], [0, 0], [1, 0], [0, 1]], kolorea=piezaKolorea)


class LaukiForma(Pieza):
	def __init__(self, kolorea=None):
		super(LaukiForma, self).__init__([0, 0], kolorea='grey')