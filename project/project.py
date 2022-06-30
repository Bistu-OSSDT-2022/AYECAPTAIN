import cv2  # opencv导入库
import pandas as pd  # 存储数据库

# 导入图片
img = cv2.imread("DSC2023.JPG")

a = []  # 创建数据数组
b = []
B = []
G = []
R = []

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 生成灰度图片


# 鼠标点击
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "Site:%d,%d" % (x, y)

        a.append(x)
        b.append(y)

        img_B = img[x, y, 0]  # BGR RGB
        img_G = img[x, y, 1]
        img_R = img[x, y, 2]

        img_RGB = "RGB:(%d,%d,%d)" % (img_R, img_G, img_B)

        B.append(img_B)
        G.append(img_G)
        R.append(img_R)

        cv2.circle(img, (x, y), 5, (0, 0, 0), thickness=6)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    5, (0, 100, 255), thickness=5)
        cv2.putText(img, img_RGB, (x, y + 150), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    4, (255, 100, 0), thickness=4)
        cv2.imshow('image', img)


cv2.namedWindow('image', 0)
cv2.setMouseCallback('image', on_EVENT_LBUTTONDOWN)
cv2.imshow('image', img)

cv2.waitKey(0)

# 保存数据
data = [a, b, B, G, R]
data = pd.DataFrame(data, index=['h', 'l', 'B', 'G', 'R'])
data.to_csv('E:/pythonProject/Data/Data.csv')
