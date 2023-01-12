import cv2
import sys

videoPath = 'C:/Users/meoheee/Documents/devlab/aicosshackathon/test.mp4'
count = 0
framecount = 0

cap = cv2.VideoCapture(videoPath)
imgName = []

while (cap.isOpened()):
    ret, image = cap.read()

    if ret:
        cv2.imshow('video', image)  # cv2.imshow - 이미지보기

        # cv.waitKey() 함수는 프레임을 표출하는 시간을 정의
        # 이때 단위는 밀리초, 즉 천분의 1초
        if cv2.waitKey(1) & 0xFF == ord('q'):  # q를 누르면 영상이 종료됨
            break
        if framecount%10==0:
            cv2.imwrite("frame%d.jpg" % count, image)  # cv2.imwrite - 이미지저장
            imgName.append("frame%d.jpg" % count)
            print("frame%d.jpg" % count)
            count += 1
        framecount += 1
    else:
        break
print("이미지 추출 완료")
cap.release()  # 오픈된 비디오 파일을 닫는다.
cv2.destroyAllWindows()
imgs = []
for name in imgName:
    img = cv2.imread(name)

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)
print("이미지 입력 완료")
# 객체 생성
stitcher = cv2.Stitcher_create()

# 이미지 스티칭
status, dst = stitcher.stitch(imgs)
print("이미지 스티칭 완료")
if status != cv2.Stitcher_OK:
    print('Stitch failed!')
    sys.exit()

# 결과 영상 저장
cv2.imwrite('output.jpg', dst)

# 출력 영상이 화면보다 커질 가능성이 있어 WINDOW_NORMAL 지정
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
print("window normal")
cv2.imshow('dst', dst)
cv2.waitKey(10000)
cv2.destroyAllWindows()


