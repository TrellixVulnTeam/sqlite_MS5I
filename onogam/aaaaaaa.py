import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time

key_name = r"python-api-project-331021-5d18bfc4ee9a.json" #jsonキー名
sheet_name = "testcsv" #スプレッドシート名

#APIにアクセス
scope = [
    'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(key_name,scope)
#OAuth2の資格情報を使用してGoogle APIにログイン
gc = gspread.authorize(credentials)

cell_number = "B1"
input_value = "TEST"
wks = gc.open(sheet_name).sheet1
wks_key = gc.open(sheet_name)
#wks.update_acell(cell_number,input_value)
#wks.update_acell("A5","onoami27")

for i in range(15):
    point = random.randint(1,20)
    wks.update_acell(cell_number,point)
    time.sleep(0.2)

wks.update_acell("B2","終了しました")
print(wks.acell("B1").value)#B1のセルの値を取得