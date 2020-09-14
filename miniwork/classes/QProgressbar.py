from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtGui
import time
import sys

class Window(QDialog):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Slider"
        self.left = 500
        self.top = 200
        self.width = 600
        self.height = 500
        self.iconname = "imgs/2.jpg"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconname))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.InitUI()

        self.show()
    
    def InitUI(self):

        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}; QProgressBar::chunk {backgroud:green")
        # self.progressbar.setTextVisible(False)
        # self.progressbar.setOrientation(Qt.Vertical)

        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        self.button.setStyleSheet("background-color:red")
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def startProgressBar(self):

        self.thread = Thread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()


    def setProgressVal(self, val):

        self.progressbar.setValue(val)

class Thread(QThread):
    change_value =pyqtSignal(int)

    def run(self):

        cnt = 0

        while cnt < 100:

            cnt += 1

            time.sleep(0.01)
            self.change_value.emit(cnt)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
