import pandas_datareader as pdr
import pandas as pd


#【米国】データ取得
def main(name,start,end):
    try:
        col_name = ["日付","高値","安値","始値","終値","出来高","調整済み終値"]
        #株価取得
        df = pdr.DataReader(name,"yahoo",start=start,end=end)
        if bool(df) == False:
            return
        else:
            
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
        dfs = []
        return dfs
        

    return dfs

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
        dfs =[]
        return dfs
    
    return dfs

#try:
#    df = pdr.DataReader("asdfas","yahoo",start="2021/09/01",end="2021/10/01")
#    print(df)

#except:
#    print(df)
#    print("data無し")

try:

    df_1 =main("aa","2021/09/01","2021/09/30")
    df_2 = jp_main("8888","2021/09/01","2021/09/30")
except:
    print("no")
    pass

print(df_1)