import sqlite3 as sq

con = None


# Creation of the table
def creation(file_name: str, name: str):
    try:

        con = sq.connect(f"{file_name}.db")
        cur = con.cursor()

        cur.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
            station_id INTEGER,
            max_vel INTEGER,
            average_vel INTEGER,
            important_build INTEGER
            )""")
        con.commit()
    except sq.Error:
        if con: con.rollback()
        print("Error creation")
    finally:
        if con: con.close()     # closing


#creation("BegovayData.db", 'Begovaya')


# Dropping the table
def dropping(file_name: str, name: str):
    try:
        con = sq.connect(f"{file_name}.db")
        cur = con.cursor()

        cur.execute(f"""DROP TABLE IF EXISTS {name} """)

        con.commit()
    except sq.Error:
        if con: con.rollback()
        print("Error dropping")
    finally:
        if con: con.close()     # closing


# Adding to the table

def insert(file_name: str, name: str, column: str, new: str):
    try:
        con = sq.connect(f"{file_name}.db")
        cur = con.cursor()

        cur.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
            station_id INTEGER,
            max_vel INTEGER,
            average_vel INTEGER,
            important_build INTEGER
            )""")

        cur.execute(f"""INSERT INTO {name} ({column}) VALUES  ({new})""")
        con.commit()
    except sq.Error:
        if con: con.rollback()
        print("Error insert")
    finally:
        if con: con.close()     # closing

#insert("BegovayData.db", 'Begovaya','max_vel','123')



# Updating the table

def update(file_name: str, name: str, old: str, new: str):
    try:
        con = sq.connect(f"{file_name}.db")
        cur = con.cursor()

        cur.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
            station_id INTEGER,
            max_vel INTEGER,
            average_vel INTEGER,
            important_build INTEGER
            )""")

        cur.execute(f"""UPDATE {name} SET {old} = {new}""")
        con.commit()
    except sq.Error:
        if con: con.rollback()
        print("Error update")
    finally:
        if con: con.close()     # closing


#dropping("BegovayData.db", 'Begovaya')

