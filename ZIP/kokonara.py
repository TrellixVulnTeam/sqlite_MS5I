import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import japanize_matplotlib


sg.theme(new_theme="LightGrey1")

sg.set_options(dpi_awareness=True,use_ttk_buttons=True,)

listut = ["バルセロナ","レアルマドリード","チェルシー","バイエルンミュンヘン","リヴァプール","マンチェスターシティ"]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    #ツールバー設置
    NavigationToolbar2Tk(figure_canvas_agg,canvas)
    return figure_canvas_agg

data = pdr.DataReader("HDV","yahoo","2020/01/01","2021/01/01")

fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot()
#ax.set_ylim(-10, 10)


lay = [
    [sg.Input(),sg.Button("選択")],
    [sg.Listbox(listut,size=(30,6)),sg.Image("soccer.png",),sg.Table(values=str(data["Open"]))],
    [sg.Radio("リンゴ",group_id="A"),sg.Radio("ゴリラ",group_id="A"),sg.Radio("ラッパ",group_id="A")],
    [sg.Checkbox("A"),sg.Checkbox("B")],
    #[sg.Multiline(size=(40,8))],
    [sg.Button("change",key = "change")],
    
    [sg.Menu([["ファイル",["aaa"]],["編集"],["表示"],["オプション"]],tearoff=False,background_color="white",text_color=("black"))],
    [sg.Canvas(key="canvas",size=(550,400),)],
    
    
]








window = sg.Window("サンプル",lay,finalize=True,grab_anywhere=True,)

fig_agg = draw_figure(window['canvas'].TKCanvas, fig)
plt.grid()
fig_agg.draw()
ax.plot(data["Open"].index,data["Close"],alpha=0.4)
ax.set_xlabel("日付")
ax.set_ylabel("株価")

fig_agg.draw()
while True:
    event,values = window.read()
    
    
    if event == None:
        break
    
    if event == "change":
        pass
        