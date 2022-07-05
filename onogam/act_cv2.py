import cv2
import os
import numpy as np

#第1引数:ディレクトリpath 第2引数:アスペクト比指定(長辺)
def resize_img(dir_path,size):
    os.chdir(dir_path)
    file_list = os.listdir()
    act_list = []
    for file_name in file_list:
        name = os.path.abspath(file_name)
        act_list.append(name)
        
    for i in act_list:
        
        img = cv2.imread(i)
        
        # リサイズしたい長い辺のサイズ
        re_length = size

        #縦横サイズを取得(px) h= 縦幅　w=横幅
        h, w = img.shape[:2]

        # 変換する倍率を計算
        re_h = re_w = re_length/max(h,w)
        #リサイズする
        img2 = cv2.resize(img, dsize=None, fx=re_h, fy=re_w)
        #画像を保存
        cv2.imwrite(i,img2)
        
buf = np.fromfile(r"C:\Users\60837\Desktop\画像\pos\post_4.jpg", np.uint8)
img = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED)        

iii = cv2.imread(r"C:\Users\60837\Desktop\画像\pos\post_4.jpg")
cv2.imshow("",img)
cv2.waitKey(0)


#resize_img(r"C:\Users\60837\Desktop\fu",500)