from PIL import Image
from functools import reduce
import numpy as np
import scipy.fftpack
#计算指纹
def a_hash(img):
    if not isinstance(img, Image.Image):
        img = Image.open(img)
    img = img.resize((8, 8), Image.ANTIALIAS).convert('L') #将image压缩为8*8,转化为灰度图
    avg = reduce(lambda x, y: x + y, img.getdata()) / (64*1)#对每个像素点的灰度累和,最后除以64,得到灰度的平均值
    #map对每个像素做判断,大于平均值为1,否则为0
    #enumerate函数返回一个列表的下标及该下标对应的元素,用tuple装起来: (index, element)
    #reduce,对每个元素右移对应的下标位,并且与前一个元素做或运算,最终得到的结果为一个
    # 64位的二进制数,每一位的0,1代表该位的像素灰度与平均像素灰度的比较结果
    return reduce(lambda x, y_z: x | (y_z[1] << y_z[0]),enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())) , 0)

#计算汉明距离,亦或后返回1的个数
def hamming(h1, h2):
    #直接对两个数按位做异或操作,这样得到一个64位的二进制数,该二进制数包含的1的个数,即为汉明距离
    h, d = 0, h1 ^ h2
    #求d中包含的1的个数
    while d:
        h += 1
        d &= d - 1
    return h

def d_hash(img,size=(8,8)):
    #比较相邻像素
    if not isinstance(img, Image.Image):
        img = Image.open(img)
    img = img.resize(size).convert('L') #将image压缩为8*8,转化为灰度图
    #map对每个像素做判断,大于下一个值为1,否则为0
    #enumerate函数返回一个列表的下标及该下标对应的元素,用tuple装起来: (index, element)
    #reduce,对每个元素右移对应的下标位,并且与前一个元素做或运算,最终得到的结果为一个
    # 64位的二进制数,每一位的0,1代表该位的像素灰度与平均像素灰度的比较结果
    pixels = np.asarray(img)
    # compute differences between columns
    diff = (pixels[:, 1:] > pixels[:, :-1])*1
    return reduce(lambda x, y_z: x | (y_z[1] << y_z[0]),enumerate(np.hstack(diff.tolist())), 0)

def p_hash(img,hash_size=8,highfreq_factor=4):
    #第一步，缩放尺寸
    #第二步，离散余弦变换，DCT系数求取
    #第三步，求取DCT系数均值（左上角8 * 8
    #第四步，计算哈希值。 * /
    img_size = hash_size * highfreq_factor
    if not isinstance(img, Image.Image):
        img = Image.open(img)
    image = img.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = np.asarray(image)
    dct = scipy.fftpack.dct(pixels)#DCT系数
    dctlowfreq = dct[:hash_size, :hash_size]
    avg = dctlowfreq.mean()
    diff = (dctlowfreq > avg)*1
    return reduce(lambda x, y_z: x | (y_z[1] << y_z[0]),enumerate(np.hstack(diff.tolist())), 0)
def hist_sim(img1,img2,size=(64,64),part_size=(8,8)):
    if not isinstance(img1, Image.Image) and not isinstance(img2,Image.Image):
        img1 = Image.open(img1)
        img2 = Image.open(img2)
    img1=img1.convert('L').resize(size)
    img2=img2.convert('L').resize(size)
    w,h = img1.size
    pw,ph = part_size
    assert  w % pw == h % ph ==0
    li = [img1.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]
    ri = [img2.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]
    #
    # lh = img1.histogram()
    # rh = img2.histogram()
    sim = sum( sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lp.histogram(), rp.histogram())) / len(lp.histogram()) for lp,rp in zip(li,ri) )/64
    return sim

if __name__ == '__main__':
    img1 = input('请输入第一张图片路径:')
    img2 = input('请输入第二张图片路径:')
    h1 = p_hash(img1)
    print(h1)
    h2 = p_hash(img2)
    print(h2)
    print ("两张图片的指纹汉明距离为:%s" % hamming(h1, h2))
    print(hist_sim(img1,img2))
