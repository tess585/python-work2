import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("UPDATE EMPLOYEES SET SALARY=540000.0 WHERE ID=5")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEES")
for row in cursor:
    print("ID:", row[0])
    print("NAME:", row[1])
    print("AGE:", row[2])
    print("SALARY:", row[3])
print("update successful")
conn.close()