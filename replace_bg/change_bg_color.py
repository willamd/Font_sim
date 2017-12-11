import cv2
import  numpy as np
img=cv2.imread('a.jpg')
img_back=cv2.imread('23.jpg')

rows,cols,channels = img.shape

# #转换hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
np.set_printoptions(threshold=1e6)
# #获取mask
lower_red=np.array([0,0,0])
upper_red=np.array([115,125,125])
mask = cv2.inRange(hsv, lower_red, upper_red)

# 腐蚀膨胀
erode=cv2.erode(mask,None,iterations=1)
# cv2.imshow('erode',erode)
#膨胀
dilate=cv2.dilate(mask,None,iterations=5)
# 遍历替换
center=[50,50]#在新背景图片中的位置
for i in range(rows):
    for j in range(cols):
        if dilate[i,j]==255:#0代表黑色的点
            # print(np.round(img[i,j][0]/255))
            if np.round(img[i,j][0]/255)==1:
                img_back[center[0]+i,center[1]+j]=img[i,j]=np.round((img[i,j])/255)
            else:
                img_back[center[0] + i, center[1] + j] = np.ceil((img[i,j]+120)/255)*255
cv2.fastNlMeansDenoisingColored(img_back,img_back,32,20, 10, 21)

cv2.imwrite('test.jpg',img_back)
cv2.imshow('res',img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
