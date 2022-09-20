#from itertools import count
import cv2
import datetime

count = 1



# VideoCapture を作成する。
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#解像度変更  
cap.set(cv2.CAP_PROP_FPS, 30) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100) 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter を作成する。
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
writer = cv2.VideoWriter(f"output{count}.mp4", fourcc, fps, (width, height))

d = datetime.datetime.now()
while True:
    
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    cv2.imshow("",frame)
    if not ret:
        break  # 取得に失敗した場合
    if ret == True:
        writer.write(frame)
        
        if (datetime.datetime.now() -d).seconds >= 6:
            writer.release()
            
            writer = cv2.VideoWriter(f"output{count}.mp4", fourcc, fps, (width, height))
            count+=1
            d = datetime.datetime.now()
            writer.write(frame)
            
            continue
            
            
    
    
    
    
    
    #writer.write(frame)  # フレームを書き込む。
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

writer.release()
cap.release()