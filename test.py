import io
import cv2
import numpy as np
from matplotlib import pyplot as plt

import PySimpleGUI as sg


def draw_plot(img_f):

    histgram = cv2.calcHist([img_f], [0], None, [256], [0, 256])
    plt.figure(figsize=(5, 5))
    plt.plot(histgram)
    plt.xlim([0, 256])
    plt.title('Histgram')
    item = io.BytesIO()
    plt.savefig(item, format='png')
    plt.clf()

    ### RuntimeWarning: More than 20 figures have been opened. 
    # Figures created through the pyplot interface (`matplotlib.pyplot.figure`) 
    # are retained until explicitly closed and may consume too much memory. 
    # (To control this warning, see the rcParam `figure.max_open_warning`).
    # このエラーが出るため　plt.close('all')を追加
    plt.close('all')

    return item.getvalue()


sg.theme('LightBlue')

layout = [
        [sg.Text('Realtime movie', size=(40, 1), justification='center', font='Helvetica 20',key='-status-')],
        [sg.Text('Camera number: ', size=(8, 1)), sg.InputText(default_text='0',  size=(4, 1),key='-camera_num-')],
        [sg.Image(filename='', key='image'), sg.Image(filename='', key='-hist_img-')],
        [sg.Button('Start', size=(10, 1), font='Helvetica 14',key ='-start-'),
            sg.Button('Stop', size=(10, 1), font='Helvetica 14',key = '-stop-'),
            sg.Button('Exit', size=(10, 1), font='Helvetica 14', key='-exit-'), ]
        ]


window = sg.Window('Realtime movie with histgram',layout, location=(100, 100))

recording = False

while True:
    event, values = window.read(timeout=20)
    if event in (None, '-exit-'):
        break

    elif event == '-start-':
        window['-status-'].update('Live')
        camera_number = int(values['-camera_num-'])
        cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        # cap = cv2.VideoCapture(camera_number) 
        recording = True

    elif event == '-stop-':
        window['-status-'].update("Stop")
        recording = False
        # 幅、高さ　戻り値Float
        W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(H,W)
        img = np.full((H, W), 0)
        # ndarry to bytes
        imgbytes = cv2.imencode('.png', img)[1].tobytes()
        window['image'].update(data=imgbytes)
        cap.release()
        cv2.destroyAllWindows()

    if recording:
        ret, frame = cap.read()
        if ret is True:
            imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
            window['image'].update(data=imgbytes)

            histbytes = draw_plot(frame)
            window['-hist_img-'].update(data=histbytes)

window.close()
