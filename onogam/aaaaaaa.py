from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import time
import PySimpleGUI as sg
import datetime
import webbrowser


key_name = r"python-api-project-331021-5d18bfc4ee9a.json" #jsonキー名


sheet_name = "testcsv" #スプレッドシート名

#APIにアクセス
scope = [
    'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(key_name,scope)
#OAuth2の資格情報を使用してGoogle APIにログイン
gc = gspread.authorize(credentials)

cell_number = "B2"
input_value = "TEST"
wks = gc.open(sheet_name).sheet1

#wks.update_acell(cell_number,input_value)
#wks.update_acell("A5","onoami27")
def sp():

    for i in range(15):
        point = random.randint(1,20)
        wks.update_acell(cell_number,point)
        time.sleep(0.2)

    wks.update_acell("B2","終了しました")
    print(wks.acell("B1").value)#B1のセルの値を取得
def count_now():
    count = wks.acell("B2").value
    return count
count_now = count_now()
count = 0+int(count_now)
lay= [
    [sg.Button("push",key="bt_1"),sg.Button("reset",key="reset",button_color="red")],
    [sg.Text(count,key="tx_1")],
    [sg.Button("スプレッドシート",enable_events=True,key="url"),sg.Button("add",key="add")]
]



window = sg.Window("",lay,grab_anywhere=True)

while True:
    event,values = window.read()
    date_now = datetime.datetime.now()
    if event == None:
        break
    try:

        if event == "bt_1":
            count +=1
            window["tx_1"].update(count)
            wks.update_acell(cell_number,count)
            wks.update_acell("C2",f"{date_now}")

        elif event == "reset":
            count = 0
            window["tx_1"].update(count)
            wks.update_acell(cell_number,count)
            wks.update_acell("C2",f"{date_now}")
    except:
        gc = gspread.authorize(credentials)
        wks = gc.open(sheet_name).sheet1

    if event == "url":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1TxLzcHODFNkWDrJyT7931PQrbndDyW08CSKIAWJ_VqE/edit?usp=sharing")

    if event == "add":
        wks.append_row(["1",count,f"{date_now}"])