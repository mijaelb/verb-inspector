import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot

from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
import qt.QtUtils as QtUtils

VERB_LIST_WIDTH = 225


class EditPlotPointWidget(QtWidgets.QWidget):
    def __init__(self, pp, parent=None):
        super().__init__(parent)
        self.plotpoints = pp
        self.currentPlotPoint = None
        self.currentPlotPoints = None
        self.currentSense = None

        self.plotpointsLabel = QtWidgets.QLabel('PlotPoints ▾')

        self.plotPointsList = QtWidgets.QListWidget()
        self.plotPointsList.currentItemChanged.connect(self.updatePlotPoint)
        self.updatePlotPointsList()

        self.editArgsWidget = ArgDragWidget(None, self)
        self.editArgsLayout = QtWidgets.QHBoxLayout()
        self.editArgsLayout.addWidget(self.editArgsWidget)
        # self.editArgsWidget.selected.connect(self.selectArg)

        self.senseList = QtWidgets.QListWidget()
        self.senseList.currentItemChanged.connect(self.updateSense)
        self.editSenseLayout = QtWidgets.QHBoxLayout()
        self.editSenseLayout.addWidget(self.senseList)

        self.plotpointsEditLayout = QtWidgets.QVBoxLayout()
        self.plotpointsEditLayout.addLayout(self.editArgsLayout)
        self.plotpointsEditLayout.addLayout(self.editSenseLayout)

        self.plotpointsListLayout = QtWidgets.QVBoxLayout()
        self.plotpointsListLayout.addWidget(self.plotpointsLabel)
        self.plotpointsListLayout.addWidget(self.plotPointsList)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.plotpointsListLayout)
        self.layout.addLayout(self.plotpointsEditLayout)

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.plotPointsList.setStyleSheet('QLabel { color: palette(midlight); }')
        self.plotPointsList.setMaximumWidth(self.plotPointsList.sizeHint().width())
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    def updatePlotPointArgs(self, selected=None):
        if self.currentSense:
            self.editArgsWidget.resetWidget(self.currentSense.args, selected)
        else:
            self.editArgsWidget.clearWidget()

    def updatePlotPointsList(self):
        self.plotPointsList.clear()
        plotpoints = self.plotpoints.get_plotpoints() if not self.currentPlotPoints else self.currentPlotPoints
        for pp in plotpoints.values():
            ppItem = QtWidgets.QListWidgetItem(pp.lemma)
            ppItem.setData(QtCore.Qt.UserRole, pp)
            ppItem.setFlags(ppItem.flags() | QtCore.Qt.ItemIsEditable)
            self.plotPointsList.addItem(ppItem)

    def updateSenseList(self):
        if self.currentPlotPoint:
            self.senseList.clear()
            for sense in self.currentPlotPoint.senses:
                senseItem = QtWidgets.QListWidgetItem(sense.id + ": " + str(sense.dataset) + ": " + str(sense.descr))
                senseItem.setData(QtCore.Qt.UserRole, sense)
                # senseItem.setFlags(senseItem.flags() | QtCore.Qt.ItemIsEditable)
                self.senseList.addItem(senseItem)

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updatePlotPoint(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentPlotPoint = current.data(QtCore.Qt.UserRole)
            self.currentSense = None

            self.updateSenseList()
        else:
            self.currentPlotPoint = None

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updateSense(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentSense = current.data(QtCore.Qt.UserRole)
            self.updatePlotPointArgs()
        else:
            self.currentSense = None
