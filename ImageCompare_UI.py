# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageCompare.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 570, 130))
        self.groupBox.setObjectName("groupBox")
        self.Compare_btn = QtWidgets.QPushButton(self.groupBox)
        self.Compare_btn.setGeometry(QtCore.QRect(0, 30, 99, 27))
        self.Compare_btn.setObjectName("Compare_btn")
        self.a_hash_lab = QtWidgets.QLabel(self.groupBox)
        self.a_hash_lab.setGeometry(QtCore.QRect(10, 70, 60, 20))
        self.a_hash_lab.setObjectName("a_hash_lab")
        self.d_hash_lab = QtWidgets.QLabel(self.groupBox)
        self.d_hash_lab.setGeometry(QtCore.QRect(10, 100, 60, 20))
        self.d_hash_lab.setObjectName("d_hash_lab")
        self.p_hash_lab = QtWidgets.QLabel(self.groupBox)
        self.p_hash_lab.setGeometry(QtCore.QRect(170, 70, 60, 20))
        self.p_hash_lab.setObjectName("p_hash_lab")
        self.hist_lab = QtWidgets.QLabel(self.groupBox)
        self.hist_lab.setGeometry(QtCore.QRect(330, 70, 60, 20))
        self.hist_lab.setObjectName("hist_lab")
        self.w_hash_lab = QtWidgets.QLabel(self.groupBox)
        self.w_hash_lab.setGeometry(QtCore.QRect(170, 100, 60, 20))
        self.w_hash_lab.setObjectName("w_hash_lab")
        self.a_hash = QtWidgets.QLineEdit(self.groupBox)
        self.a_hash.setGeometry(QtCore.QRect(70, 70, 80, 30))
        self.a_hash.setObjectName("a_hash")
        self.w_hash = QtWidgets.QLineEdit(self.groupBox)
        self.w_hash.setGeometry(QtCore.QRect(230, 100, 80, 30))
        self.w_hash.setObjectName("w_hash")
        self.hist_sim = QtWidgets.QLineEdit(self.groupBox)
        self.hist_sim.setGeometry(QtCore.QRect(370, 70, 80, 30))
        self.hist_sim.setObjectName("hist_sim")
        self.p_hash = QtWidgets.QLineEdit(self.groupBox)
        self.p_hash.setGeometry(QtCore.QRect(230, 70, 80, 30))
        self.p_hash.setObjectName("p_hash")
        self.d_hash = QtWidgets.QLineEdit(self.groupBox)
        self.d_hash.setGeometry(QtCore.QRect(70, 100, 80, 30))
        self.d_hash.setObjectName("d_hash")
        self.cover_percent_lab = QtWidgets.QLabel(self.groupBox)
        self.cover_percent_lab.setGeometry(QtCore.QRect(320, 100, 60, 20))
        self.cover_percent_lab.setObjectName("cover_percent_lab")
        self.cover_percent = QtWidgets.QLineEdit(self.groupBox)
        self.cover_percent.setGeometry(QtCore.QRect(370, 100, 80, 30))
        self.cover_percent.setObjectName("cover_percent")
        self.comapre_result = QtWidgets.QGraphicsView(self.centralwidget)
        self.comapre_result.setGeometry(QtCore.QRect(590, 0, 461, 451))
        self.comapre_result.setMouseTracking(True)
        self.comapre_result.setObjectName("comapre_result")
        self.line_tar = QtWidgets.QFrame(self.centralwidget)
        self.line_tar.setGeometry(QtCore.QRect(570, 0, 20, 451))
        self.line_tar.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_tar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_tar.setObjectName("line_tar")
        self.line_src = QtWidgets.QFrame(self.centralwidget)
        self.line_src.setGeometry(QtCore.QRect(280, 0, 21, 300))
        self.line_src.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_src.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_src.setObjectName("line_src")
        self.src_img_lab = QtWidgets.QLabel(self.centralwidget)
        self.src_img_lab.setGeometry(QtCore.QRect(0, 0, 270, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.src_img_lab.setFont(font)
        self.src_img_lab.setMouseTracking(True)
        self.src_img_lab.setAcceptDrops(True)
        self.src_img_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.src_img_lab.setAutoFillBackground(False)
        self.src_img_lab.setScaledContents(True)
        self.src_img_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.src_img_lab.setWordWrap(False)
        self.src_img_lab.setObjectName("src_img_lab")
        self.tar_img_lab = QtWidgets.QLabel(self.centralwidget)
        self.tar_img_lab.setGeometry(QtCore.QRect(290, 0, 270, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.tar_img_lab.setFont(font)
        self.tar_img_lab.setMouseTracking(True)
        self.tar_img_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tar_img_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.tar_img_lab.setObjectName("tar_img_lab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 31))
        self.menubar.setObjectName("menubar")
        self.menuImage_Comparasion = QtWidgets.QMenu(self.menubar)
        self.menuImage_Comparasion.setObjectName("menuImage_Comparasion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuImage_Comparasion.addAction(self.actionOpen)
        self.menuImage_Comparasion.addSeparator()
        self.menuImage_Comparasion.addAction(self.actionExit)
        self.menubar.addAction(self.menuImage_Comparasion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Img Comp"))
        self.groupBox.setTitle(_translate("MainWindow", "Operation"))
        self.Compare_btn.setText(_translate("MainWindow", "Compare"))
        self.a_hash_lab.setText(_translate("MainWindow", "A-Hash:"))
        self.d_hash_lab.setText(_translate("MainWindow", "D-Hash:"))
        self.p_hash_lab.setText(_translate("MainWindow", "P_Hash:"))
        self.hist_lab.setText(_translate("MainWindow", "Hist:"))
        self.w_hash_lab.setText(_translate("MainWindow", "W_Hash:"))
        self.a_hash.setText(_translate("MainWindow", "0.0"))
        self.w_hash.setText(_translate("MainWindow", "0.0"))
        self.hist_sim.setText(_translate("MainWindow", "0.0"))
        self.p_hash.setText(_translate("MainWindow", "0.0"))
        self.d_hash.setText(_translate("MainWindow", "0.0"))
        self.cover_percent_lab.setText(_translate("MainWindow", "Cover:"))
        self.cover_percent.setText(_translate("MainWindow", "0.0"))
        self.src_img_lab.setText(_translate("MainWindow", "Double Click to add a Image"))
        self.tar_img_lab.setText(_translate("MainWindow", "Double Click to add a Image"))
        self.menuImage_Comparasion.setTitle(_translate("MainWindow", "File(F)"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

