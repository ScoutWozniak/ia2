import sqlite3 as sql
from roles import Roles

class User:
    def __init__(self, name : str, code : str, role : str, year : int) -> None:
        self.name = name
        self.code = code
        self.role = role
        self.year = year
    
    def IsNominated(self) -> bool:
        conn = sql.connect('CCountry.db')
        conn.row_factory = sql.Row

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Nominations WHERE userCode = '{self.code}'")

        rows = cur.fetchall()
        conn.commit()
        conn.close()

        return len(rows) > 0
    
    def Nominate(self):
        conn = sql.connect('CCountry.db')
        conn.row_factory = sql.Row

        cur = conn.cursor()
        cur.execute(f"INSERT INTO Nominations VALUES ('{self.code}', '{self.year.__str__() + "C"}')")

        conn.commit()
        conn.close()
    
    def UnNominate(self):
        conn = sql.connect('CCountry.db')
        conn.row_factory = sql.Row

        cur = conn.cursor()
        cur.execute(f"DELETE FROM Nominations WHERE userCode = '{self.code}'")

        conn.commit()
        conn.close()


def GetUserFromCode(code :str) -> User:
    conn = sql.connect('CCountry.db')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Users WHERE UserCode = '{code}'")

    rows = cur.fetchall()
    print(rows[0].keys())    
    conn.commit()
    conn.close()

    return User(rows[0]['FirstName'], rows[0]['userCode'], rows[0]['Role'], rows[0]['Year'])

def GetUserFromEmail(code :str) -> User:
    conn = sql.connect('CCountry.db')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Users WHERE email = '{code}'")

    rows = cur.fetchall()
    print(rows[0].keys())    
    conn.commit()
    conn.close()

    return User(rows[0]['FirstName'], rows[0]['userCode'], rows[0]['Role'], rows[0]['Year'])

if __name__ == "__main__":
    user1 = GetUserFromCode("s624881")
    print(user1.IsNominated())
    user1.UnNominate()