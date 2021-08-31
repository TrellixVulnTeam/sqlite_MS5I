import PySimpleGUI as sg

form = sg.FlexForm("Dynamic Combo")
layout = [[sg.Text('<-- Enlazar Clientes con Páginas web -->')],
    [sg.Text('Dominio: ')], [sg.InputText()],
    [sg.Text('URL del Cliente: (con http:// o https://)')], [sg.InputText()],
    [sg.Button("SELECCIONAR TODOS")], 
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Checkbox("something")], [sg.Checkbox("something")],
    [sg.Text('')],
    [sg.Submit('Ejecutar'), sg.Cancel('Salir')]
]

form = sg.Window('Enlazador de Páginas Web',grab_anywhere = True,layout=layout).read()