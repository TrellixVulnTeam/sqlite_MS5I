
import PySimpleGUIQt as qt
import pyzipper as zip
import os
import zipfile
import sys

#lzh形式でファイルを圧縮　　引数（圧縮ファイル名,　パスワード,　圧縮したいファイルpath）
def lzh_file(new_name,password,file_path):
    #カレントディレクトリ変更
    os.chdir(os.path.split(file_path)[0])
    
    with zip.AESZipFile(f"{new_name}.lzh","w",encryption=zip.WZ_AES) as zf:
        
        #パスワード設定
        zf.setpassword(bytes(password,encoding="utf-8"))
        
        #圧縮したいファイルpathを指定 arcnameでファイル名を指定
        file_full_name = os.path.split(file_path)[1]
        gfd = os.path.split(file_full_name)[1]
        gfd = f"{gfd}"
        #gfd = gfd.encode('cp437').decode("cp437")
        
        print(gfd)
        out_file = zf.write(filename=f"{gfd}".encode("utf-8").decode("utf-8",errors="ignore"))
        print(f"{os.path.split(file_full_name)[1]}")
        
        #os.rename(out_file,"高橋")
        
#zip形式でファイルを圧縮　　引数（圧縮ファイル名,　パスワード,　圧縮したいファイルpath）
def zip_file(new_name,password,file_path):
    #カレントディレクトリ変更
    os.chdir(os.path.split(file_path)[0])
    
    with zip.AESZipFile(f"{new_name}.zip","w",encryption=zip.WZ_AES) as zf:
      
        #パスワード設定
        zf.setpassword(bytes(password,encoding="utf-8"))
        #圧縮したいファイルpathを指定 arcnameでファイル名を指定
        file_full_name = os.path.split(input_path)[1]
        
        zf.write(file_path,arcname=f"{os.path.split(file_full_name)[1]}")
        
#テーマ設定
qt.theme("LightGrey1")
        
#オプション設定
qt.set_options(icon="icon32.ico",font=("meiryo",10))
lay_1 = qt.Tab("ファイルのみ",[
    [qt.Text("➀圧縮したいファイルを選択して下さい",text_color="#dc143c")],
    [qt.InputText(key="file_input"),qt.FileBrowse(button_text="選択",size=(6,1),)],
    [qt.Text("➁保存形式を選択して下さい",pad=((100,100),(100,100)), text_color="#dc143c",)],
    [qt.Radio(text="lzh形式",group_id="A",key="file_lzh",default=True),qt.Radio(text="zip形式",group_id="A",key="file_zip")],
    [qt.Text("➂設定するパスワードを記載",text_color="#dc143c")],
    [qt.InputText(default_text="daiwakasei",password_char="*",key="password")],
    [qt.Button("ファイル変換",key="file_go")],

    
])

lay_2 = qt.Tab("フォルダ全て",[
    [qt.Text("➀圧縮したいファイルを選択して下さい",text_color="#dc143c")],
    [qt.InputText(key="folder_input"),qt.FileBrowse(button_text="選択",size=(6,1),)],
    [qt.Text("➁保存形式を選択して下さい",pad=((100,100),(100,100)), text_color="#dc143c",)],
    [qt.Radio(text="lzh形式",group_id="B",key="folder_lzh",default=True),qt.Radio(text="zip形式",group_id="B",key="folder_zip")],
    [qt.Text("➂設定するパスワードを記載",text_color="#dc143c")],
    [qt.InputText(default_text="daiwakasei",password_char="*",key="folder_password")],
    [qt.Button("フォルダ変換",key="folder_go")],
    
    
])

lay = [[qt.TabGroup([[lay_1,lay_2]])]]
window = qt.Window(title="Password設定",layout = lay,icon="icon32.ico",size=(400,200))

while True:
    event, values = window.read()
    
    if event == None:
        break
    
    if event == "file_go":
        if values["file_input"] == "":
            qt.popup("ファイルを選択して下さい")
            pass
        elif values["file_password"] == "":
            qt.popup("パスワードを入力して下さい")
            pass
        else:
            
            file_path = values["file_input"]
            #ドラッグ＆ドロップ時のfile:///を消去
            input_path = file_path.lstrip("file:///")
            
            #ファイルの名前(***.ico)
            file_full_name = os.path.split(input_path)[1]
            #拡張子なしファイルの名前
            file_name =  os.path.splitext(file_full_name)[0]
            
            if values["file_lzh"] == True:
                 
                lzh_file(f"{file_name}",password=values["file_password"],file_path=input_path)
                qt.popup("処理が完了しました",custom_text="閉じる")
                
            elif values["file_zip"] == True:
                
                zip_file(f"{file_name}",password=values["password"],file_path=input_path)
                qt.popup("処理が完了しました",custom_text="閉じる")
        
    
    if event == "folder_go":
          
        if values["folder_input"] == "":
            qt.popup("フォルダを選択して下さい")
            pass
        elif values["folder_password"] == "":
            qt.popup("パスワードを入力して下さい")
            pass
        
        else:
            file_path = values["folder_input"]
                #ドラッグ＆ドロップ時のfile:///を消去
            input_path = file_path.lstrip("file:///")
            #カレントで移動
            os.chdir(input_path)
            #フォルダ内のファイル一覧取得
            folder_list = os.listdir(input_path)
            
            for file in folder_list:
                #拡張子なしファイルの名前
                file_name =  os.path.splitext(file)[0]
                #ファイルのフルパス
                full_path = os.path.abspath(file)
                #lzhファイルの処理
                if values["folder_lzh"] == True:
                    lzh_file(f"{file_name}",password=values["folder_password"],file_path=full_path)
                    
                
                elif values["folder_zip"] == True:
                    zip_file(f"{file_name}",password=values["folder_password"],file_path=full_path)
                    
                    
            qt.popup("処理が完了しました",custom_text="閉じる")