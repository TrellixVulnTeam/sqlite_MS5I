

import sqlite3
from contextlib import closing

rf = r'C:\Users\onoga\OneDrive\Desktop\MyPython\mayuka.png'  #読み込み画像ファイルパス
wf = 'C:\\test\\write.jpg' #書き込み画像ファイルパス
img_path = r"ドスジャイアン.png"
#with closing(sqlite3.connect('path.db')) as db:
  #適当にテーブル作成
 # cursor = db.cursor()
  #try:
   # cursor.execute('create table img_table (img blob);')
  #except sqlite3.OperationalError:
   # cursor.execute('delete from img_table')
  #バイナリ読み込み
  #with open(rf, 'rb') as f:
   # blob = f.read()
  #レコード追加してコミット
  #db.execute('insert into img_table values(?)', [blob])
  #db.commit()

conn = sqlite3.connect("path.db")
c = conn.cursor()
with open(img_path, "rb") as f:
  data = f.read()

c.execute("insert into img_table values(?)" , [data])
conn.commit()
