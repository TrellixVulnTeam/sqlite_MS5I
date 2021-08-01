import PySimpleGUI as sg
import sqlite3
import os
import sys

conn = sqlite3.connect("path.db")
c = conn.cursor()
#テーブル名
table_name = "cp_path"

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
def insert_act(file_name, path_name):


    try:
        c.execute("insert into cp_path(名称,path) values('{0}','{1}')".format(file_name,path_name))
        conn.commit()
    except:
        sg.popup_error("同名のファイルが存在します")

#値を削除する
def del_act(file_1):
    c.execute("delete from {1} where 名称 = '{0}'".format(file_1,table_name))
    conn.commit()

#値を更新する
def updete_act(cg_path,dir_name):
    
    c.execute("update cp_path set path = '{0}' where 名称 = '{1}'".format(cg_path, dir_name))
    
    conn.commit()






#for i in select_act():

    #print(i)
#print("ファイル数:",len(select_act()))