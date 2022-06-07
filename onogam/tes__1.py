import tempfile
import cv2
import os 

img = cv2.imread(r"C:\Users\onoga\Desktop\MyDocker\Git\origin\test\pos\2.png")


with tempfile.NamedTemporaryFile(delete=True) as tf:
    cv2.imwrite(f"{tf.name}.jpg" , img)#一時ファイルに画像形式で書き込む
 
    tf.seek(0)#先頭に戻る
    os.chdir(os.path.split(tf.name)[0])#一時ファイルの位置にカレントディレクトリを移動する
    iii = cv2.imread(f"{tf.name}.jpg")#←これが重要　CV2で読み込む形式に変換
    cv2.imshow("" , iii)
    cv2.waitKey(0)
tf.close()

