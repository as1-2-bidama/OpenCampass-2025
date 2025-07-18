import pygame
import cv2
pygame.init()

screen = pygame.display.set_mode((1600,1200))
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
    return faces
image_inu = pygame.image.load('いぬ.png')
image_inu = pygame.transform.scale(image_inu,(1600,1200))
run = True
clock = pygame.time.Clock()
image = {}
for i in range(1,201):
    j = str(i).zfill(4)
    print(i,j)
    image[i] = pygame.image.load(f'./picture/{j}.png')
    # image[i] = pygame.transform.flip(image[i], True,True)

while run:
    screen.fill((0,0,0))
    clock.tick(60)
    face = camera()
    if len(face) != 1:
        screen.blit(image_inu, (0, 0))
    else:
        for x, y, w, h in face:
            print(x)
            if(x<400 and x > 0):
                screen.blit(image[int(int(x)/2)],(0,0))
    # pygameのイベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # ウィンドウが閉じられたら終了
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # 'q'キーが押されたら終了
                run = False
    pygame.display.update()  # 画面を更新






# カメラ終了
cap.release()
# ウィンドウ終了
# cv2.destroyAllWindows()