import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'FAITH KARIMI',34,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'BENARD MUNENE',24,240000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'JOY MWENDE',44,140000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'VAN WAWIRA',26,540000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'LIAM MUSHIRA',33,640000.00)")
conn.commit()

print("Employees inserted successfully")
conn.close()