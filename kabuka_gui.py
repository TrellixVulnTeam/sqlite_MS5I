from re import sub
from traceback import print_tb
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, InputText
import pandas_datareader.data as pdr
import pandas as pd
import sqlite3
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os


#画面ぼやける回避
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

def main(name,start,end):
    col_name = ["日付","高値","安値","始値","終値","出来高","調整済み終値"]
    #株価取得
    df = pdr.DataReader(name,"yahoo",start=start,end=end)
    #pandas-datareaderで取得した値をデータフレームに変換
    dfs = pd.DataFrame(df)
    #インデックスをカラムに戻す
    dfs = dfs.reset_index()
    #カラム名を日本語へ変換
    dfs.columns = col_name
    #日付をdatetime型へ変換
    dfs["日付"] = pd.to_datetime(dfs["日付"],format="%Y/%m/%d")
    #日付の行をインデックスへ再設定 ※inplace = Trueを忘れずに記載
    dfs.set_index("日付",inplace=True)

    return dfs




sum = pdr.DataReader("HDV","yahoo",start="2021/09/01",end="2021/09/06")
aa = pd.DataFrame(sum)
ui = aa.reset_index()
val = [["onogami","kahon"],["happy","lose"]]

lay = [
    [sg.Text("データを取得したいティッカー名を入力して下さい　(例)AAPL , AMZM , TSLA")],
    [sg.Text("ティッカー名："),sg.InputText(default_text="AMZN",key="in_1",size=(6,1)),],
    [sg.Text("開始日："),sg.InputText(key="in_Start",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d"),
    sg.Text("終了日："),sg.InputText(key="in_End",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d")],
    [sg.Button("データ表示",key="start_bt"),sg.Button("csvファイルに保存",key="save_csv"),sg.Button("Excelファイルに保存",key="save_excel")],
    [sg.Button("グラフを描画",key="graph")],
    [sg.Output(size=(80,20))]
    ]


window = sg.Window("株価取得", lay,finalize=True,resizable=True)

while True:
    event,values = window.read()

    if event in (None,WIN_CLOSED):
        break
    #グラフを描画
    if event == "graph":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            plt.plot(df.index,df["始値"])
            #plt.plot(df["始値"],df["終値"])
            plt.legend()
            plt.xticks(rotation=30)
            plt.show()
        
        else:
            sg.popup("入力されていない項目があります")
            pass

    #アウトプット欄に株価データを表示
    if event == "start_bt":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            #window["table"].update(values=ui)
            
            print(f"ティッカー名：{values['in_1']}","\n*************************************************************************************************\n",df,
                        "\n*************************************************************************************************" )
            
        else:
            sg.popup("入力されていない項目があります")
            pass

    if event == "save_csv":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい")
            file_name = sg.popup_get_text("保存したいファイル名を入力して下さい")
            file_path = os.path.join(folder,f"{file_name}.csv")
            print(file_path)
            df.to_csv(file_path)
        
        else:
            sg.popup("入力されていない項目があります")
            pass

    if event == "save_excel":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい")
            file_name = sg.popup_get_text("保存したいファイル名を入力して下さい")
            file_path = os.path.join(folder,f"{file_name}.xlsx")
            
            df.to_excel(file_path)
        
        else:
            sg.popup("入力されていない項目があります")
            pass

