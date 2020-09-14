from PyQt5 import QtCore, QtGui, QtWidgets

class PhotoViewer(QtWidgets.QGraphicsView):

    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):

        super(PhotoViewer, self).__init__()
