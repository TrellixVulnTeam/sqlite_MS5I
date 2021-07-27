import sqlite3
import pandas as pd
import os
import datetime


#databaseに接続＆databaseファイル作成
conn = sqlite3.connect("main_data.db")
c = conn.cursor()
#テーブルを作成
c.execute("create table main(更新時間,ファイル名)")
