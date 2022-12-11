import sqlite3


class datuBasea:

    def __init__(self):
        print("...")

    def taulaSortu(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute("CREATE TABLE if not exists erregistroa (erabiltzailea varchar(20) NOT NULL, pasahitza varchar(20) NOT NULL, administratzailea varchar(3) DEFAULT NULL, unekoErab varchar(3) DEFAULT NULL, PRIMARY KEY (erabiltzailea));")
        con.commit()
        con.close()

    def taulaSortuPartida(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
            "CREATE TABLE if not exists partida (erabiltzailea varchar(20) NOT NULL, zerrenda BLOB, zailtasuna varchar(10), puntuazioa int(10), tam0 int(1), tam1 int(1), PRIMARY KEY (erabiltzailea));")
        con.commit()
        con.close()

    def taulaSortuPertsonalizazioa(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
        "CREATE TABLE if not exists pertsonalizazioa (erabiltzailea varchar(20) NOT NULL, atzekoKolorea varchar(40), musika varchar(20), Laukia varchar(20) DEFAULT 'yellow', Zutabea varchar(10) DEFAULT 'cyan', Lforma varchar(10) DEFAULT 'blue', LformaAlderantzizko varchar(10) DEFAULT 'orange', Zforma varchar(10) DEFAULT 'green', ZformaAlderantzizko varchar(10) DEFAULT 'red', Tforma varchar(10) DEFAULT 'purple', PRIMARY KEY(erabiltzailea));")
        con.commit()
        con.close()

    def taulaSortuRanking(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
            "CREATE TABLE if not exists ranking (id int NOT NULL, erabiltzailea varchar(20) NOT NULL, puntuazioa int(10), zailtasuna varchar(10), PRIMARY KEY(id, erabiltzailea), FOREIGN KEY(erabiltzailea) REFERENCES erregistroa(erabiltzailea) ON DELETE CASCADE);")
        con.commit()
        con.close()

    def taulaSortuSaria(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
            "CREATE TABLE if not exists saria (saria varchar(20) NOT NULL, erabiltzailea varchar(20) NOT NULL, zailtasuna varchar(20), FOREIGN KEY(erabiltzailea) REFERENCES erregistroa(erabiltzailea) ON DELETE CASCADE);")
        con.commit()
        con.close()

    def erabiltzaileGehitu(self, erabiltzailea, pasahitza):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("INSERT INTO erregistroa VALUES ('" + erabiltzailea + "', '" + pasahitza + "', 'Ez', 'Ez')")
            res.fetchall()
            con.commit()
            con.close()
            return True
        except sqlite3.IntegrityError:
            con.close()
            return False

    def initPertsonalizazioa(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute(
                "INSERT INTO pertsonalizazioa VALUES ('" + erabiltzailea + "', ' Beltza', '', ' Horia', ' Zian', ' Urdina', ' Laranja', ' Berdea', ' Gorria', ' Morea')")
            res.fetchall()
            con.commit()
            con.close()
            return True
        except sqlite3.IntegrityError:
            con.close()
            return False

    def erabiltzaileEzabatu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("DELETE FROM erregistroa WHERE erabiltzailea = '" + erabiltzailea + "'")
            res.fetchall()
            con.commit()
            con.close()
            return True
        except sqlite3.IntegrityError:
            con.close()
            return False

    def erabiltzailearenPasahitzaInprimatu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT pasahitza from erregistroa where erabiltzailea = '" + erabiltzailea + "'")
        datos = cur.fetchall()
        con.commit()
        con.close()
        return datos

    def erabiltzaileaKonprobatu(self, erabiltzailea, pasahitza):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM erregistroa WHERE erabiltzailea = '" + erabiltzailea + "' AND pasahitza = '" + pasahitza + "'")
        datuak = cur.fetchall()
        con.commit()
        con.close()
        return datuak

    def erabiltzaileaKonprobatu2(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM erregistroa WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchall()
        con.commit()
        con.close()
        return datuak

    def erabiltzailearenDatuakEguneratu(self, erab, pasa, erabBerria, pasaBerria):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("UPDATE erregistroa SET erabiltzailea = '" + erabBerria + "', pasahitza = '" + pasaBerria + "' WHERE erabiltzailea = '" + erab + "' AND pasahitza = '" + pasa + "'")
            res.fetchall()
            con.commit()
            con.close()
            return True
        except sqlite3.IntegrityError:
            con.close()
            return False

    def partidaGorde(self, erab, zerrenda, zailtasuna, puntuazioa, tam0, tam1):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("INSERT INTO partida VALUES (?, ?, ?, ?, ?, ?)",
                              (erab, zerrenda, zailtasuna, puntuazioa, tam0, tam1))
            res.fetchall()
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            res = cur.execute(
                "UPDATE partida SET zerrenda = ?, zailtasuna = ?, puntuazioa = ?, tam0 = ?, tam1 = ? WHERE erabiltzailea =  ?",
                (zerrenda, zailtasuna, puntuazioa, tam0, tam1, erab))
            res.fetchall()
            con.commit()
            con.close()


    def partidaKargatu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT zerrenda FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getZailtasuna(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT zailtasuna FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getPuntuazioa(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT puntuazioa FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getTamaina0(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT tam0 FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getTamaina1(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT tam1 FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getAdmin(self, erabiltzailea):  # devuelve si es admin o no
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT administratzailea FROM erregistroa WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return ''.join(datuak) == "Bai"

    def setAdmin(self, erabiltzailea, BaiEz):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("UPDATE erregistroa SET administratzailea = '" + BaiEz + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            res.fetchall()
            con.commit()
            con.close()
            return True
        except sqlite3.IntegrityError:
            con.close()
            return False

    def getUnekoa(self):  # devuelve el nombre del uneko, sino nada
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT erabiltzailea FROM erregistroa WHERE unekoErab = 'Bai'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        if datuak:
            return ''.join(datuak)
        else:
            return ''

    def setUnekoa(self, erabiltzailea, BaiEz):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("UPDATE erregistroa SET unekoErab = '" + BaiEz + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            res.fetchall()
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            con.close()

    def pertsonalizazioaEguneratu(self, kolorea, musika, adreilua, adrKolorea, erabiltzailea):
        print(kolorea)
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            print(adreilua)
            if adreilua==" Zforma":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', Zforma = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua == " ZformaAlderantzizko":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', ZformaAlderantzizko = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua==" Lforma":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', Lforma = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua==" LformaAlderantzizko":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', LformaAlderantzizko = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua==" Laukia":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', Laukia = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua==" Zutabea":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', Zutabea = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            elif adreilua==" Tforma":
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "', Tforma = '" + adrKolorea + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            else:
                res = cur.execute(
                "UPDATE pertsonalizazioa SET atzekoKolorea = '" + kolorea + "', musika = '" + musika + "' WHERE erabiltzailea = '" + erabiltzailea + "'")
            res.fetchall()
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            con.close()

    def pertsonalizazioaSortu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        res = cur.execute("INSERT INTO pertsonalizazioa VALUES('" + erabiltzailea + "', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')")
        res.fetchall()
        con.commit()
        con.close()

    def getKolorea(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT atzekoKolorea FROM pertsonalizazioa WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        if datuak:
            return ''.join(datuak)
        else:
            return ''

    def getMusika(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT musika FROM pertsonalizazioa WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        if datuak:
            return ''.join(datuak)
        else:
            return ''

    def getAdreiluKolorea(self, adreilua, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT " + adreilua + " FROM pertsonalizazioa WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        if datuak:
            return ''.join(datuak)
        else:
            return ''

    def gordeRanking(self, erabiltzailea, id, zailtasuna, puntuazioa):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("INSERT INTO ranking VALUES ('" + id + "', '" + erabiltzailea + "', '" + puntuazioa + "', '" + zailtasuna + "')")
            res.fetchall()
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            con.close()

    def getRankingPertsonala(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM ranking WHERE erabiltzailea = '" + erabiltzailea + "' ORDER BY puntuazioa DESC")
        datuak = cur.fetchall()
        con.commit()
        con.close()
        return datuak

    def getRankingGlobala(self):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM ranking ORDER BY puntuazioa DESC")
        datuak = cur.fetchall()
        con.commit()
        con.close()
        return datuak

    def getZenbatPartida(self, erabiltzailea, zailtasuna):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT count(id) FROM ranking WHERE erabiltzailea = '" + erabiltzailea + "' AND zailtasuna = '" + zailtasuna + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def getNextId(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT MAX(id) FROM ranking WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchone()
        con.commit()
        con.close()
        return datuak

    def gordeSaria(self, saria, erabiltzailea, zailtasuna):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("INSERT INTO saria VALUES ('" + saria + "', '" + erabiltzailea + "', '" + zailtasuna + "')")
            res.fetchall()
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            con.close()

    def getSaria(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM saria WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchall()
        con.commit()
        con.close()
        return datuak
