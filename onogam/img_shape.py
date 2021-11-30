import cv2
import numpy as np
import sys
img = cv2.imread(r"C:\Users\onoga\desktop\MyDocker\Git\origin\test\pos\ok_1.png")

class PointList():
    def __init__(self, npoints):
        self.npoints = npoints
        self.ptlist = np.empty((npoints, 2), dtype=int)
        self.pos = 0

    def add(self, x, y):
        if self.pos < self.npoints:
            self.ptlist[self.pos, :] = [x, y]
            self.pos += 1
            return True
        return False



#画像高さを取得
height = img.shape[0]
#画像幅を取得
width = img.shape[1]
print(height,width)

cv2.line(img, (0,0), (width, height),(255,255,0),5)
cv2.rectangle(img, (100,20),(120,50),(0,0,255),1)
count = 0
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

    if count >2:
        sys.exit()
            
def event_mouse(event, x, y,a,b):
    global n1 , n2 , count
    n1 = x
    n2 = y
    if event == cv2.EVENT_LBUTTONDOWN:
        count += 1
    if count == 2:
        print(n1, n2)
        
        return n1,n2
        
cv2.imshow("", img)
#npoints = 4
#ptlist = PointList(npoints)

list = cv2.setMouseCallback("", event_mouse,)

cv2.imshow("", img)
cv2.waitKey()
cv2.destroyAllWindows()