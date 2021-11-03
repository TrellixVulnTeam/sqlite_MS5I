
from pathlib import Path
from pdf2image import convert_from_path
import PySimpleGUI as sg
import subprocess
import openpyxl
import os

import glob
from PIL import Image as iim
from openpyxl.drawing.image import Image
import shutil
import re

#画面がぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
#オプション設定
sg.set_options(use_ttk_buttons=True)

#pyinstallerでexe化する時にエラーを回避する為の表記↓
_original_constructor = subprocess.Popen.__init__

def _patched_constructor(*args, **kwargs):
    for key in ('stdin', 'stdout', 'stderr'):
        if key not in kwargs:
            kwargs[key] = subprocess.PIPE

    return _original_constructor(*args, **kwargs)

subprocess.Popen.__init__ = _patched_constructor


#test_dirがCドライブに存在している場合は削除する
start = os.listdir("C:/")
for i in start:
    if i == "test_dir":
        shutil.rmtree(r"C:\test_dir")
    else:
        pass

#output_folder 作成
os.mkdir(r"C:\test_dir")

img_path = Path(r"C:\test_dir")

def main(name):
    try:
        file_path = name
        #ドラック＆ドロップしたファイル名の先頭に"file:///"と記載があるのでそのファイルを抽出
        if bool(re.match("file:///",file_path)) == True:
            #対象のファイルpathから"file:///"が無いpathに抽出
            file_path = re.split("file:///",file_path)[1]
        # PDFファイルのパス
        pdf_path = Path(file_path)
        
        #output_folder  path
        img_path=Path(r"C:\test_dir")

        #この1文で変換されたjpegファイルが、imageホルダー内に作られます。
        convert_from_path(pdf_path, output_folder=img_path,fmt='jpeg',output_file=pdf_path.stem,dpi=800,)
        #globでimageフォルダ内の絶対pathを取得
        get_name = glob.glob(r"C:\test_dir\*.jpg")

        
        #リサイズする画像パス
        image_path = Path(get_name[0])
        #ファイルの名前(ディレクトリパス、拡張子なし)
        file_name = pdf_path.stem
        #Pillowでリサイズする画像を開く
        im = iim.open(image_path)
        #画像をリサイズする
        im.thumbnail((im.width//4, im.height//4),resample=iim.LANCZOS)
        #リサイズした画像の保存ファイルパス
        img_file_neme = os.path.join(os.path.dirname(image_path),file_name+"-1"+ ".jpg")
        #リサイズした画像を保存する
        im.save(img_file_neme,quality = 100)

        #新しくワークシートを作成
        wbb= openpyxl.load_workbook(r"L:\部門_部署\生産準備課\金型・設備改良係共通〔管理者：荻野〕\不具合指示書回覧\【用紙5】金型修理改善依頼書原紙 RevB(仕入れ先用).xlsx")
        #シートを選択
        ws = wbb["金型修理改善依頼書"]

        #挿入する画像を指定
        img = Image(img_file_neme)


        #画像を挿入
        ws.add_image(img, "A1")
        #画像挿入したエクセルの保存ファイルパス
        ex_file_neme = os.path.join(os.path.dirname(image_path), file_name +".xlsx")
        #エクセルファイルを保存する
        wbb.save(ex_file_neme)
        #作成した画像を削除する
        os.remove(img_file_neme)#リサイズした画像
        os.remove(image_path)#リサイズする前の画像
        #変換先のフォルダを開く
        subprocess.Popen(["explorer",img_path],shell=True)
    except:
        sg.PopupError("変換できません")
        pass



lay = [[sg.Text("PDF→Excelファイルに変換したいPDFファイルを選択して下さい")],
       [sg.Text("※Excel変換後はファイルをデスクトップ等に移動させて下さい")],
       [sg.InputText(key="in"), sg.FileBrowse(button_text="ファイル選択",)],
       [sg.Button("Excel変換", key="ok"),sg.Button("変換先フォルダ", key="dir_open",pad=((50,0),(0,0)))]]

window = sg.Window(title="PDF→Excel変換", layout=lay, keep_on_top=True)


while True:
    event, values = window.read()

    if event == None:
        shutil.rmtree(r"C:\test_dir")
        break

    if event == "ok":
        x = values["in"]#inputtext内の情報を取得
        if x == "":#ファイルを選択していない状態で"ok"ボタンを押した際にcontinue
            continue
        else:

            main(x)
            continue

    if event == "dir_open":
        subprocess.Popen(["explorer", img_path],shell=True)
        continue
