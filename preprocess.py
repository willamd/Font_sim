import cv2
import numpy as np
from matplotlib import pyplot as plt
# img = cv2.imread("/home/william/Download/lfj/004.png")

# dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,7)
#
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()
#
# cv2.waitKey(0)
from skimage.feature import match_template
from skimage import color
from PIL import  Image
img1 = Image.open("/home/william/Download/lfj/004.jpg")
img2 = Image.open("/home/william/Download/lfj/005.jpg")
img1=color.rgb2gray(img1)
img2=color.rgb2gray(img2)
print(img2)
result=match_template(img1,img2)
print(result)

