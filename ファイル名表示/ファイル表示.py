
from hashlib import new
import PySimpleGUI as sg
import os 
import time
import subprocess

#テーマ設定
sg.theme("LightGrey1")
#オプション設定
sg.set_options(use_ttk_buttons=True,dpi_awareness=True,font=("meiryo",8),)

#ユーザーセッティング
Setings = sg.UserSettings(filename="setings_file",path=os.path.split(__file__)[0])
Setings.load()

#フォルダ内ファイル検索　try→　そのまま返す　except→　実行ファイルのあるフォルダを返す
def file_serrch(path):
    try:
        list = os.listdir(path)
        return list
    except:
        return os.listdir(os.path.split(__file__)[0])
#ユーザーセッティングが未記入の場合　実行ファイルのあるディレクトリを表示させる 
def lis_res():
    try:
        list = file_serrch(Setings["dir_path"])
        return list
    except:
        return os.listdir(__file__)


lis = lis_res()

lay = [
    [sg.Text("★表示するフォルダを選択★",background_color="#00ffff")],
    [sg.InputText(default_text=Setings["dir_path"],key="dir_path",size=(40,1)),sg.FolderBrowse("選択",key="change",tooltip="表示したいフォルダを選択して下さい"),sg.Button("保存",image_filename="フロッピーアイコン.png",
                                                                                                                            button_color="white",mouseover_colors=("yellow","#1e90ff"),tooltip="フォルダ変更保存",key="save")],
    [sg.Button("選択フォルダへ移動",key="send_dir")],
    
    [sg.Listbox(values=lis,enable_events=True,size=(50,20),key="list")],
]

Window = sg.Window(title="ファイル表示",layout=lay,)

while True:
    event, value = Window.read(timeout=1000)
    
    if event == None:
        break
    
    
    
    #フォルダが選択されていなかったらホップアップを表示させる
    if value["dir_path"] == "":
        time.sleep(1.5)
        sg.popup("フォルダを選択して下さい")
    #保存ボタンを押すとセッティングファイルを更新する
    if event == "save":
        Setings["dir_path"] = value["dir_path"]
    #選択フォルダへ移動ボタンを押すとフォルダを表示する
    if event == "send_dir":
        os.chdir(value["dir_path"])#カレントディレクトリを変更
        sg.execute_command_subprocess("explorer",".")#カレントディレクトリを開く
    #非同期処理の内容記述
    new = len(Window["list"].get_list_values())
    if event == "__TIMEOUT__":
        file_serrch(Setings["dir_path"])
        Window["list"].update(values = file_serrch(value["dir_path"]))
        
        
        #ファイル追加の通知
        old = len(Window["list"].get_list_values())
        
        if new < old:
            
            #通知
            notify = sg.popup_notify("{0}フォルダーに\n新しいファイルが追加されました".format(os.path.split(value["dir_path"])[1]))
            
            #ポップアップ表示
            Popup = sg.popup_ok_cancel("{0}フォルダーに\n新しいファイルが追加されました\nフォルダへ移動しますか？".format(os.path.split(value["dir_path"])[1]),
                            )
            
            if Popup == "OK":
                os.chdir(value["dir_path"])#カレントディレクトリを変更
                sg.execute_command_subprocess("explorer",".")#カレントディレクトリを開く
            else:
                pass
            
            
  
    
        

