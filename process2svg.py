import cv2
import os
from src.adjust_wh import *
from src.binaryMinAreaRect import *
from PIL import Image
import argparse
def process_img(filname):
    img=Image.open(filname)
    img_mat=np.asmatrix(img.convert('1'),dtype=np.uint8) # convert image to black and white
    #delete the top left bottom and right white place
    img_box = binaryMinAreaRect(img_mat).get_box()
    print("Filename:%s,image box:%s"%(filname,img_box))
    #cut the mimAreacRect from img
    img = img.crop((img_box))
    img = cv2.bilateralFilter(np.asarray(img).astype(np.uint8), 9, 10, 40)
    return img

def fetch_file_name(file_path,fmt):
    Names = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if os.path.splitext(file)[1] == fmt:
                Names.append(os.path.join(root, file))
    return Names

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-path', type=str, default='./',
                        help='load image path')
    parser.add_argument('-fmt', type=str, default='.jpg',help='process pictures is fmt')
    ret = parser.parse_args()
    Names = fetch_file_name(ret.path, ret.fmt)
    for file_path in Names:
        img=process_img(file_path)
        result=Image.fromarray(img)

        saveFilename=os.path.split(file_path)[1].split('.')[0]
        savePath=os.path.split(file_path)[0]
        savename=os.path.join(savePath,saveFilename+".bmp")
        svg_savepath=savePath+'/'+saveFilename+'.svg'
        print("Saved fileName:%s"%(savename))
        result.save(savename)
        potrace="potrace --svg %s -o %s"%(savename,svg_savepath)
        print(potrace)
        os.system(potrace)