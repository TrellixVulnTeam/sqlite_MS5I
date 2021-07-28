import datetime
import sqlite3
import os


conn = sqlite3.connect("main_data.db")
c = conn.cursor()

#値をインサートする
def insert_act(file):
    now_time = str(datetime.datetime.now())
    file_name = os.path.basename(file)
    c.execute("insert into main values(?,?)",(now_time,file_name))
    conn.commit()
