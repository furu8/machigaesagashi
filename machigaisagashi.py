import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('img/1.jpg')
img2 = cv2.imread('img/2.jpg')
# img3 = cv2.imread('A_1.jpg')
# img4 = cv2.imread('A_2.jpg')
# img5 = cv2.imread('A_3.jpg')

# サイズ変更
# img1 = cv2.resize(img1, (1074, 1526)) # 1074, 1524
# img2 = cv2.resize(img2, (1074, 1526)) # 1074, 1526
# img1 = img1[2:1526, 0:1074]
# print(img1.shape)
# print(img2.shape)

# answer = np.empty([1524, 1074])
# for i in range(1524):
#     for j in range(1074):
#         if np.any((img3 == img4) < 10 ): # どれかが黒
#             img1[i, j] = 0
#         else:
#             img1[i, j] = 255

# cv2.imwrite('5.jpg', img1)
# cv2.imwrite('6.jpg', img2)

# グレースケールに変換
# img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
 
# 二値変換
# thresh = 100
# max_pixel = 255
# ret, img_dst1 = cv2.threshold(img_gray, thresh, max_pixel, cv2.THRESH_BINARY)

# 差分
img_diff = cv2.absdiff(img1, img2)
cv2.imwrite('img/A.jpg', img_diff)

# cv2.imshow("a", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 合成
#dst = cv2.addWeighted(img2, 0.5, img1, 0.5, 128)
#cv2.imwrite('gousei.jpg', dst)
