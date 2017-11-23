from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,QRectF
from PyQt5.QtGui import  QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene,QLabel,QFileDialog,QGraphicsView,QVBoxLayout,QMainWindow
from ImageCompare_UI import Ui_MainWindow
import sys

def itemSelected(self):
    print("Selection changed")
app = QApplication(sys.argv)
grview = QGraphicsView()
scene = QGraphicsScene()
scene.addPixmap(QPixmap('22.jpg'))
grview.setScene(scene)
scene.selectionChanged.connect(itemSelected)
grview.show()
sys.exit(app.exec_())