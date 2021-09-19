import PySimpleGUIQt as sgq
import PySimpleGUI as sg
import sqlite3
import datetime
from psgtray import SystemTray
import re
import os

#ぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

#ユーザーセッティング
settings = sg.UserSettings()
settings.load()

main_col_name  = ["更新時間","タスク名"]
log_col_name = ["完了時間","タスク名"]
log_todo_col_name = ["いつまでに","やること"]

#テーマを設定
sg.theme("LightBlue3")
sgq.theme("LightBlue3")

#sqliteの設定
conn = sqlite3.connect("task.db")
c = conn.cursor()

# テーブル作成　　c.execute("create table main(nowtime text, name text)")
#c.execute("insert into main values(?,?)",("6/8","onogami"))
#mainテーブルに値をインサートする
def insert(name):
    time = datetime.datetime.now()
    nowtime = time.strftime("%Y-%m-%d %H:%M")
    c.execute("insert into main values(?,?)",(nowtime,name))
    conn.commit()
#logテーブルに値をインサートする
def insert_log(outtime,name):
    c.execute("insert into 'log' values(?,?)",(outtime,name))
    conn.commit()
#log_todoテーブルに値をインサートする
def insert_log_todo(outtime,name):
    c.execute("insert into 'log_todo' values(?,?)",(outtime,name))
    conn.commit()
    window["log"].update(values = select_log_todo())
#やることリストのメインテーブルに表示させる項目
def select():
    c.execute("select * from main")
    out = c.fetchall()
    return out
#やることリストの履歴を表示させる項目
def select_log():
    c.execute("select * from 'log'")
    out = c.fetchall()
    return out
#ToDoリストの履歴を表示させる項目
def select_log_todo():
    c.execute("select * from 'log_todo'")
    out = c.fetchall()
    return out
#ファイル保存の要素を表示させる
def select_file_insert():
    c.execute("select * from 'fileinsert'")
    out = c.fetchall()
    return out
#内容更新の処理関数
def updete_act(name,up_name,old_name):
    time = datetime.datetime.now()
    nowtime = time.strftime("%Y-%m-%d %H:%M")
    c.execute("update main set nowtime = '{0}' where nowtime = '{1}' and name = '{2}' ".format(nowtime, name, old_name))
    c.execute("update main set name = '{0}' where name = '{1}'".format(up_name, old_name))
    
    conn.commit()

#画像インサート
def file_insert():
    try:
        get_file = sgq.popup_get_file("読み込むファイルを選択して下さい")
        if bool(re.match("file:///",get_file)) == True:
            get_file = re.split("file:///",get_file)[1]
        file_name = os.path.basename(get_file)

        with open(get_file,"rb") as f:
            base = f.read()
        time = datetime.datetime.now()
        outtime = time.strftime("%Y-%m-%d %H:%M")
        c.execute("insert into file_insert values(?,?,?)" , (outtime,file_name,base))
        conn.commit()
    except:
        pass

lib_name = select()
combo_list = ["やること","ToDo"]
la_1=sg.Tab("やることリスト",[      
                [sg.Multiline(key="in"),sg.Button("内容更新",key="up_1")],
                [sg.Table(values=lib_name,enable_events=True,key="table",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=main_col_name,
                    justification="left",auto_size_columns=False,num_rows=10)],
                [sg.Button("完了",key="comp"),sg.Button("削除",key="del_1"),sg.Button("ok",key="ok")],
                [sg.Menu(menu_definition=[["追加",["タスクを追加する","削除"],]],background_color="white",)]])

la_2=sg.Tab("履歴",[
                [sg.Multiline(key="in_2"),sg.Combo(values=combo_list, size=(10,5),key="combo",enable_events=True,default_value="やること")],
                [sg.Table(values=select_log(),enable_events=True,key="log",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=log_col_name,
                justification="left",auto_size_columns=False,num_rows=10)],
                [sg.Button("削除",key="del_2")]])

month_list = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月",]
week_list = ["日","月","火","水","木","金","土",]
la_3=sg.Tab("ToDoリスト",[
                [sg.Text("いつまでに"),sg.Text("やること",pad=(60,0))],
                [sg.InputText(key="todo_day_1",size=(10,0),default_text=settings["todo_day_1"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_1",default_text=settings["todo_in_1"]),sg.Button("完了",key="todo_b1")],
                [sg.InputText(key="todo_day_2",size=(10,0),default_text=settings["todo_day_2"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_2",default_text=settings["todo_in_2"]),sg.Button("完了",key="todo_b2")],
                [sg.InputText(key="todo_day_3",size=(10,0),default_text=settings["todo_day_3"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_3",default_text=settings["todo_in_3"]),sg.Button("完了",key="todo_b3")],
                [sg.InputText(key="todo_day_4",size=(10,0),default_text=settings["todo_day_4"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_4",default_text=settings["todo_in_4"]),sg.Button("完了",key="todo_b4")],
                [sg.InputText(key="todo_day_5",size=(10,0),default_text=settings["todo_day_5"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_5",default_text=settings["todo_in_5"]),sg.Button("完了",key="todo_b5")],
                [sg.InputText(key="todo_day_6",size=(10,0),default_text=settings["todo_day_6"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_6",default_text=settings["todo_in_6"]),sg.Button("完了",key="todo_b6")],
                [sg.InputText(key="todo_day_7",size=(10,0),default_text=settings["todo_day_7"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_7",default_text=settings["todo_in_7"]),sg.Button("完了",key="todo_b7")],
                [sg.InputText(key="todo_day_8",size=(10,0),default_text=settings["todo_day_8"]),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_8",default_text=settings["todo_in_8"]),sg.Button("完了",key="todo_b8")],
                ])

la_4 = sg.Tab("ファイル保存",[
                [sg.Table(values=[[]])]
])

lay =[
    [sg.TabGroup([[la_1,la_3,la_2,la_4]])]
    
]

window = sg.Window("タスク管理",lay,finalize=True,enable_close_attempted_event=True)

menu = ["",["追加",["タスクを追加する"],"削除"]]
tray = SystemTray(menu=menu,window=window)

while True:


    event,values = window.read()
    #tableの要素を削除する
    def delete():
        if values["table"] == []:
            sg.popup_ok("タブを選択してください")
            pass

        else:

            elem = window["table"].get()
            filename = elem[values["table"][0]]
            
            c.execute(f"delete from main where nowtime = '{filename[0]}' and name = '{filename[1]}'")
            conn.commit()
            window["table"].update(values = select())

    #履歴のlogをを削除する
    def delete_log():
        if values["log"] == []:
            sg.popup_ok("タブを選択してください")
            pass

        else:
            if values["combo"] == "やること":
                elem = window["log"].get()
                filename = elem[values["log"][0]]
                
                c.execute(f"delete from log where outtime = '{filename[0]}' and name = '{filename[1]}'")
                conn.commit()
                window["log"].update(values = select_log())
            elif values["combo"] == "ToDo":
                elem = window["log"].get()
                filename = elem[values["log"][0]]
                c.execute(f"delete from log_todo where outtime = '{filename[0]}' and name = '{filename[1]}'")
                window["log"].update(values = select_log_todo())
                conn.commit()

    #windowのenable_close_attempted_eventをTrueにしてsg.WIN_X_EVENTでXボタンを押したときの処理を設定する
    if event in (None,sg.WIN_X_EVENT):
        #ウィンドウを閉じる時にToDoリストの内容をユーザーセッティングに保存
        settings["todo_day_1"] = values["todo_day_1"]
        settings["todo_day_2"] = values["todo_day_2"]
        settings["todo_day_3"] = values["todo_day_3"]
        settings["todo_day_4"] = values["todo_day_4"]
        settings["todo_day_5"] = values["todo_day_5"]
        settings["todo_day_6"] = values["todo_day_6"]
        settings["todo_day_7"] = values["todo_day_7"]
        settings["todo_day_8"] = values["todo_day_8"]

        settings["todo_in_1"] = values["todo_in_1"]
        settings["todo_in_2"] = values["todo_in_2"]
        settings["todo_in_3"] = values["todo_in_3"]
        settings["todo_in_4"] = values["todo_in_4"]
        settings["todo_in_5"] = values["todo_in_5"]
        settings["todo_in_6"] = values["todo_in_6"]
        settings["todo_in_7"] = values["todo_in_7"]
        settings["todo_in_8"] = values["todo_in_8"]
        break
    #システムトレイのボタンを適用
    if event == tray.key:
        event =values[event]

    if event == "ok":
        file_insert()
    #tableが選択されたときにタスク内容を表示させる
    if event == "table":
        get_value=window["table"].get()

        window["in"].update(get_value[values["table"][0]][1])
    #logが選択されたときにタスクの内容を表示させる
    if event == "log":
        get_value=window["log"].get()

        window["in_2"].update(get_value[values["log"][0]][1])

    #コンボボックスの処理
    if event == "combo":
        #ToDoを選択した時の処理
        if values["combo"] == "ToDo":
            window["log"].update(values = select_log_todo())
      
        #やることを選択した時の処理
        elif values["combo"] == "やること":
            window["log"].update(values = select_log())
    
    #内容更新ボタンを押したときの処理
    if event == "up_1":
        if values["table"] == []:
            sg.popup_ok("先にタブを選択し内容を変更してください")
            pass
        else:
            get_value = window["table"].get()
            outtime = get_value[values["table"][0]][0]
            log_name = get_value[values["table"][0]][1]

            updete_act(name=outtime, up_name=values["in"], old_name=log_name)
            window["table"].update(values = select())
    #完了ボタンを押したときの処理
    if event == "comp":
        if values["table"] == []:
            sg.popup_ok("タブを選択してください")
            pass
        else:
            get_value = window["table"].get()
            outtime = get_value[values["table"][0]][0]
            log_name = get_value[values["table"][0]][1]
            time = datetime.datetime.now()
            nowtime = time.strftime("%Y-%m-%d %H:%M")
            insert_log(nowtime,log_name)
            window["log"].update(values = select_log())
            delete()
    
    #タスクを追加する処理
    if event == "タスクを追加する":
        get_text = sg.popup_get_text(message="追加するタスク名を入力してください")
        if "OK":
            #入力がない状態でOKボタンを押したときに何も処理しない為の記述
            if get_text == "":
                pass
            if get_text == "cancel":
                pass
            if get_text == None:
                pass
            elif bool(get_text) == True:
                insert(get_text)
    
        window["table"].update(values = select())
    
    #ToDoリストの完了ボタンを押したときの処理
    if event == "todo_b1":
        if bool(values["todo_day_1"]) and bool(values["todo_in_1"]) == True:
            todo_day = values["todo_day_1"]
            todo_in = values["todo_in_1"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_1"].update("")
            window["todo_in_1"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass

    if event == "todo_b2":
        if bool(values["todo_day_2"]) and bool(values["todo_in_2"]) == True:
            todo_day = values["todo_day_2"]
            todo_in = values["todo_in_2"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_2"].update("")
            window["todo_in_2"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass
        
    if event == "todo_b3":
        if bool(values["todo_day_3"]) and bool(values["todo_in_3"]) == True:
            todo_day = values["todo_day_3"]
            todo_in = values["todo_in_3"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_3"].update("")
            window["todo_in_3"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass
    
    if event == "todo_b4":
        if bool(values["todo_day_4"]) and bool(values["todo_in_4"]) == True:
            todo_day = values["todo_day_4"]
            todo_in = values["todo_in_4"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_4"].update("")
            window["todo_in_4"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass

    if event == "todo_b5":
        if bool(values["todo_day_5"]) and bool(values["todo_in_5"]) == True:
            todo_day = values["todo_day_5"]
            todo_in = values["todo_in_5"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_5"].update("")
            window["todo_in_5"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass

    if event == "todo_b6":
        if bool(values["todo_day_6"]) and bool(values["todo_in_6"]) == True:
            todo_day = values["todo_day_6"]
            todo_in = values["todo_in_6"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_6"].update("")
            window["todo_in_6"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass

    if event == "todo_b7":
        if bool(values["todo_day_7"]) and bool(values["todo_in_7"]) == True:
            todo_day = values["todo_day_7"]
            todo_in = values["todo_in_7"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_7"].update("")
            window["todo_in_7"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass
    if event == "todo_b8":
        if bool(values["todo_day_8"]) and bool(values["todo_in_8"]) == True:
            todo_day = values["todo_day_8"]
            todo_in = values["todo_in_8"]

            insert_log_todo(todo_day,todo_in)
            window["todo_day_8"].update("")
            window["todo_in_8"].update("")
        else:
            sg.popup("'日付'と'やること'を入力して下さい")
            pass
    #履歴内の要素を削除する
    if event == "del_2":
        delete_log()
    
    #やることリストの要素を削除する
    if event in ("削除","del_1"):
        delete()
    #window["table"].update(values = select())
    

