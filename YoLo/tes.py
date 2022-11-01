
import cv2
import torch


#model = torch.hub.load("yolov5", "custom",path=r"C:\Users\60837\Desktop\YoLo\periperi.pt",source="local")
#model = torch.hub.load("yolov5", "custom",path=r"C:\Users\onoga\Desktop\MyDocker\Git\sqlite\YoLo\baribari.pt",source="local")
#model.conf = 0.8  #閾値を変更できる
#img = cv2.imread(r"C:\Users\60837\Desktop\YoLo\neg_7.jpg")
#img_1 = cv2.imread(r"C:\Users\60837\Desktop\YoLo\pos_155.jpg")
#img = cv2.imread(r"C:\Users\onoga\Desktop\MyDocker\Git\sqlite\onogam\07_15\pos\pos_171.jpg")
#result = model(img)
#result_1 = model(img_1)

#UU =result.render()#
#result.show()
#result_1.show()#処理結果画像を表示
#result.save(save_dir="teet.jpg")#処理画像を保存
#fdf = result.print()

#print(len(result.xyxy[0])) #検出個数
#print(len(result_1.xyxy[0])) #検出個数

#result.display(show=True,save=True)
#ii = result.display(pprint=True)


def main(pt_path, conf):
    model = torch.hub.load("yolov5", "custom",path=pt_path ,source="local")
    #model = torch.hub.load("WongKinYiu/yolov7", r"yolov7")
    
    
    #--- 検出の設定 ---
    model.conf = conf #--- 検出の下限値（<1）。設定しなければすべて検出
    model.classes = [0] #--- 0:person クラスだけ検出する。設定しなければすべて検出
    #print(model.names) #--- （参考）クラスの一覧をコンソールに表示

    #--- 映像の読込元指定 ---
    #camera = cv2.VideoCapture("../pytorch_yolov3/data/sample.avi")#--- localの動画ファイルを指定
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)                #--- カメラ：Ch.(ここでは0)を指定
    
    #解像度の設定
    camera.set(cv2.CAP_PROP_FPS, 60) 
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 300) 


    #--- 画像のこの位置より左で検出したら、ヒットとするヒットエリアのためのパラメータ ---
    pos_x = 240

    while True:

        #--- 画像の取得 ---
        #  imgs = 'https://ultralytics.com/images/bus.jpg'#--- webのイメージファイルを画像として取得
        #  imgs = ["../pytorch_yolov3/data/dog.png"] #--- localのイメージファイルを画像として取得
        ret, imgs = camera.read()              #--- 映像から１フレームを画像として取得

        #--- 推定の検出結果を取得 ---
        #  results = model(imgs) #--- サイズを指定しない場合は640ピクセルの画像にして処理
        results = model(imgs,size=800) #--- 160ピクセルの画像にして処理
        
        #物体が検出されたらコンソールに文字を表示
        if len(results.xyxy[0]) > 0:
            print(True) 

        #--- 出力 ---
        #--- 検出結果を画像に描画して表示 ---
        #--- 各検出について
        for *box, conf, cls in results.xyxy[0]:  # xyxy, confidence, class

            #--- クラス名と信頼度を文字列変数に代入
            s = model.names[int(cls)]+":"+'{:.1f}'.format(float(conf))

            #--- ヒットしたかどうかで枠色（cc）と文字色（cc2）の指定
            if int(box[0])>pos_x :
                cc = (255,255,0)
                cc2 = (128,0,0)
            else:
                cc = (0,255,255)
                cc2 = (0,128,128)

            #--- 枠描画
            cv2.rectangle(
                imgs,
                (int(box[0]), int(box[1])),
                (int(box[2]), int(box[3])),
                color=cc,
                thickness=2,
                )
            #--- 文字枠と文字列描画
            cv2.rectangle(imgs, (int(box[0]), int(box[1])-20), (int(box[0])+len(s)*10, int(box[1])), cc, -1)
            cv2.putText(imgs, s, (int(box[0]), int(box[1])-5), cv2.FONT_HERSHEY_PLAIN, 1, cc2, 1, cv2.LINE_AA)

        #--- ヒットエリアのラインを描画
       #cv2.line(imgs, (pos_x, 0), (pos_x, 640), (128,128,128), 3)

        #--- 描画した画像を表示
        cv2.imshow('color',imgs)

        #--- （参考）yolo標準機能を使った出力 ---
        #  results.show()#--- yolo標準の画面表示
        #  results.print()#--- yolo標準のコンソール表示

        #--- （参考）yolo標準の画面を画像取得してopencvで表示 ---
        #  pics = results.render()
        #  pic = pics[0]
        #  cv2.imshow('color',pic)

        #--- 「q」キー操作があればwhileループを抜ける ---
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
main(pt_path=r"C:\Users\60837\Desktop\YoLo\periperi.pt", conf=0.6)
