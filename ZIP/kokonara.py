import PySimpleGUI as sg

sg.theme(new_theme="LightTeal")

sg.set_options(dpi_awareness=True,use_ttk_buttons="DEFAULT_TTK_THEME",)

listut = ["バルセロナ","レアルマドリード","チェルシー","バイエルンミュンヘン","リヴァプール","マンチェスターシティ"]



lay = [
    [sg.Input(),sg.Button("選択")],
    #[sg.Listbox(listut,size=(30,6))],
    #[sg.Radio("リンゴ",group_id="A"),sg.Radio("ゴリラ",group_id="A"),sg.Radio("ラッパ",group_id="A")],
    [sg.Multiline(size=(50,10))],
    [sg.Button("change",key = "change")],
    [sg.Checkbox("A"),sg.Checkbox("B")],
    [sg.Menu([["ファイル",["aaa"]],["編集"],["表示"],["オプション"]],tearoff=False,)],
    
    
]

window = sg.Window("サンプル",lay)

while True:
    event,values = window.read()
    
    if event == None:
        break
    
    if event == "change":
        pass