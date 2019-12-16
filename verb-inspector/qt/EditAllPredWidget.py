import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import qt.QtUtils as QtUtils
from PyQt5.QtCore import pyqtSlot

class EditAllPredWidget(QtWidgets.QWidget):
    def __init__(self, vn, parent=None):
        super().__init__(parent)
        self.setObjectName('EditAllPredWidget')