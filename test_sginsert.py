import PySimpleGUI as sg
import sqlite3
import datetime
import os

conn = sqlite3.connect("main_data.db")
c = conn.cursor()

#column名を取得する関数
def colum_name():
   
    c.execute("select * from main")
    out = []
    for i in c.description:
        out.append(i[0])
        
    return out




def select_act():
    
    c.execute("select * from main")
    out = c.fetchall()

    return out

#値をインサートする
def insert_act(file):
    now_time = str(datetime.datetime.now())
    file_name = os.path.basename(file)
    c.execute("insert into main values(?,?)",(now_time,file_name))
    conn.commit()