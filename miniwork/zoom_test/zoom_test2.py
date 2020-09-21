from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class myWindow(QWidget):                                                       # QMainWindow is not available because QLabel inherits from QWidget
    def __init__(self):
        super(myWindow, self).__init__()
        self.imgPixmap = QPixmap('imgs/1.jpg')                              # Load Images
        self.scaledImg = self.imgPixmap.scaled(self.size())                    # Initialize zoom
        self.singleOffset = QPoint(0, 0)                                       # Initialize offset value
        self.isLeftPressed = bool(False)                                       # Picture is clicked (left mouse button) flag bit
        self.isImgLabelArea = bool(True)                                       # Mouse into the label picture display area
               
    '''Heavy haul drawing: Dynamic drawing'''
    def paintEvent(self,event):
        super(myWindow, self).paintEvent(event)
        self.imgPainter = QPainter()                                           # Use to draw pictures dynamically
        self.imgFramePainter = QPainter()                                      # Use to draw picture outline dynamically
        self.imgPainter.begin(self)                                            # If there is no begin and end, the update cycle will continue
        self.imgPainter.drawPixmap(self.singleOffset, self.scaledImg)          # Extract Pixmap from image file and display it in the specified location
        self.imgFramePainter.setPen(QColor(168, 34, 3))  # Default black if not set   # Set drawing color / size / style
        self.imgFramePainter.drawRect(10, 10, 480, 480)                        # Draw lines for pictures (extend 1 outwards)
        self.imgPainter.end()                                                  # If there is no begin and end, the update cycle will continue

    '''Reload mouse down event(Single click)'''
    def mousePressEvent(self, event):
        super(myWindow, self).mousePressEvent(event)
        if event.buttons() == QtCore.Qt.LeftButton:                            # Left key press
            # print("Left click")
            self.isLeftPressed = True;                                         # Press the left key (the picture is clicked), and set the tree
            self.preMousePosition = event.pos()                                # Get the current mouse position

    '''Reload the scroll event'''
    def wheelEvent(self, event):
        # This function has been deprecated, use pixelDelta() or angleDelta() instead.
        angle=event.angleDelta() / 8                                           # Returns the QPoint object, which is the value of the wheel rotation, in 1 / 8 degree
        angleX=angle.x()                                                       # Distance rolled horizontally (not used here)
        angleY=angle.y()                                                       # Vertical rolling distance
        if angleY > 0:                                                         # Roller rolling
            self.scaledImg = self.imgPixmap.scaled(self.scaledImg.width()+50,
                                                   self.scaledImg.height()+50)
            newWidth = event.x() - (self.scaledImg.width() * (event.x()-self.singleOffset.x())) / (self.scaledImg.width()-50)
            newHeight = event.y() - (self.scaledImg.height() * (event.y()-self.singleOffset.y())) / (self.scaledImg.height()-50)
            self.singleOffset = QPoint(newWidth, newHeight)                    # Update offset
            self.repaint()                                                     # Repaint
        else:                                                                 
            self.scaledImg = self.imgPixmap.scaled(self.scaledImg.width()-50,
                                                   self.scaledImg.height()-50)
            newWidth = event.x() - (self.scaledImg.width() * (event.x()-self.singleOffset.x())) / (self.scaledImg.width()+50)
            newHeight = event.y() - (self.scaledImg.height() * (event.y()-self.singleOffset.y())) / (self.scaledImg.height()+50)
            self.singleOffset = QPoint(newWidth, newHeight)                    # Update offset
            self.repaint()                                                     # Repaint

    '''Reload mouse move event'''
    def mouseMoveEvent(self,event):
        if self.isLeftPressed:                                                 # Left key press
            self.endMousePosition = event.pos() - self.preMousePosition        # Mouse current position - previous position = single offset
            self.singleOffset = self.singleOffset + self.endMousePosition      # Update offset
            self.preMousePosition = event.pos()                                # Update the position of the current mouse on the window. Use
            self.repaint()                                                     # Repaint
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.show()
    sys.exit (app.exec_())