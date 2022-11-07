import sqlite3


class datuBasea:

    def __init__(self):
        print("...")

    def taulaSortu(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute("CREATE TABLE if not exists erregistroa (erabiltzailea varchar(20) NOT NULL, pasahitza varchar(20) NOT NULL, PRIMARY KEY (erabiltzailea));")
        con.commit()
        con.close()

    def taulaSortuPartida(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
            "CREATE TABLE if not exists partida (erabiltzailea varchar(20) NOT NULL, zerrenda varchar(400), zailtasuna varchar(10), PRIMARY KEY (erabiltzailea));")
        con.commit()
        con.close()

    def taulaSortuPartida(self):
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute(
        "CREATE TABLE if not exists pertsonalizazioa (erabiltzailea varchar(20) NOT NULL, atzekoKolorea varchar(40), Laukia varchar(10), Zutabea varchar(10), Lforma varchar(10), LformaAlderantzizko varchar(10), Zforma varchar(10), ZformaAlderantzizko varchar(10), Tforma varchar(10), PRIMARY KEY(erabiltzailea));")
        con.commit()
        con.close()

    def erabiltzaileGehitu(self, erabiltzailea, pasahitza):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        try:
            res = cur.execute("INSERT INTO erregistroa VALUES ('" + erabiltzailea + "', '" + pasahitza + "')")
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

    def partidaGorde(self, erab, zerrenda):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        res = cur.execute("INSERT INTO partida VALUES ('" + erab + "', '" + zerrenda + "')")
        res.fetchall()
        con.commit()
        con.close()

    def partidaKargatu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cur = con.cursor()
        cur.execute("SELECT zerrenda FROM partida WHERE erabiltzailea = '" + erabiltzailea + "'")
        datuak = cur.fetchall()
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