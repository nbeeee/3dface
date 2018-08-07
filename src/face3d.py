# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face3d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QProgressDialog
from PyQt5.QtGui import QPixmap,QIcon,QImage
from PyQt5.QtCore import QTimer,Qt,QThread
import cv2
import faceManager as oper
import os
import traceback

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1115, 856)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 711, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.vediolabel = QtWidgets.QLabel(self.frame)
        self.vediolabel.setGeometry(QtCore.QRect(10, 20, 711, 621))
        self.vediolabel.setText("")
        self.vediolabel.setObjectName("vediolabel")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 20, 351, 771))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.framelabel = QtWidgets.QLabel(self.frame_2)
        self.framelabel.setGeometry(QtCore.QRect(1, 1, 349, 359))
        self.framelabel.setText("")
        self.framelabel.setObjectName("framelabel")
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.facelabel = QtWidgets.QLabel(self.frame_3)
        self.facelabel.setGeometry(QtCore.QRect(1, 1, 349, 358))
        self.facelabel.setText("")
        self.facelabel.setObjectName("facelabel")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 660, 711, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openCamBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openCamBtn.setObjectName("openCamBtn")
        self.horizontalLayout.addWidget(self.openCamBtn)
        self.closeWinBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.horizontalLayout.addWidget(self.closeWinBtn)
        self.initFaceBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.initFaceBtn.setObjectName("initFaceBtn")
        self.horizontalLayout.addWidget(self.initFaceBtn)
        self.cutScreenBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cutScreenBtn.setObjectName("cutScreenBtn")
        self.horizontalLayout.addWidget(self.cutScreenBtn)
        self.create3DBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.create3DBtn.setObjectName("create3DBtn")
        self.horizontalLayout.addWidget(self.create3DBtn)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 640, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(720, 0, 20, 831))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.startCamera)
        self.IsOpened = False
        #按钮信号槽
        self.openCamBtn.clicked.connect(self.openCamera)
        self.closeWinBtn.clicked.connect(self.closeWin)
        self.cutScreenBtn.clicked.connect(self.cutScreenAndFaceDet)
        self.initFaceBtn.clicked.connect(self.initWindow)
        self.create3DBtn.clicked.connect(self.create3DFace)

        if os.path.exists('face/face.jpg'):
            face_img = cv2.imread('face/face.jpg')
            fwidth = self.framelabel.width()
            fheight = self.framelabel.height()
            showImage = self.coventFrametoQImage(face_img, fwidth, fheight)
            self.framelabel.setPixmap(QPixmap.fromImage(showImage))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openCamBtn.setText(_translate("MainWindow", "打开摄像头"))
        self.closeWinBtn.setText(_translate("MainWindow", "关闭"))
        self.initFaceBtn.setText(_translate("MainWindow", "初始化"))
        self.cutScreenBtn.setText(_translate("MainWindow", "截图"))
        self.create3DBtn.setText(_translate("MainWindow", "生成3D图"))

    #打开摄像头
    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.IsOpened = self.cap.isOpened()
        self.timer.start(10)

    #根据timer定时器播放画面
    def startCamera(self):
        self.timer.stop()
        ret,frame = self.cap.read()
        if ret:
            try:
                wframe = self.vediolabel.width()
                hframe = self.vediolabel.height()
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
                showImage = QImage(frame.data, width, height,bytesPerLine,QImage.Format_RGB888)
                showImage = showImage.scaled(wframe,hframe)
                self.vediolabel.setPixmap(QPixmap.fromImage(showImage))
            except Exception as e:
                print('play vedio frame error[' + str(e) + ']')
        self.timer.start(1)

    #截屏识别人脸
    def cutScreenAndFaceDet(self):
        if self.IsOpened:
            ret,frame = self.cap.read()
            if ret:
                try:
                    oper.faceDetector(frame)
                except Exception as e:
                    print('face detector error[' + str(e) + ']')
                wframe = self.framelabel.width()
                hframe = self.framelabel.height()
                showImage = self.coventFrametoQImage(frame,wframe,hframe)
                self.framelabel.setPixmap(QPixmap.fromImage(showImage))

    #生成3d人脸图像
    def create3DFace(self):
        if not os.path.exists(oper.facepath):
            QMessageBox.warning(self,'提示','请先截取人脸照片',QMessageBox.Yes,QMessageBox.No)
        else:
            try:
                self.facelabel.setText('正在生成。。。。。。')
                #self.progressDialog = QProgressDialog(self)
                #self.showProgressbar()
                image = oper.gener3DFace()
                fwidth = self.facelabel.width()
                fheight = self.facelabel.height()
                showImage = self.coventFrametoQImage(image, fwidth, fheight)
                self.facelabel.setPixmap(QPixmap.fromImage(showImage))
                #self.progressDialog.close()
            except Exception as e:
                print('traceback.format_exc():\n%s' % traceback.format_exc())

    def showProgressbar(self):
        self.step = 0
        self.ptimer = QTimer(self)
        self.ptimer.timeout.connect(self.addprocess)
        self.ptimer.start()
        self.progressDialog.setWindowModality(Qt.WindowModal)
        self.progressDialog.setMinimumDuration(5)
        self.progressDialog.setWindowTitle(self.tr("进度"))
        self.progressDialog.setLabelText(self.tr("正在生成"))
        # progressDialog.setCancelButtonText(self.tr("取消"))
        self.progressDialog.setCancelButton(None)
        self.progressDialog.setFixedWidth(300)
        self.progressDialog.setFixedHeight(50)
        self.progressDialog.setRange(0, 100)

    def addprocess(self):
        print("addprocessor  step 1......")
        self.ptimer.stop()
        if self.step <= 99:
            self.step += 1
            self.progressDialog.setValue(self.step)
            self.ptimer.start(10)
    #初始化
    def initWindow(self):
        self.framelabel.clear()
        self.facelabel.clear()
        if os.path.exists(oper.facepath):
            os.remove(oper.facepath)

    #关闭窗口，释放摄像头
    def closeWin(self):
        if self.IsOpened:
            self.cap.release()
        self.close()


    def coventFrametoQImage(self,frame,w,h):
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        showImage = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        showImage = showImage.scaled(w, h)
        return showImage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())