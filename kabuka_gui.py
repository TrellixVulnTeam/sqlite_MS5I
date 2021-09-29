import pandas_datareader.data as pdr
import pandas as pd
import sqlite3
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os
import japanize_matplotlib
import mplfinance as mpf

sg.theme("DarkGreen6")

#画面ぼやける回避
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

#【日本株】データ取得
def jp_main(name,start,end):
    col_name = ["日付","始値","高値","安値","終値","出来高"]
    df = pdr.DataReader(f"{name}.JP","stooq",start=start,end=end)
    dfs = pd.DataFrame(df)
    dfs = dfs.reset_index()
    dfs.columns = col_name
    dfs["日付"] = pd.to_datetime(dfs["日付"],format="%Y/%m/%d")
    dfs.set_index("日付",inplace=True)
    
    return dfs

#【米国】データ取得
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
#【米国】グラフ描画用
def mpf_main(name,start,end):

    df = pdr.DataReader(name,"yahoo",start=start,end=end)
  
    return df
#【日本株】グラフ描画用
def jp_mpf_main(name,start,end):
    df = pdr.DataReader(f"{name}.JP","stooq",start=start,end=end)
  
    return df



lay_1 =sg.Tab( "米国株",[
    [sg.Text("データを取得したいティッカー名を入力して下さい　(例)AAPL , AMZM , TSLA")],
    [sg.Text("ティッカー名："),sg.InputText(default_text="AMZN",key="in_1",size=(6,1)),],
    [sg.Text("開始日："),sg.InputText(key="in_Start",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d"),
    sg.Text("終了日："),sg.InputText(key="in_End",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d")],
    [sg.Button("データ表示",key="start_bt"),sg.Button("csvファイルに保存",key="save_csv"),sg.Button("Excelファイルに保存",key="save_excel")],
    [sg.Button("グラフを描画",key="graph")],
    [sg.Multiline(size=(80,20),key="out_1",)]
    ])


lay_2 =sg.Tab( "日本株",[
    [sg.Text("データを取得したいティッカー名を入力して下さい　(例)7203 , 9983 , 4755")],
    [sg.Text("ティッカー名："),sg.InputText(default_text="7203",key="in_2",size=(6,1)),],
    [sg.Text("開始日："),sg.InputText(key="in_2_Start",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d"),
    sg.Text("終了日："),sg.InputText(key="in_2_End",size=(11,1)),sg.CalendarButton("日付選択",format="%Y/%m/%d")],
    [sg.Button("データ表示",key="start_2_bt"),sg.Button("csvファイルに保存",key="save_2_csv"),sg.Button("Excelファイルに保存",key="save_2_excel")],
    [sg.Button("グラフを描画",key="graph_2")],
    [sg.Multiline(size=(80,20),key="out_2")]
    ])

layout = [[sg.TabGroup([[lay_1,lay_2]])]]

window = sg.Window("株価取得", layout,finalize=True,resizable=True)

while True:
    event,values = window.read()

    def out_mes(name,df):
        m1 = f"ティッカー名：{values[name]}"
        m2 = "\n*************************************************************************************************\n"
        m3 = df
        m4 = "\n*************************************************************************************************"
        mes = f"{m1}{m2}{m3}{m4}"
        return mes

    if event in (None,sg.WIN_CLOSED):
        break
    #【米国】グラフを描画
    if event == "graph":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            #df = main(values["in_1"],values["in_Start"],values["in_End"])
            df = mpf_main(values["in_1"],values["in_Start"],values["in_End"])
            #fig = plt.figure(figsize=(6,6))#グラフサイズを指定
            
            
            def start_chart():#始値を描画する
                plt.plot(df.index,df["始値"],label="始値")

            def end_chart():#終値を描画する
                plt.plot(df.index,df["終値"],label="終値")

            def high_chart():#高値を描画する
                plt.plot(df.index,df["高値"],label="高値")

            def low_chart():#安値を描画する
                plt.plot(df.index,df["安値"],label="安値")

            def AdjClose_chart():#調整済み終値を描画する
                plt.plot(df.index,df["調整済み終値"],label="調整済み終値")

            #日本語対応する為の記述
            cs = mpf.make_mpf_style(rc={"font.family":"IPAexGothic"},gridcolor="gray",gridstyle="--")
            mpf.plot(df,type="candle",volume=True,datetime_format="%Y/%m/%d",
                    title=values["in_1"],ylabel="株価(ドル/円)",ylabel_lower="出来高",mav=(5,25),style=cs)
            

            #plt.grid()#グリッドを追加
            #plt.title(values["in_1"])
            #plt.legend()
            #plt.xticks(rotation=30)
            plt.show()
           
        else:
            sg.popup("入力されていない項目があります")
            pass
    #【日本株】グラフを描画
    if event == "graph_2":
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            df = jp_mpf_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            #日本語対応する為の記述
            cs = mpf.make_mpf_style(rc={"font.family":"IPAexGothic"},gridcolor="gray",gridstyle="--")
            mpf.plot(df,type="candle",volume=True,datetime_format="%Y/%m/%d",
                    title=values["in_2"],ylabel="株価(ドル/円)",ylabel_lower="出来高",mav=(5,25),style=cs)
            plt.show()        

        else:
            sg.popup("入力されていない項目があります")
            pass
    #【米国】アウトプット欄に株価データを表示
    if event == "start_bt":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            #window["table"].update(values=ui)
   
            window["out_1"].update(value = out_mes("in_1",df))
            
        else:
            sg.popup("入力されていない項目があります")
            pass
    #【日本株】アウトプット欄に株価データを表示
    if event == "start_2_bt":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            window["out_2"].update(value = out_mes("in_2",df))
        else:
            sg.popup("入力されていない項目があります")
            pass
    
    #【米国】csvデータ保存
    if event == "save_csv":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            df = main(values["in_1"],values["in_Start"],values["in_End"])
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい")
            file_name = sg.popup_get_text("保存したいファイル名を入力して下さい")
            file_path = os.path.join(folder,f"{file_name}.csv")
            print(file_path)
            df.to_csv(file_path,encoding="shift jis")
        
        else:
            sg.popup("入力されていない項目があります")
            pass
    #【日本株】csvデータ保存
    if event == "save_2_csv":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい")
            file_name = sg.popup_get_text("保存したいファイル名を入力して下さい")
            file_path = os.path.join(folder,f"{file_name}.csv")
            print(file_path)
            df.to_csv(file_path,encoding="shift jis")
        
        else:
            sg.popup("入力されていない項目があります")
            pass
    #【米国】Excelデータ保存
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
    #【日本株】Excelデータ保存
    if event == "save_2_excel":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい")
            file_name = sg.popup_get_text("保存したいファイル名を入力して下さい")
            file_path = os.path.join(folder,f"{file_name}.xlsx")
            
            df.to_excel(file_path)
        
        else:
            sg.popup("入力されていない項目があります")
            pass
    