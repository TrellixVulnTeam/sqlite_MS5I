import datetime
import sqlite3
import os
now_time = str(datetime.datetime.now())
file_name = os.path.basename(r"C:\Users\onoga\OneDrive\Desktop\検証用フォルダ\229-772-82711-111111-1修理)高橋.xlsx")

conn = sqlite3.connect("main_data.db")
c = conn.cursor()

#値をインサートする
c.execute("insert into main values(?,?)",(now_time,file_name))
conn.commit()
