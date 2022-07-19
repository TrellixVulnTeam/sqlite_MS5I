import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image

sg.theme('LightBlue')

layout = [
        [sg.Text('Realtime movie', size=(40, 1), justification='center', font='Helvetica 20',key='-status-')],
        [sg.Text('Camera number: ', size=(8, 1)), sg.InputText(default_text='0',  size=(4, 1),key='-camera_num-')],
        [sg.Image(filename='', key='image')],
        [sg.Button('Start', size=(10, 1), font='Helvetica 14',key ='-start-'),
            sg.Button('Stop', size=(10, 1), font='Helvetica 14',key = '-stop-'),
            sg.Button('Exit', size=(10, 1), font='Helvetica 14', key='-exit-'), ]
        ]


window = sg.Window('Realtime movie',layout, location=(100, 100))


recording = False

while True:
    event, values = window.read(timeout=20)
    if event in (None, '-exit-'):
        break

    elif event == '-start-':
        window['-status-'].update('Live')
        camera_number = int(values['-camera_num-'])
        img = cv2.imread("onono.jpg")
        img = Image.open(img)
        print(img)
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
        ret, frame = img.read()
        if ret is True:
            imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
            window['image'].update(data=img)

window.close()