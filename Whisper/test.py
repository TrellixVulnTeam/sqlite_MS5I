import whisper
import PySimpleGUI as sg
import subprocess


sg.theme("SystemDefaultForReal")

def GO (file_path):
    out = subprocess.run("whisper {0} --language ja --task transcribe --model tiny --output_dir {1}".format(file_path,r"C:\Users\onoga\Desktop\favicons"),shell=True,  stdout=subprocess.PIPE)#check=True
    out_put = str(out.stdout,"shift_jis")
    return out_put


sg.set_options(dpi_awareness=True,use_ttk_buttons=True,font=("デジタル",10))

Model_list = ["tiny.en","tiny","base.en","base","small.en","small","medium.en","medium","large"]
Language_list =["af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu","fa",
                "fi","fo","fr","gl","gu","ha","haw","hi","hr","ht","hu","hy","id","is","it","iw","ja","jw","ka","kk","km","kn","ko",
                "la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc","pa","pl","ps","pt",
                "ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th","tk","tl","tr","tt","uk","ur",
                "uz","vi","yi","yo","zh","Afrikaans","Albanian","Amharic","Arabic","Armenian","Assamese","Azerbaijani","Bashkir","Basque",
                "Belarusian","Bengali","Bosnian","Breton","Bulgarian","Burmese","Castilian","Catalan","Chinese","Croatian","Czech","Danish",
                "Dutch","English","Estonian","Faroese","Finnish","Flemish","French","Galician","Georgian","German","Greek","Gujarati",
                "Haitian","Haitian Creole","Hausa","Hawaiian","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Italian","Japanese",
                "Javanese","Kannada","Kazakh","Khmer","Korean","Lao","Latin","Latvian","Letzeburgesch","Lingala","Lithuanian","Luxembourgish",
                "Macedonian","Malagasy","Malay","Malayalam","Maltese","Maori","Marathi","Moldavian","Moldovan","Mongolian","Myanmar",
                "Nepali","Norwegian","Nynorsk","Occitan","Panjabi","Pashto","Persian","Polish","Portuguese","Punjabi","Pushto","Romanian",
                "Russian","Sanskrit","Serbian","Shona","Sindhi","Sinhala","Sinhalese","Slovak","Slovenian","Somali","Spanish","Sundanese",
                "Swahili","Swedish","Tagalog","Tajik","Tamil","Tatar","Telugu","Thai","Tibetan","Turkish","Turkmen","Ukrainian","Urdu",
                "Uzbek","Valencian","Vietnamese","Welsh","Yiddish","Yoruba"]

lay = [
    [sg.Frame("",[
    [sg.Text("task選択"),sg.Combo(values=["transcribe","translate"],default_value="transcribe")],
    [sg.Text("翻訳するファイルを選択"),sg.InputText(key="in_file",size=(20,1)),sg.FileBrowse("ファイル選択")],
    [sg.Text("学習モデルを選択"),sg.Combo(values=Model_list,auto_size_text=True,key="model")],
    [sg.Text("翻訳言語を選択"),sg.Combo(values=Language_list,size=(15,1),key="language")],
    [sg.Text("保存先のフォルダを選択"),sg.InputText(key="output_dir",size=(20,1)),sg.FolderBrowse("選択")],]),],
]


lay2 = [
    [sg.Frame("",[
    [sg.Multiline(size=(52,10),key="out")],])],
    [sg.Button("保存先のフォルダを開く")],
    [sg.Button("START",key="START")],
    ]


layout = [lay,lay2]

window = sg.Window("Whisper",layout)

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
        #OUT = main(value["model"],value["in_file"])
        #window["out"].update(OUT)
        window["out"].update(GO(value["in_file"]))
