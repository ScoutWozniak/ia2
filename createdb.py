import sqlite3 as sql
conn = sql.connect('CCountry.db')
print("Database opened ;)")


# conn.execute('''
#     CREATE TABLE Users
#     (UserCode varchar(10),
#     LastName varchar(25),
#     House varchar(10),
#     Role varchar(10),
#     YearLevel int,
#     DOB varchar(8),
#     FirstName varchar(20),
#     ChildCode varchar(8)) 
#     ''')

conn.execute('''
    CREATE TABLE UserLogins
    (UserCode varchar(10),
    Email varchar(40),
    Password varchar(20))
    ''')


#ChildCode can be NULL


# conn.execute('''
#     CREATE TABLE AgeLevel
#     (AgeLevel varchar(10),
#     UserCode varchar(10))''')


# conn.execute('''
#     CREATE TABLE AgeLevelEvent
#     (AgeLevel varchar(10),
#     EventName varchar (20),
#     UserCode varchar(10))''')


# conn.execute('''
#     CREATE TABLE AgeLevelEventPlace
#     (AgeLevel varchar(10),
#     EventName varchar(20),
#     UserCode varchar(10),
#     Time varchar(6),
#     Place int
#     Points int)
# ''')


conn.commit()


print("Table created successfully")


conn.close()