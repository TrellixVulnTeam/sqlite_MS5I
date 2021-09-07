from PySimpleGUI.PySimpleGUI import execute_command_subprocess, execute_file_explorer
import PySimpleGUIQt as sg
import subprocess
lay=[
    [sg.InputText(key="in"),sg.FileBrowse()],
    [sg.Multiline(default_text="ここにドラックしてください",key="m")],
    [sg.Button("ok")]

]

window = sg.Window("",layout = lay)

exec = execute_command_subprocess(command="open")


while True:
    event,values = window.read()

    if event == None:
        break

    if event == "ok":
        subprocess.Popen(["start",values["m"]],shell=True)