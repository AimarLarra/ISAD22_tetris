import sqlite3

class datuBasea:

    def __init__(self):
        print("...")

    def taulaSortu(self):
        #Datu basera konektatu
        con = sqlite3.connect("tetrisJokoa.db")
        con.execute("CREATE TABLE if not exists erregistroa (erabiltzailea varchar(20) NOT NULL, pasahitza varchar(20) NOT NULL, PRIMARY KEY (erabiltzailea));")
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
            return False

    def erabiltzailearenPasahitzaInprimatu(self, erabiltzailea):
        con = sqlite3.connect("tetrisJokoa.db")
        cursor = con.execute("select Pasahitza from erabiltzaileak where erabiltzailea = ?", erabiltzailea)
        con.commit()
        pasahitza = cursor.fetchone()
        con.close()