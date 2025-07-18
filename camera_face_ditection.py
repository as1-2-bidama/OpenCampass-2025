import cv2

# 分類器
# cascade_path = 'C:\Users\bidam\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'

# 特徴量読み込み
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

# カメラ定義
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
def camera():
    # ビデオキャプチャ
    ret, frame = cap.read()
    # 顔検出
    faces = cascade.detectMultiScale(frame, scaleFactor=1.23, minNeighbors=3, minSize=(10, 10))
    # 検出した顔を囲む矩形の作成
    # for x, y, w, h in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (127, 255, 0), 2)
    # print(faces)
    # 表示q
    # cv2.imshow('frame', frame)

    # qが押されたら終了
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# カメラ終了
cap.release()
# ウィンドウ終了
# cv2.destroyAllWindows()