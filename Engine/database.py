import sqlite3

#Create table
def create_table():
    con = sqlite3.connect('db.sqlite3')
    c = con.cursor()
    c.execute("""CREATE TABLE njuskalo (
            price int,
            area int
            )""")
    con.commit()
    con.close()

#Add new record to the table
def add_one(pr,loc):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO njuskalo VALUES (?,?)",(pr,loc))
    conn.commit()
    conn.close()

#Show all elements
def show_all():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    items = c.execute("SELECT rowid,* FROM njuskalo")
    items = c.fetchall()
    print(items)
    conn.commit()
    conn.close()




