import whisper
import PySimpleGUI as sg

sg.set_options(dpi_awareness=True,use_ttk_buttons=True)

list_value = ["tiny","base","small","medium","large"]

lay = [
    [sg.Text("ファイルを選択"),sg.InputText(key="in_file",size=(20,1)),sg.FileBrowse("ファイル選択")],
    [sg.Text("モデルを選択"),sg.Combo(values=list_value,auto_size_text=True,key="model")],
    [sg.Button("START",key="START")],
    [sg.Multiline(size=(50,10),key="out")],
]

window = sg.Window("",lay)

while True:
    event, value = window.read()
    if event == None:
        break
    
    def main (model,file):
        model = whisper.load_model(model)
        result = model.transcribe(file)
        

        #f = open("out.txt", "w")
        #f.write(result["text"])
        return result["text"]
    
    if event == "START":
        OUT = main(value["model"],value["in_file"])
        window["out"].update(OUT)
