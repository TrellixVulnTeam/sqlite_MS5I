import pandas_datareader.data as pdr
import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os
import japanize_matplotlib
import mplfinance as mpf
import datetime

#テーマの設定
sg.theme("Default")

#オプション設定
sg.set_options(use_ttk_buttons=True,icon="kabu48_48.ico")

#画面ぼやける回避
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

#【日本株】データ取得
def jp_main(name,start,end):
    try:
        col_name = ["日付","始値","高値","安値","終値","出来高"]
        df = pdr.DataReader(f"{name}.JP","stooq",start=start,end=end)
        dfs = pd.DataFrame(df)
        dfs = dfs.sort_index(ascending=True)#インデックスを昇順に変更
        dfs = dfs.reset_index()
        dfs.columns = col_name
        dfs["日付"] = pd.to_datetime(dfs["日付"],format="%Y/%m/%d")
        dfs.set_index("日付",inplace=True)
    except:
        dfs = pd.DataFrame()#空のデータフレームを作成
        return dfs
    
    return dfs

#【米国】データ取得
def main(name,start,end):
    try:
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
    except:
        dfs = pd.DataFrame()#空のデータフレームを作成
        return dfs

    return dfs

#【米国】グラフ描画用
def mpf_main(name,start,end):
    try:
        df = pdr.DataReader(name,"yahoo",start=start,end=end)
    except:
        df = pd.DataFrame()
        return df

    return df

#【日本株】グラフ描画用
def jp_mpf_main(name,start,end):
    try:
        df = pdr.DataReader(f"{name}.JP","stooq",start=start,end=end)
        df = df.sort_index(ascending=True)#インデックスを昇順に変更
    except:
        df = pd.DataFrame()
        return df
    return df

week_list = ["日","月","火","水","木","金","土"]
manth_list = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]

lay_1 =sg.Tab( "米国株",[
    [sg.Text("データを取得したいティッカー名を入力して下さい　(例)AAPL , AMZM , TSLA")],
    [sg.Text("ティッカー名："),sg.InputText(key="in_1",size=(6,1),background_color="#FFFFAA"),],
    [sg.Text("開始日："),sg.InputText(key="in_Start",size=(11,1),background_color="#FFFFAA"),sg.CalendarButton("日付選択",format="%Y/%m/%d",day_abbreviations=week_list,month_names=manth_list,title="日付選択",no_titlebar=False),
    sg.Text("終了日："),sg.InputText(key="in_End",size=(11,1),background_color="#FFFFAA"),sg.CalendarButton("日付選択",format="%Y/%m/%d",day_abbreviations=week_list,month_names=manth_list,title="日付選択",no_titlebar=False)],
    [sg.Button("データ表示",key="start_bt"),sg.Button("csvファイルに保存",key="save_csv"),sg.Button("Excelファイルに保存",key="save_excel")],
    [sg.Button("グラフを描画",key="graph")],
    [sg.Multiline(size=(80,20),key="out_1",)]
    ])


lay_2 =sg.Tab( "日本株",[
    [sg.Text("データを取得したいティッカー名を入力して下さい　(例)7203 , 9983 , 4755")],
    [sg.Text("ティッカー名："),sg.InputText(key="in_2",size=(6,1),background_color="#FFFFAA"),],
    [sg.Text("開始日："),sg.InputText(key="in_2_Start",size=(11,1),background_color="#FFFFAA"),sg.CalendarButton("日付選択",format="%Y/%m/%d",day_abbreviations=week_list,month_names=manth_list,title="日付選択",no_titlebar=False),
    sg.Text("終了日："),sg.InputText(key="in_2_End",size=(11,1),background_color="#FFFFAA"),sg.CalendarButton("日付選択",format="%Y/%m/%d",day_abbreviations=week_list,month_names=manth_list,title="日付選択",no_titlebar=False)],
    [sg.Button("データ表示",key="start_2_bt"),sg.Button("csvファイルに保存",key="save_2_csv"),sg.Button("Excelファイルに保存",key="save_2_excel")],
    [sg.Button("グラフを描画",key="graph_2")],
    [sg.Multiline(size=(80,20),key="out_2")]
    ])

layout = [[sg.TabGroup([[lay_1,lay_2]],tab_background_color="#87CEEB",selected_background_color="white",)],
          [sg.Text("【ソフトウェア作成者】：ono_shin "),sg.Text("※無断でソフトウェアの配布/転載/複製を禁止とします",text_color="red",)]]

window = sg.Window("株価取得", layout,finalize=True,resizable=True,icon="kabu48_48.ico")

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
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_Start"]
            second_day = values["in_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = mpf_main(values["in_1"],values["in_Start"],values["in_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            #日本語対応する為の記述
            cs = mpf.make_mpf_style(rc={"font.family":"IPAexGothic"},gridcolor="gray",gridstyle="--")
            mpf.plot(df,type="candle",volume=True,datetime_format="%Y/%m/%d",
                    title=values["in_1"],ylabel="株価(ドル/円)",ylabel_lower="出来高",mav=(5,25,75),style=cs)
            
            plt.show()
           
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【日本株】グラフを描画
    if event == "graph_2":
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_2_Start"]
            second_day = values["in_2_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = jp_mpf_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            #日本語対応する為の記述
            cs = mpf.make_mpf_style(rc={"font.family":"IPAexGothic"},gridcolor="gray",gridstyle="--")
            mpf.plot(df,type="candle",volume=True,datetime_format="%Y/%m/%d",
                    title=values["in_2"],ylabel="株価(ドル/円)",ylabel_lower="出来高",mav=(5,25,75),style=cs)
            plt.show()        

        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【米国】アウトプット欄に株価データを表示
    if event == "start_bt":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_Start"]
            second_day = values["in_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = main(values["in_1"],values["in_Start"],values["in_End"])
            
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
           
   
            window["out_1"].update(value = out_mes("in_1",df))
            
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【日本株】アウトプット欄に株価データを表示
    if event == "start_2_bt":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_2_Start"]
            second_day = values["in_2_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            window["out_2"].update(value = out_mes("in_2",df))
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    
    #【米国】csvデータ保存
    if event == "save_csv":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_Start"]
            second_day = values["in_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = main(values["in_1"],values["in_Start"],values["in_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい",icon="kabu48_48.ico",history=True,)
            if folder == None:
                pass
            else:

                file_name = sg.popup_get_text("保存したいファイル名を入力して下さい",icon="kabu48_48.ico")
                file_path = os.path.join(folder,f"{file_name}.csv")
                df.to_csv(file_path,encoding="shift jis")
        
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【日本株】csvデータ保存
    if event == "save_2_csv":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_2_Start"]
            second_day = values["in_2_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい",icon="kabu48_48.ico",history=True)
            if folder == None:
                pass
            else:

                file_name = sg.popup_get_text("保存したいファイル名を入力して下さい",icon="kabu48_48.ico")
                file_path = os.path.join(folder,f"{file_name}.csv")
                df.to_csv(file_path,encoding="shift jis")
        
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【米国】Excelデータ保存
    if event == "save_excel":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_1"]) and bool(values["in_Start"]) and bool(values["in_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_Start"]
            second_day = values["in_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = main(values["in_1"],values["in_Start"],values["in_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい",icon="kabu48_48.ico",history=True)
            if folder == None:
                pass
            else:

                file_name = sg.popup_get_text("保存したいファイル名を入力して下さい",icon="kabu48_48.ico")
                file_path = os.path.join(folder,f"{file_name}.xlsx")
                df.to_excel(file_path)
        
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    #【日本株】Excelデータ保存
    if event == "save_2_excel":
        #入力欄に空白があるとmain関数を実行しない様に設定
        if bool(values["in_2"]) and bool(values["in_2_Start"]) and bool(values["in_2_End"]) == True:
            #日付選択で未来の数字を入力した時にメッセージを表示
            first_day = values["in_2_Start"]
            second_day = values["in_2_End"]
            today = datetime.date.today()
            today = today.strftime("%Y/%m/%d")
            if first_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif second_day > today:
                sg.popup("本日以前の日程を選択して下さい",icon="kabu48_48.ico")
                continue
            elif first_day > second_day:
                sg.popup("開始日は終了日より前の日に設定して下さい",icon="kabu48_48.ico")
                continue

            df = jp_main(values["in_2"],values["in_2_Start"],values["in_2_End"])
            #データフレームを取得できなかった場合の処理
            dfs = df.empty #データフレームが空の場合Trueを返す
            if dfs == True:
                sg.popup("取得可能なデータがありません",icon="kabu48_48.ico")
                continue
            folder = sg.popup_get_folder("保存先のフォルダを選択して下さい",icon="kabu48_48.ico",history=True)
            if folder == None:
                pass
            else:

                file_name = sg.popup_get_text("保存したいファイル名を入力して下さい",icon="kabu48_48.ico")
                file_path = os.path.join(folder,f"{file_name}.xlsx")
                df.to_excel(file_path)
        
        else:
            sg.popup("入力されていない項目があります",icon="kabu48_48.ico")
            pass
    