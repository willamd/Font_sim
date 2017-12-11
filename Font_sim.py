import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSizePolicy, QGraphicsScene
from ImageCompare_UI import Ui_MainWindow
from PIL import Image
import numpy as np
import imagehash
import matplotlib
matplotlib.use("Qt5Agg")# 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.colors as mcl
from matplotlib.figure import Figure
import random

class Imgcomp_ui(Ui_MainWindow,QMainWindow):#从自动生成的界面类继承

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)#设置界面
        ##set graphic view's mouse event
        self.ui.src_img_lab.mouseDoubleClickEvent = self.srcfile
        self.ui.tar_img_lab.mouseDoubleClickEvent = self.tarfile
        self.ui.src_img_lab.setScaledContents(True)
        self.ui.tar_img_lab.setScaledContents(True)
        #信号绑定
        self.ui.Compare_btn.clicked.connect(self.Image_Comp)
        self.src_img_data=None
        self.tar_img_data=None#to store the readed image data to compare the image difference"""
        self.ui.actionExit.triggered.connect(self.exitCall)


    def eventFilter(self, source, event):

        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
            source is self.ui.src_img_lab):
            # pos = event.pos()
            self.srcfile(event)
        elif (event.type() == QtCore.QEvent.MouseButtonDblClick and source is self.ui.tar_img_lab):
            # pos=event.pos()
            self.tarfile(event)
    def srcfile(self,eventtype=None):
        filename,_=QFileDialog.getOpenFileName(self,'Open File',"./","*.jpg ;; *.bmp;; *.png")
        if filename:
            pixmap = QPixmap(filename)
            self.ui.src_img_lab.setPixmap(pixmap)
            self.imge_open(filename, self.src_img_data)

    def tarfile(self,eventtype=None):
        filename,_=QFileDialog.getOpenFileName(self,'Open File',"./","*.jpg ;; *.bmp;; *.png")
        if filename:
            pixmap = QPixmap(filename)
            self.imge_open(filename,self.tar_img_data)
            self.ui.tar_img_lab.setPixmap(pixmap)
    def imge_open(self,file_name,obj):
        """the function is used  to compare the image difference"""
        img = Image.open(file_name)
        # print(np.asarray((img)))
        if obj is self.src_img_data:
            self.src_img_data=img
            # print(img)
        elif obj is self.tar_img_data:
            self.tar_img_data=img

    @pyqtSlot()
    def Image_Comp(self):
        src_p=imagehash.phash(self.src_img_data)
        tar_p=imagehash.phash(self.tar_img_data)
        src_d=imagehash.dhash(self.src_img_data)
        tar_d=imagehash.dhash(self.tar_img_data)
        src_a=imagehash.average_hash(self.src_img_data)
        tar_a=imagehash.average_hash(self.tar_img_data)
        src_w=imagehash.whash(self.src_img_data)
        tar_w=imagehash.whash(self.tar_img_data)
        phash=1.0-(src_p-tar_p)/len(src_p.hash)**2
        dhash=1.0-(src_d-tar_d)/len(src_d.hash)**2
        ahash=1.0-(src_a-tar_a)/len(src_a.hash)**2
        whash=1.0-(src_w-tar_w)/len(src_w.hash)**2
        self.ui.a_hash.setText(str(ahash))
        self.ui.d_hash.setText(str(dhash))
        self.ui.w_hash.setText(str(whash))
        self.ui.p_hash.setText(str(phash))
        self.ui.hist_sim.setText(str(self.hist_sim(self.src_img_data,self.tar_img_data)))
        data=self.image_comp_display(self.src_img_data,self.tar_img_data)
        self.ui.cover_percent.setText(str(data['cover']))
        dr = PlotCanvas(data)
        dr.plot()  # 画图
        graphicscene =QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.comapre_result.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.comapre_result.show()

    def hist_sim(self,img1,img2,size=(64,64),part_size=(8,8)):
        img1=img1.convert('L').resize(size,Image.ANTIALIAS)
        img2=img2.convert('L').resize(size,Image.ANTIALIAS)
        w,h = img1.size
        pw,ph = part_size
        assert  w % pw == h % ph ==0
        li = [img1.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]
        ri = [img2.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]
        sim = sum( sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lp.histogram(), rp.histogram())) / len(lp.histogram()) for lp,rp in zip(li,ri) )/size[0]
        return float("%.4f"%sim)

    def image_comp_display(self,src_img,tar_img,size=(160,160)):
        if src_img is not None and tar_img is not None:
            src_img_shape=np.asarray(src_img).shape[:2]
            tar_img_shape=np.asarray(tar_img).shape[:2]
            if(src_img_shape!=tar_img_shape):
                gray_src = np.asarray(src_img.convert('L').resize(size,Image.ANTIALIAS))
                gray_tar = np.asarray(tar_img.convert('L').resize(size,Image.ANTIALIAS))
            else:
                gray_src = np.asarray(src_img.convert('L'))
                gray_tar = np.asarray(tar_img.convert('L'))
            del src_img
            del tar_img
            # set color map to display the difference between img
            colors = ['black', 'green', 'red', 'yellow', 'blue', 'white', 'purple']
            bounds = [0, 1, 2, 3, 4, 5, 6]
            cmap = mcl.ListedColormap(colors)
            norm = mcl.BoundaryNorm(bounds, cmap.N)
            # If src[i,j]!=0 and tar[i,j]!=0 then append the i,j to comp_result[i,j]=1
            # else if src[i,j]!=0 and tar[i,j]=0 then append to comp_result[i,j]=2
            # else if src[i,j]=0 and tar[i,j]!=0 then append to comp_result[i,j]=3.
            H, W = gray_src.shape
            comp_result = np.zeros((W,H))
            # print(W,H)resize 按照W,H,np是高宽
            # np.set_printoptions(threshold=1e6)
            # print(gray_tar)
            # print(H,W
            for i in range(H):
                for j in range(W):
                    # print(i,j)
                    if gray_src[i, j] != 0 and gray_tar[i, j] != 0 and gray_src[i, j]>=127 and gray_tar[i, j]>=127:
                        comp_result[i, j] = 1
                    elif gray_src[i, j] != 0 and gray_tar[i, j] == 0:
                        comp_result[i, j] = 2
                    elif gray_src[i, j] == 0 and gray_tar[i, j] !=0:
                        comp_result[i, j] = 3
                    else:
                        # print(i,j)
                        comp_result[i, j] = 0
            cover_rate_src2tar=np.sum(comp_result == 1) / (np.sum(comp_result == 1) + np.sum(comp_result == 2))
            # print(comp_result)
            data={}
            data['result']=comp_result
            data['cmap']=cmap
            data['norm']=norm
            data['cover']=float("%.4f" % cover_rate_src2tar)
            return data


        else:
            print("Can not find img!")
            raise NameError
        # return comp_result,cmap,norm

    ###############################################################
    ##
    ##Design the menue bar
    ##
    ###############################################################
    def exitCall(self):
        sys.exit()

class PlotCanvas(FigureCanvas):

    def __init__(self,data, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes =self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.data=data

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    def plot(self):
        ax =self.axes
        test= ax.imshow(self.data['result'],cmap=self.data['cmap'],norm=self.data['norm'])
        self.fig.colorbar(test, ticks=[0, 1, 2, 3], label='0:Backgroud 1:Same 2:Src Much 3:Src Less')
        ax.set_title('Compare Result')
        self.draw()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    myui = Imgcomp_ui()#创建对话框
    myui.setWindowTitle("Img Comp")
    myui.show()#主窗体显示
    sys.exit(app.exec_())