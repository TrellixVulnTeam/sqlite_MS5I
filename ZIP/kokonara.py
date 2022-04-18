import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import japanize_matplotlib
import pandas as pd


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
col = ["日付","高値","安値","始値","終値","出来高","調整済み終値"]
data = pdr.DataReader("HDV","yahoo","2020/01/01","2022/04/01")
DATA = pd.DataFrame(data)
DATA = DATA.reset_index()
DATA["Date"] = pd.to_datetime(DATA["Date"].values.tolist())

fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot()
#ax.set_ylim(-10, 10)

val = [["dd"],["bb"]]
head = ["夢"]

lay = [
    
    [sg.Input(),sg.Button("選択")],
<<<<<<< HEAD
    #[sg.Listbox(listut,size=(30,6)),sg.Image("soccer.png",),sg.Table(values=str(data["Open"]))],
=======

>>>>>>> fafa87a23602d9163cb25602c8c49d699a767945
    [sg.Radio("リンゴ",group_id="A"),sg.Radio("ゴリラ",group_id="A"),sg.Radio("ラッパ",group_id="A")],
    [sg.Checkbox("A"),sg.Checkbox("B")],
    #[sg.Multiline(size=(40,8))],
    [sg.Button("change",key = "change")],
    [sg.Table(values=DATA.round(2).values.tolist(),headings=col,auto_size_columns=False,border_width=5,col_widths=10,background_color="pink"),
         ],
    [sg.Menu([["ファイル",["aaa"]],["編集"],["表示"],["オプション"]],tearoff=False,background_color="white",text_color=("black"))],
    [sg.Canvas(key="canvas",size=(550,400),),sg.Listbox(listut,size=(30,6),),sg.Image("soccer.png",)],
    
    
]








window = sg.Window("サンプル",lay,finalize=True,grab_anywhere=True,)

fig_agg = draw_figure(window['canvas'].TKCanvas, fig)
plt.grid()
plt.xticks(rotation = 20)
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