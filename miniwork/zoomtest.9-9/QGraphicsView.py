
# ===== GraphicsView Framework =====
# * Provides:
#   - a surface for managing interactive 2D graphical items
#   - a view widget for visualizing the items
# * Uses MVC paradigm
# * Resolution Imdependent
# * Animation Support
# * Fast item discovery, hit tests, collision detection
#   - Using Binary Space Paritioning (BSP) tree indexes
# * Can manage large numbers of items (tens of thousands)
# * Support zooming, printing and rendering

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QPushButton
import sys

class Window(QMainWindow):
    
    def __init__(self):

        super().__init__()

        self.title = "PyQt5 QGraphic View"
        self.left = 500
        self.top = 200
        self.width = 600
        self.height = 500
        self.iconname = "imgs/2.jpg"

        self.InitUI()

    def InitUI(self):

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconname))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGraphicView()

        self.show()

    def createGraphicView(self):

        self.scene = QGraphicsScene()

        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)

        self.pen = QPen(Qt.red)
        self.pen.setWidth(5)

        self.graphicView = QGraphicsView(self.scene, self)
        self.graphicView.setGeometry(0,0,600,400)

        self.button1 = QPushButton("Rotate -", self)
        self.button1.setGeometry(175,425,100,50)
        self.button1.clicked.connect(self.rotateMinus)

        self.button2 = QPushButton("Rotate +", self)
        self.button2.setGeometry(325, 425, 100, 50)
        self.button2.clicked.connect(self.rotatePlus)

        self.shapes()

    def rotateMinus(self):
        self.graphicView.rotate(-10)

    def rotatePlus(self):
        self.graphicView.rotate(10)

    def shapes(self):
        ellipse = self.scene.addEllipse(20,20,200,200, self.pen, self.greenBrush)
        rect = self.scene.addRect(-100, -100, 200, 200, self.pen, self.grayBrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)
        rect.setFlag(QGraphicsItem.ItemIsSelectable)
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())