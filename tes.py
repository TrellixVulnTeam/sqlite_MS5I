import PySimpleGUIQt as sg

lay = [
    [sg.Menu(menu_definition=[["追加",["タスクを追加する","削除"],]],background_color="white")],
    [sg.Button("ok")],
    [sg.Table(values=[[]],enable_events=True,key="table",size=(10,6),background_color="white",text_color="black")],
]

window = sg.Window("",lay)

while True:
    event,values = window.read()

    if event == None:
        break
    print(event)