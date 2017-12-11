import src.Upsize
import numpy as np

class adjust_img(object):
    def __init__(self,img_src,img_tar,shape):
        self.src_img=img_src
        self.tar_img=img_tar
        self.src_hw=img_src.shape[:2]
        self.tar_hw=img_tar.shape[:2]
    def adjust(self):
        src_max=np.max(self.src_hw)
        tar_max=np.max(self.tar_hw)
        up2size= src_max if src_max>tar_max else tar_max






img = cv2.imread("./replace_bg/3.jpg")
rows, cols, channels = img.shape
np.set_printoptions(threshold=1e6)

src_img = np.asarray(cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY))

img = Upsize(src_img, (512, 512)).upresize()
import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()
