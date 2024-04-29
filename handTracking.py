# need do some thing to make it work
# pip install mediapipe
# pip install opencv-python

import cv2
import mediapipe as mp
import time

cap =cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

handLmsStyle = mpdraw.DrawingSpec(color=(0, 0, 255), thickness=5)
# 設定點的樣式 # 第一個參數為線條的顏色，第二個參數為線條的粗度  

handConStyle = mpdraw.DrawingSpec(color=(0, 255, 0), thickness=10)
# 設定連線的樣式 # 第一個參數為線條的顏色，第二個參數為線條的粗度

pTime = 0
ctIME = 0

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        # 取得圖片的高度和寬度
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                # 畫出手的landmarks # 第一個參數為圖片，第二個參數為landmarks，第三個參數為連線的樣式，第四個參數為landmarks的樣式，第五個參數為landmarks的大小
                
                # 印出所有點座標
                for i ,lm in enumerate(handLms.landmark):
                    # 取得landmarks的座標
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4 ,(0, 0, 255), 2)
                    # 畫出landmarks的座標 # 第一個參數為圖片，第二個參數為文字，第三個參數為座標，第四個參數為字型，第五個參數為大小，第六個參數為顏色，第七個參數為線條粗度
                    print(i, xPos, yPos)
 
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        # 畫出FPS # 第一個參數為圖片，第二個參數為文字，第三個參數為座標，第四個參數為字型，第五個參數為大小，第六個參數為顏色，第七個參數為線條粗度

        cv2.imshow("img", img)

    if cv2.waitKey(1) == ord('q'):
        break
