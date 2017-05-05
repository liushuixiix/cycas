# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.setWindowTitle("图标")
        self.setWindowIcon(QtGui.QIcon(r'ooopic_1459042536.ico'))
        with open('cycas.qss', 'r') as q:#挂载样式表
            self.setStyleSheet(q.read())#挂载样式表
        self.pushButton_1 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_1.setGeometry(QtCore.QRect(310, 440, 81, 51))
        self.pushButton_1.setObjectName("pushButton_1")     
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 440, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 440, 81, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 510, 81, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 510, 81, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 510, 81, 51))
        self.pushButton_6.setObjectName("pushButton_6")

        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(130, 380, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 430, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 480, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.timeEdit = QtWidgets.QTimeEdit(MainWindow)
        self.timeEdit.setGeometry(QtCore.QRect(30, 590, 221, 51))
        self.timeEdit.setObjectName("timeEdit")

        self.dateEdit = QtWidgets.QDateEdit(MainWindow)
        self.dateEdit.setGeometry(QtCore.QRect(29, 541, 221, 41))
        self.dateEdit.setObjectName("dateEdit")

        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(40, 380, 61, 31))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 430, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 480, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)#显示图片
        self.label_4.setGeometry(QtCore.QRect(30, 30, 241, 221))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        pic = QtGui.QPixmap(r'npuc.png').scaled(self.label_4.width(), self.label_4.height())
        self.label_4.setPixmap(pic)#显示图片
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(730, 30, 231, 601,))
        self.label_5.setObjectName("label_5")
        #self.label_5.adjustSize()
        self.label_5.setAlignment(Qt.AlignLeft | Qt.AlignTop)#对齐命令
        #self.label_5.setMargin(50)#设置外边距
        #self.label_5.setWordWrap(True)#换行命令
        #self.label_5.resize(50, 50)#换行命令
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(310, 30, 381, 381))
        self.label.setText("")

        pic = QtGui.QPixmap(r'npuc.png').scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pic)
        self.label.setObjectName("label")

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.video = QtWidgets.QAction(MainWindow)
        self.video.setObjectName("video")
        self.picture = QtWidgets.QAction(MainWindow)
        self.picture.setObjectName("picture")
        self.menu.addAction(self.video)
        self.menu.addAction(self.picture)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_1.clicked.connect(self.paly)
        # self.pushButton_2.clicked.connect(self.openimage2)
        # self.pushButton_3.clicked.connect(self.list)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "监控识别"))
        self.pushButton_1.setText(_translate("MainWindow", "停止"))
        self.pushButton_2.setText(_translate("MainWindow", "播放"))
        self.pushButton_3.setText(_translate("MainWindow", "暂停"))
        self.pushButton_4.setText(_translate("MainWindow", "获取系统时间"))
        self.pushButton_5.setText(_translate("MainWindow", "截取图片"))
        self.pushButton_6.setText(_translate("MainWindow", "截取帧数时间"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "工具"))
        self.video.setText(_translate("MainWindow", "打开视频"))
        self.picture.setText(_translate("MainWindow", "打开图片"))
        self.label_1.setText(_translate("MainWindow", "播放速度"))
        self.label_2.setText(_translate("MainWindow", "精确度"))
        self.label_3.setText(_translate("MainWindow", "抽帧数"))

