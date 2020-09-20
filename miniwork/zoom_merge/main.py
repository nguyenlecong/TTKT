from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor, QImage, QPainter, QPixmap
from photo_viewer import PhotoViewer
import numpy as np
import cv2

class Ui_MainWindow(QtWidgets.QGraphicsView):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(60, 550, 121, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.open_image_file)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 550, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.gray_scale)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.photo_viewer_ = PhotoViewer(self)
        scence = QtWidgets.QGraphicsScene()
        scence.addWidget(self.photo_viewer_)
        layout = QtWidgets.QGraphicsView(scence, self.centralwidget)
        layout.setGeometry(QtCore.QRect(0, 0, 961, 520))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zoom"))
        self.pushButton_1.setText(_translate("MainWindow", "Select Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Gray Scale"))

    def open_image_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'imgs/', "Image files (*.jpg *.png)")
        
        # load image and display into photo_viewer class
        self.input_path = fname[0]
        pixmap = QPixmap(self.input_path)

        self.photo_viewer_.setPhoto(pixmap)

    def gray_scale(self, photo_viewer_, input_path = None):
        image = cv2.imread(self.input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            
        height, width, channel = image.shape
        bytesPerLine = width * channel
        pixmap = QPixmap(QPixmap.fromImage(QImage(image.data, width, height,\
                                                    bytesPerLine, QImage.Format_RGB888)))

        self.photo_viewer_.setPhoto(pixmap)
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''
    -thay qgraphic view bang photoviewer
    -khi chon anh ban dau cho hien o photoviewer
    -ham xu ly anh o main windows
    -sau khi xu ly xong thi set lai anh o photoviewer
'''
