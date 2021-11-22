import cv2
import numpy as np

img = cv2.imread(r"C:\Users\60837\Desktop\Resized\PXL_20211109_071617813.jpg")

def onMouse (event, x, y, flags, params):
    
     
    if event == cv2.EVENT_LBUTTONDOWN:# レフトボタンをクリックしたとき、ptlist配列にx,y座標を格納する 
 
        crop_img = img[[y], [x]]
        b_val = crop_img.T[0].flatten().mean()
        g_val = crop_img.T[1].flatten().mean()
        r_val = crop_img.T[2].flatten().mean()
        #print(f"R:{r_val},G:{g_val},B:{b_val}")
        print("x:",x, "y:",y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), 3)
        cv2.circle(img, (x, y), 1, (0, 0, 255), 3)
        #cv2.line(img,(x,y),(0,y),(0,255,0),thickness=2)
        #cv2.line(img,(x,y),(x,0),(0,255,0),thickness=2)
        cv2.imshow("", img)
            
        
        
        #マウスの位置に青線を追加する
    if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
        img2 = np.copy(img)
        h, w = img2.shape[0], img2.shape[1]
        cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
        cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
        cv2.imshow("", img2)
            
cv2.imshow("",img)

cv2.setMouseCallback("",onMouse)
cv2.waitKey(0)