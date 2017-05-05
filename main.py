import cv2
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
import sys
import findCat
from nda2qim import toQImage
from ui import Ui_MainWindow  # 导入生成ui.py里生成的类


class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def paly(self):
        global qim
        video = findCat.videoGen('testvideo\\01.mp4', 25)
        img, curtime = video.send(None)
        while img is not None:
            qim = QtGui.QPixmap.fromImage(toQImage(img)).scaled(self.label.width(), self.label.height())
            self.label.setPixmap(qim)
            img, curtime = video.send(cv2.waitKey(1))
            print(curtime)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
