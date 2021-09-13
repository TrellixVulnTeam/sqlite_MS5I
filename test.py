from sys import winver
import PySimpleGUI as sg
import sqlite3
import datetime

from PySimpleGUI.PySimpleGUI import SELECT_MODE_EXTENDED
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

la_1=sg.Tab("tab_1",[      
                [sg.Multiline(key="in")],
                [sg.Table(values=lib_name,enable_events=True,key="table",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=col_name,
                    justification="left",auto_size_columns=False,num_rows=10)],
                [sg.Button("完了",key="comp")],
                [sg.Menu(menu_definition=[["追加",["タスクを追加する","削除"],]],background_color="white")]])

la_2=sg.Tab("履歴",[
                [sg.Multiline(key="in_2")],
                [sg.Table(values=select_log(),enable_events=True,key="log",col_widths=[13,30],background_color="white",text_color="black",select_mode="extended",headings=col_name,
                justification="left",auto_size_columns=False,num_rows=10)]])
lay =[
    [sg.TabGroup([[la_1,la_2]])]
    
]

window = sg.Window("タスク管理",lay,finalize=True,)


while True:
    
    event,values = window.read()
    
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
    
    
    
    
  
    if event == "削除":
        delete()
    #window["table"].update(values = select())
    

