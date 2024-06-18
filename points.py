from user import GetUserFromCode
import sqlite3 as sql

def GetHousePoints():
    houses = []
    houses.append(dict(house="Morgan", points=GetHousePoint("Morgan")))
    houses.append(dict(house="Ambrose", points=GetHousePoint("Ambrose")))
    houses.append(dict(house="Callan", points=GetHousePoint("Callan")))
    houses.append(dict(house="Elliot", points=GetHousePoint("Elliot")))
    houses.append(dict(house="Finn", points=GetHousePoint("Finn")))
    houses.append(dict(house="Ignatius", points=GetHousePoint("Ignatius")))
    houses.append(dict(house="Rice", points=GetHousePoint("Rice")))
    houses.append(dict(house="Treacy", points=GetHousePoint("Treacy")))
    return houses

def GetHousePoint(house : str):
    cmd = f"""SELECT Place, eventCode
        FROM Results
        JOIN Users ON Results.UserCode = Users.userCode
        WHERE House = '{house}';"""
    
    conn = sql.connect('CCountry.db')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute(cmd)

    rows = cur.fetchall()
    conn.commit()
    conn.close()

    points = 0
    for i in rows:
        points += placeToPoints(i[0], "NC" in i[1])

    return points

def placeToPoints(place : int, isChamp : bool) -> int:
    startNum = 81 if isChamp else 41
    return clamp(startNum - place, 1, 80)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def GivePoints(userCode : str, type : str, place : int, time : str = None):
    user = GetUserFromCode(userCode)
    if user is None:
        return
    if user.role != "Student":
        return
    
    conn = sql.connect('CCountry.db')
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute(f"INSERT INTO Results VALUES ('{user.year.__str__() + type}', '{userCode}', '{time}', '{place}')")

    conn.commit()
    conn.close()