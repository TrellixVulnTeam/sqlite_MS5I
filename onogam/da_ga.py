import numpy as np
import cv2
"""
setMouseCallback関数を使えばマウスイベント時の処理をセットできる
cv2.setMouseCallback(画像, 関数名, 関数に渡すパラメータ)
マウスイベントが起こったとき、指定した関数に5つの引数が渡される
event：マウスイベントの種類
x：マウスイベントが起きたx座標
y：マウスイベントが起きたy座標
flags：マウスイベント時に押されていたボタンやキーの種類
param：setMouseCallbackの第三引数で設定したパラメータ
マウスイベントの種類
cv2.EVENT_MOUSEMOVE：マウスが移動した
cv2.EVENT_LBUTTONDOWN：マウスの左ボタンが押された
cv2.EVENT_RBUTTONDOWN：マウスの右ボタンが押された
cv2.EVENT_MBUTTONDOWN：マウスの中ボタンが押された
cv2.EVENT_LBUTTONUP：マウスの左ボタンを離した
cv2.EVENT_RBUTTONUP：マウスの右ボタンを離した
cv2.EVENT_MBUTTONUP：マウスの中ボタンを離した
cv2.EVENT_LBUTTONDBCLK：マウスの左ボタンがダブルクリックされた
cv2.EVENT_RBUTTONDBCLK：マウスの右ボタンがダブルクリックされた
cv2.EVENT_MBUTTONDBCLK：マウスの中ボタンがダブルクリックされた
マウスイベント時に押されていたボタンやキーの種類
cv2.EVENT_FLAG_LBUTTON：マウスの左ボタン
cv2.EVENT_FLAG_RBUTTON：マウスの右ボタン
cv2.EVENT_FLAG_MBUTTON：マウスの中ボタン
cv2.EVENT_FLAG_CTRLKEY：Ctrlキー
cv2.EVENT_FLAG_SHIFTKEY：Shiftキー
cv2.EVENT_FLAG_ALTKEY：Altキー
    
    """

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


def onMouse(event, x, y, flag, params):
    wname, img, ptlist = params
    if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
        img2 = np.copy(img)
        h, w = img2.shape[0], img2.shape[1]
        cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
        cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
        cv2.imshow(wname, img2)

    if event == cv2.EVENT_LBUTTONDOWN:  # レフトボタンをクリックしたとき、ptlist配列にx,y座標を格納する
        if ptlist.add(x, y):
            print('[%d] ( %d, %d )' % (ptlist.pos - 1, x, y))
            cv2.circle(img, (x, y), 3, (0, 0, 255), 3)
            cv2.imshow(wname, img)
        else:
            print('All points have selected.  Press ESC-key.')
        if(ptlist.pos == ptlist.npoints):
            print(ptlist.ptlist)
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[1][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[1][0], ptlist.ptlist[1][1]),
                     (ptlist.ptlist[2][0], ptlist.ptlist[2][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[2][0], ptlist.ptlist[2][1]),
                     (ptlist.ptlist[3][0], ptlist.ptlist[3][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[3][0], ptlist.ptlist[3][1]),
                     (ptlist.ptlist[0][0], ptlist.ptlist[0][1]), (0, 255, 0), 3)


if __name__ == '__main__':
    img = cv2.imread(r"C:\Users\onoga\desktop\MyDocker\Git\sqlite\onogam\ok\an1.png")
    wname = "MouseEvent"
    cv2.namedWindow(wname)
    npoints = 4
    ptlist = PointList(npoints)
    cv2.setMouseCallback(wname, onMouse, [wname, img, ptlist])
    cv2.imshow(wname, img)
    cv2.waitKey()
    cv2.destroyAllWindows()

