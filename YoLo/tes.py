
import cv2
import torch



model = torch.hub.load("yolov5", "custom",path=r"C:\Users\60837\Desktop\YoLo\periperi.pt",source="local")
model.conf = 0.8  #閾値を変更できる
img = cv2.imread(r"C:\Users\60837\Desktop\YoLo\neg_7.jpg")
img_1 = cv2.imread(r"C:\Users\60837\Desktop\YoLo\pos_155.jpg")
#result = model(img)
result_1 = model(img_1)

#UU =result.render()#

result_1.show()#処理結果画像を表示
#result.save(save_dir="teet.jpg")#処理画像を保存
#fdf = result.print()

#print(len(result.xyxy[0])) #検出個数
#print(len(result_1.xyxy[0])) #検出個数

#result.display(show=True,save=True)
#ii = result.display(pprint=True)


def main():
    model = torch.hub.load(r'ultralytics/yolov5', 'yolov5s') 

    while True:
        img=cv2.VideoCapture(0)

        result = model(img)
        result.render()
        cv2.imshow("test",result.imgs[0])
        k = cv2.waitKey(1) & 0xFF
        if(k == ord('q')):
            break
        
