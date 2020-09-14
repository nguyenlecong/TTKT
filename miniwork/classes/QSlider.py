
''' The QSlider widget provides a vertical or horizontal slider '''

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QLabel
import sys

class Window(QWidget):
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
        self.setStyleSheet('background-color:gray')

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal) # horizontal slider
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(-100)
        self.slider.setMaximum((100))
        self.slider.valueChanged.connect(self.changeValue)

        self.label = QLabel("-100")
        self.label.setFont(QtGui.QFont("Arial", 14))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def changeValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
