import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect(r"L:\部門_部署\生産準備課\金型・設備改良係共通〔管理者：荻野〕\不具合指示書回覧\path.db")
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

#path設定用
def path(name):

    c.execute("select path from {0} where 名称 = '{1}'".format(table_name,name))
    return c.fetchone()[0]


#テーブルの値を全て抽出する
def select_act():
    
    c.execute("select * from {}".format(table_name))
    out = c.fetchall()

    return out

#値をインサートする
def insert_act(file_name, path_name):


    try:
        c.execute("insert into {2}(名称,path) values('{0}','{1}')".format(file_name,path_name,table_name))
        conn.commit()
    except:
        sg.popup_error("同名のファイルが存在します")

#値を削除する
def del_act(file_1):
    c.execute("delete from {1} where 名称 = '{0}'".format(file_1,table_name))
    conn.commit()

#値を更新する
def updete_act(cg_path,dir_name):
    
    c.execute("update {2} set path = '{0}' where 名称 = '{1}'".format(cg_path, dir_name,table_name))
    
    conn.commit()








#for i in select_act():

    #print(i)
#print("ファイル数:",len(select_act()))
