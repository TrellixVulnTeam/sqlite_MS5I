import pyminizip
import os
import PySimpleGUI as sg

#when = "C://Users//onoga//Desktop//MyDocker//venvs//zip//戦国//"
#zip = pyminizip.compress("python統計まとめ.xlsx".encode("shift-jis"),"",f"{when}python統計まとめ.xlsx.zip".encode("shift-jis"),"daiwakasei",0)


#pyminizip zipファイル
def zip_start(file_name, out_path, password):
    
    input_file_name = os.path.split(file_name)[1]
    #拡張子なし
    none_file = os.path.splitext(input_file_name)[0]
    
    ZIP = pyminizip.compress(f"{file_name}".encode("shift_jis"), "", f"{os.path.join(out_path,none_file)}.zip".encode("shift_jis"), password, 0)

lay = [
    [sg.InputText(key="in"),sg.FileBrowse("選択")],
    [sg.Text("保存先を選択")],
    [sg.InputText(key = "save_input"),sg.FolderBrowse("選択")],
    [sg.Button("開始",key="start")],
]

window = sg.Window("",lay)

while True:
    
    event,values = window.read()
    if event == None:
        break
    
    if event == "start":
        
        zip_start(values["in"], values["save_input"], "daiwakasei")