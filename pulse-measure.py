%matplotlib notebook

#インポート
import cv2
import numpy as np
import matplotlib.pyplot as plt



# VideoCaptureのインスタンスを作成する。
cap = cv2.VideoCapture(0)
y = np.array( [] )

while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)
    img = frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # 画像の輝度値を取得
    average_color_per_row = np.average(img, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    average_color = np.uint8(average_color)
    y = np.append( y, average_color[0] )
    
    #数値を200個取得したら終了
    if y.size == 200:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()

x = np.arange(0, 20, 0.1)

plt.plot(x, y)
plt.show()
