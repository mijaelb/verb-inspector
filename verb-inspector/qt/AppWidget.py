import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import qt.QtUtils as QtUtils
from qt.EditClassWidget import EditClassWidget
from qt.EditPlotPointWidget import EditPlotPointWidget
import qt.QtUtils as QtUtils


class AppWidget(QtWidgets.QWidget):
    def __init__(self, pp_container, parent=None):
        super().__init__(parent)
        self.pp_container = pp_container

        self.editClassWidget = EditClassWidget(self.pp_container)
        self.editPlotPointWidget = EditPlotPointWidget(self.pp_container)
        self.editClassWidget.setPlotPointWidget(self.editPlotPointWidget)
        self.editPlotPointWidget.setClassWidget(self.editClassWidget)

        self.hLine = QtUtils.QHLine()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.editPlotPointWidget)
        self.layout.addWidget(self.hLine)
        self.layout.addWidget(self.editClassWidget)

        self.initUI()

    def initUI(self):
        self.setLayout(self.layout)
        self.editClassWidget.setMaximumHeight(600)
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')

        self.editClassWidget.setStyleSheet(self.styleSheet())
        self.editClassWidget.setPalette(self.palette())
