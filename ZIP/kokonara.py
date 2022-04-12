import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

sg.theme(new_theme="LightGrey1")

sg.set_options(dpi_awareness=True,use_ttk_buttons=True,)

listut = ["バルセロナ","レアルマドリード","チェルシー","バイエルンミュンヘン","リヴァプール","マンチェスターシティ"]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


lay = [
    [sg.Input(),sg.Button("選択")],
    #[sg.Listbox(listut,size=(30,6)),sg.Image("soccer.png",)],
    [sg.Radio("リンゴ",group_id="A"),sg.Radio("ゴリラ",group_id="A"),sg.Radio("ラッパ",group_id="A")],
    [sg.Multiline(size=(40,8))],
    [sg.Button("change",key = "change")],
    [sg.Checkbox("A"),sg.Checkbox("B")],
    [sg.Menu([["ファイル",["aaa"]],["編集"],["表示"],["オプション"]],tearoff=False,background_color="white",text_color=("black"))],
    [sg.Canvas(key="canvas")],
    
    
]

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111)
ax.set_ylim(-10, 10)




window = sg.Window("サンプル",lay,finalize=True)

fig_agg = draw_figure(window['canvas'].TKCanvas, fig)

fig_agg.draw()
while True:
    event,values = window.read()
    
    if event == None:
        break
    
    if event == "change":
        pass