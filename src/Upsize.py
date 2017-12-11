import cv2
import  numpy as np

class Upsize(object):
    def __init__(self,imge_data,shape=(256,256,3)):
        self.img = imge_data
        self.tar_shape=shape
        self.src_shape=imge_data.shape
        self.channels =1 if len(self.src_shape)>2 else 0

    def resize(self):
        #flag to determine if the target shape is large than orignal shape
        flag=0
        if(self.channels):
            imge_h, imge_w, channels = self.img.shape

        else:
            imge_h, imge_w = self.img.shape
            channels=1

        if(self.tar_shape[0]>= self.src_shape[0] and self.tar_shape[1]>=self.src_shape[1]):
            rest = np.zeros(self.tar_shape, dtype=np.uint8)
            imgh_half = imge_h // 2
            imgw_half = imge_w // 2
            if(channels>1):
                for c in range(channels):
                    for row in range(imge_h):
                        for col in range(imge_w):
                            rest[row + self.tar_shape[0] // 2 - imgh_half, \
                                 col + self.tar_shape[1] // 2 - imgw_half,c] = self.img[row, col, c]
            else:
                for c in range(channels):
                    for row in range(imge_h):
                        for col in range(imge_w):
                            rest[row + self.tar_shape[0] // 2 - imgh_half,\
                                 col + self.tar_shape[1] // 2 - imgw_half] = self.img[row, col]

            return rest
        else:
            print("Target shape should be larger than original")
            return 0




img=cv2.imread("./replace_bg/3.jpg")
rows,cols,channels = img.shape
np.set_printoptions(threshold=1e6)

src_img = np.asarray(cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY))

img=Upsize(src_img,(512,512)).resize()
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()
