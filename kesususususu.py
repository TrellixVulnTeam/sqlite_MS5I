import PySimpleGUI as sg


column = sg.Column(
    [[sg.pin(sg.Frame('', [[
        sg.T(str(i)), sg.OK(), sg.Cancel()]],
        key=str(i), visible=False))] for i in range(10)],
    scrollable=True, vertical_scroll_only=True, size=(300, 330))
layout = [[column]] + [
    [sg.Button('Add row', key='-B1-')] + [sg.Button('Del row', key='-B2-')]
]


window = sg.Window('Window Title', layout)
i = 0
while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == '-B1-':
        if i > 9:
            i = 9
        window[str(i)](visible=True)
        i += 1
        column.contents_changed()
    if event == '-B2-':
        i -= 1
        if i < 0:
            i = 0
        window[str(i)](visible=False)
        column.contents_changed()
window.close()