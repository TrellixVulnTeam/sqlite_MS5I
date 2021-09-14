
import PySimpleGUI as sg
import sqlite3
import datetime

from PySimpleGUI.PySimpleGUI import InputText

col_name  = ["更新時間","タスク名"]
sg.theme("BluePurple")
conn = sqlite3.connect("task.db")
c = conn.cursor()
# テーブル作成　　c.execute("create table main(nowtime text, name text)")

#c.execute("insert into main values(?,?)",("6/8","onogami"))
#テーブルに値をインサートする
def insert(name):
    time = datetime.datetime.now()
    nowtime = time.strftime("%Y-%m-%d %H:%M")
    c.execute("insert into main values(?,?)",(nowtime,name))
    conn.commit()

def insert_log(outtime,name):
    c.execute("insert into 'log' values(?,?)",(outtime,name))
    conn.commit()

def select():
    c.execute("select * from main")
    out = c.fetchall()
    return out

def select_log():
    c.execute("select * from 'log'")
    out = c.fetchall()
    return out

lib_name = select()

la_1=sg.Tab("やることリスト",[      
                [sg.Multiline(key="in")],
                [sg.Table(values=lib_name,enable_events=True,key="table",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=col_name,
                    justification="left",auto_size_columns=False,num_rows=10)],
                [sg.Button("完了",key="comp")],
                [sg.Menu(menu_definition=[["追加",["タスクを追加する","削除"],]],background_color="white")]])

la_2=sg.Tab("履歴",[
                [sg.Multiline(key="in_2")],
                [sg.Table(values=select_log(),enable_events=True,key="log",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=col_name,
                justification="left",auto_size_columns=False,num_rows=10)],
                [sg.Button("削除",key="del_2")]])

month_list = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月",]
week_list = ["日","月","火","水","木","金","土",]
la_3=sg.Tab("ToDoリスト",[
                [sg.Text("いつまでに"),sg.Text("やること",pad=(60,0))],
                [sg.InputText(key="todo_day_1",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_1"),sg.Button("完了",key="todo_b1")],
                [sg.InputText(key="todo_day_2",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_2"),sg.Button("完了",key="todo_b2")],
                [sg.InputText(key="todo_day_3",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_3"),sg.Button("完了",key="todo_b3")],
                [sg.InputText(key="todo_day_4",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_4"),sg.Button("完了",key="todo_b4")],
                [sg.InputText(key="todo_day_5",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_5"),sg.Button("完了",key="todo_b5")],
                [sg.InputText(key="todo_day_6",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_6"),sg.Button("完了",key="todo_b6")],
                [sg.InputText(key="todo_day_7",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_7"),sg.Button("完了",key="todo_b7")],
                [sg.InputText(key="todo_day_8",size=(10,0)),sg.CalendarButton("日付",format="%Y-%m-%d",month_names=month_list,day_abbreviations=week_list,),sg.InputText(size=(32,0),key="todo_in_8"),sg.Button("完了",key="todo_b8")],
                ])
lay =[
    [sg.TabGroup([[la_1,la_3,la_2]])]
    
]

window = sg.Window("タスク管理",lay,finalize=True,)


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

    #履歴のlog様をを削除する
    def delete_log():
        if values["log"] == []:
            sg.popup_ok("タブを選択してください")
            pass

        else:

            elem = window["log"].get()
            filename = elem[values["log"][0]]
            
            c.execute(f"delete from log where outtime = '{filename[0]}' and name = '{filename[1]}'")
            conn.commit()
            window["log"].update(values = select_log())
    print(event,values)
    if event == None:
        break
    
    #tableが選択されたときにタスク内容を表示させる
    if event == "table":
        get_value=window["table"].get()

        window["in"].update(get_value[values["table"][0]][1])
    
    if event == "log":
        get_value=window["log"].get()

        window["in_2"].update(get_value[values["log"][0]][1])

    if event == "comp":
        if values["table"] == []:
            sg.popup_ok("タブを選択してください")
            pass
        else:
            get_value = window["table"].get()
            outtime = get_value[values["table"][0]][0]
            log_name = get_value[values["table"][0]][1]
            insert_log(outtime,log_name)
            window["log"].update(values = select_log())
            delete()

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
    
    
    
    if event == "del_2":
        delete_log()
  
    if event == "削除":
        delete()
    #window["table"].update(values = select())
    

