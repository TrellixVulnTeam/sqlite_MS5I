import PySimpleGUIQt as sg

lay = [[sg.InputText(),sg.Button("完了")]]

window = sg.Window("test",layout=lay).read()