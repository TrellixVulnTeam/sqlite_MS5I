import PySimpleGUI as sg
import sqlite3
import datetime
import os

conn = sqlite3.connect("path.db")
c = conn.cursor()
#テーブル名
table_name = "path"

#column名を取得する関数
def colum_name():
   
    c.execute("select * from {}".format(table_name))
    out = []
    for i in c.description:
        out.append(i[0])
        
    return out

def select_act():
    
    c.execute("select * from {}".format(table_name))
    out = c.fetchall()

    return out

#値をインサートする
def insert_act(file):
    try:

        now_time = str(datetime.datetime.now())
        file_name = os.path.basename(file)
        c.execute("insert into {2}(更新時間,ファイル名) values('{0}','{1}')".format(now_time,file_name,table_name))
        conn.commit()
    except:
        sg.popup_error("同名のファイルが存在します")

#値を削除する
def del_act(file_1):
    c.execute("delete from {1} where 更新時間 = '{0}'".format(file_1,table_name))
    conn.commit()






#for i in select_act():

    #print(i)
#print("ファイル数:",len(select_act()))