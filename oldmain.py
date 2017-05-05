from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
import sys
from ui import Ui_MainWindow   # 导入生成ui.py里生成的类
class mywindow(QtWidgets.QWidget,Ui_MainWindow):
	def __init__(self):
		super(mywindow,self).__init__()
		self.setupUi(self)
        #定义槽函数
	def openimage1(self):
		global imgName1_2
   # 打开文件路径
   #设置文件扩展名过滤,注意用双分号间隔
		imgName1_2,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

		print(imgName1_2)
        #利用qlabel显示图片
		png = QtGui.QPixmap(imgName1_2).scaled(self.label.width(), self.label.height())
		self.label.setPixmap(png)#将图片显示到Qlabel控件上
	def openimage2(self):
		global imgName
   # 打开文件路径
   #设置文件扩展名过滤,注意用双分号间隔
		imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

		print(imgName)
        #利用qlabel显示图片
		png = QtGui.QPixmap(imgName).scaled(self.label_4.width(), self.label_4.height())
		self.label_4.setPixmap(png)#将图片显示到Qlabel控件上
	def list(self):
		self.label_5.setText("2014.1.20.10:31:36\n\n2014.1.20.10:32:40\n\n2014.1.20.13:35:11\n\n2014.1.20.15:02:43")
if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = mywindow()
	window.show()
	sys.exit(app.exec_())
