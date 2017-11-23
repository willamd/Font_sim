#compare to image's difference and display the same parts in one color and less part in another color
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcl
import cv2
img1=cv2.imread('22.jpg')
img2=cv2.imread('44.jpg')

print(img1.shape[:2])
if  img1 is not None and img2 is not None:

    img1=cv2.resize(img1,(64,64))
    img2=cv2.resize(img2,(64,64))
    gray_src = np.asarray(cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY))
    gray_tar = np.asarray(cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY))
    del img1
    del img2
    #set color map to display the difference between img
    colors = ['black','green','red','yellow','blue', 'white','purple']
    bounds = [0,1,2,3,4,5,6]
    cmap = mcl.ListedColormap(colors)
    norm = mcl.BoundaryNorm(bounds,cmap.N)
    #If src[i,j]!=0 and tar[i,j]!=0 then append the i,j to comp_result[i,j]=1
    #else if src[i,j]!=0 and tar[i,j]=0 then append to comp_result[i,j]=2
    #else if src[i,j]=0 and tar[i,j]!=0 then append to comp_result[i,j]=3.
    comp_result=np.zeros((64,64))
    W,H=gray_src.shape
    np.set_printoptions(threshold=1e6)
    # print(gray_tar)
    for i in range(H):
        for j in range(W):
            if gray_src[i,j]!=0 and gray_tar[i,j]!=0:
                comp_result[i, j]=1
            elif gray_src[i,j]!=0 and gray_tar[i,j]==0:
                comp_result[i,j]=2
            elif gray_src[i,j]==0 and gray_tar[i,j]!=0:
                comp_result[i, j] = 3
            else:
                comp_result[i,j]=0
    # print(other_point)
    # plt.imshow(comp_same,)
    print(np.sum(comp_result==1)/(np.sum(comp_result==1)+np.sum(comp_result==2)/2))
    colo=plt.imshow(comp_result,cmap = cmap,norm = norm)
    # plt.imshow(comp_same,cmap = cmap,norm = norm)
    # plt.imshow(com_src_less,cmap = cmap,norm = norm)
    # plt.imshow(other_point, cmap=cmap, norm=norm)
    # plt.imshow(com_src_less)
    plt.colorbar(colo, ticks=[0,1,2,3],label='0:Backgroud 1:Same 2:Src Much 3:Src Less')

    plt.draw()
    # plt.show()
    # fig = Figure(figsize=(90, 100), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
    # axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
    # colo=axes.imshow(comp_result,cmap = cmap,norm = norm)
    # # axes.draw(renderer=None)
    # axes.plot()


else:
    print("Can not find img!")
    raise NameError



colors = ['red','green','orange','blue']
bounds = [ 1, 2, 3, 4]

