import sqlite3
import pandas as pd
import os
import datetime
import test_sginsert


#databaseに接続＆databaseファイル作成
conn = sqlite3.connect("main_data.db")
c = conn.cursor()
#テーブルを作成
#c.execute("create table main_2(ID integer primary key,更新時間 text,ファイル名 unique)")

#ユニークインデックスを作成(データの重複防止)
#c.execute("create unique index mai on main_(ファイル名)")

#print(test_sginsert.colum_name())