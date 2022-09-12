from tkinter.tix import ButtonBox
import PySimpleGUI as sg
import os
import subprocess

sg.theme("SystemDefault")

sg.set_options(font=("meiryo",8),use_ttk_buttons=True,dpi_awareness=True)

CD = os.getcwd()

lay_img = sg.Tab("画像",[
    [sg.Text("カレントディレクトリ"),sg.InputText(default_text=CD,key="img_cd",size=(30,1),readonly=True),sg.FolderBrowse("変更"),sg.Button("保存",key="img_save",button_color="#008000")],
    [sg.Text("検出する画像フォルダを選択"),sg.InputText(key="img_in",size=(30,1)),sg.FolderBrowse("選択")],
    [sg.Text("学習データを選択(.ptファイル)"),sg.InputText(key="img_pt",size=(30,1)),sg.FileBrowse("選択")],
    [sg.Text("判定の閾値 [--conf]"),sg.InputText(default_text=0.4, size=(10,1),key="img_conf")],
    [sg.Text("保存するディレクトリを指定"),sg.InputText(default_text="runs/detect",key="img_project",size=(30,1)),sg.FolderBrowse("選択")],
    [sg.Text("学習データを保存するディレクトリを指定"),sg.InputText(default_text="exp",key="img_dir_name",size=(20,1))],

    [sg.Button("START",key="START_IMG")],
    
])

lay_cap = sg.Tab("動画",[
    [sg.Text("学習データを選択(.ptファイル)"),sg.InputText(key="cap_pt",size=(30,1)),sg.FileBrowse("選択")],
    [sg.Text("判定の閾値 [--conf]"),sg.InputText(default_text=0.4, size=(10,1),key="cap_conf")],
    [sg.Text("画像のサイズ[--img]"),sg.InputText(default_text=640, size=(10,1),key="cap_img")],
    [sg.Button("START",key="cap_IMG")],
])

layout = [[sg.TabGroup([[lay_img,lay_cap]])]]

window = sg.Window("",layout=layout)
while True:
    event, value = window.read()
    
    if event == None:
        break
    #画像処理開始
    if event == "START_IMG":
        subprocess.run("python detect.py --source {0} --weights {1} --conf {2} --project {3} --name {4}".format(value["img_in"],value["img_pt"],value["img_conf"],value["img_project"],value["img_dir_name"]),shell=True)
    
    #カレントディレクトリを保存    
    if event == "img_save":
        CD = value["img_cd"]
        os.chdir(CD)
        window["img_cd"].update(CD)
        
    #動画処理開始
    if event == "cap_IMG":
        subprocess.run("python detect.py --source 0 --weights {0} --conf {1} --img {2}".format(value["cap_pt"],value["cap_conf"],value["cap_img"]),shell=True)
        