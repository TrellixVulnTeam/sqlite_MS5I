import sqlite3
from sqlite3.dbapi2 import Cursor
import PySimpleGUI as sg
import os

conn = sqlite3.connect("img.db")
c = conn.cursor()

#c.execute("create table img_t(file_name , img blob)")
#conn.commit()

#画像インサート
def file_insert():
    get_file = sg.popup_get_file("読み込むファイルを選択して下さい")
    file_name = os.path.basename(get_file)
    with open(get_file,"rb") as f:
        base = f.read()
    
    
    c.execute("insert into img_t values(?,?)" , (file_name,base))
    conn.commit()

#具現化
def real(name,number):
    row = c.execute("select * from img_t").fetchall()
    pic = row[number]

    f = open("{}".format(name),"wb")
    f.write(pic[0])
    f.close()
    c.close()

file_insert()
#file_insert()
c.execute("select file_name from img_t")
print(c.fetchall())

