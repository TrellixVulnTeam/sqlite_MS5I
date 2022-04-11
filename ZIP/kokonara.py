import PySimpleGUI as sg

sg.theme("LightBlue3")

sg.set_options(dpi_awareness=True,)

listut = ["バルセロナ","レアルマドリード","チェルシー","バイエルンミュンヘン","リヴァプール","マンチェスターシティ"]



lay = [
    [sg.Input(),sg.Button("選択")],
    [sg.Listbox(listut,size=(30,6))],
    [sg.Radio("リンゴ",group_id="A"),sg.Radio("ゴリラ",group_id="A"),sg.Radio("ラッパ",group_id="A")],
    [sg.Multiline(size=(50,10))],
    
    
]

window = sg.Window("サンプル",lay)

while True:
    event,values = window.read()
    
    if event == None:
        break