import cv2

import matplotlib.pyplot as plt

그림BGR = cv2.imread("py.jpg")

그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)

그림흑백 = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2GRAY)



# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.

plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열

plt.imshow(그림RGB)

plt.xticks([]) # x축 좌표 숨김

plt.yticks([]) # y축 좌표 숨김



plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열

plt.imshow(그림흑백, cmap='gray')

plt.xticks([]) # x축 좌표 숨김

plt.yticks([]) # y축 좌표 숨김

print(그림흑백)


plt.show()