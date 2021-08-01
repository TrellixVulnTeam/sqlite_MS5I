import sqlite3

conn = sqlite3.connect("path.db")
c = conn.cursor()
sel = c.execute("select path from cp_path where 名称 = 'コメントあり'")
name = c.fetchone()

uu = {"home":"{0}".format(name[0])}
print(uu["home"])
