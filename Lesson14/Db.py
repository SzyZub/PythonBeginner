import sqlite3

conn = sqlite3.connect("Lesson14/DB2.sqlite")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    address = email.split("@")
    RA = address[1]
    cur.execute("SELECT count FROM Counts WHERE org = ? ", (RA,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (RA,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",(RA,))
conn.commit()