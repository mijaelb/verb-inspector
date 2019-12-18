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
        self.currentClass = None

        self.plotpointsLabel = QtWidgets.QLabel('PlotPoints ▾')

        self.plotPointsList = QtWidgets.QListWidget()
        self.plotPointsList.currentItemChanged.connect(self.updatePlotPoint)
        self.updatePlotPointsList()

        self.editArgsWidget = ArgDragWidget(None, self)
        self.editArgsLayout = QtWidgets.QHBoxLayout()
        self.editArgsLayout.addWidget(self.editArgsWidget)
        # self.editArgsWidget.selected.connect(self.selectArg)

        self.classesList = QtWidgets.QListWidget()

        self.editClassButton = QtWidgets.QPushButton('Edit Class')
        self.selectSenseButton = QtWidgets.QPushButton('Select Sense')
        self.selectSenseButton.released.connect(self.selectSense)

        self.classesListLayout = QtWidgets.QVBoxLayout()
        self.classesListLayout.addWidget(self.classesList)
        self.classesListLayout.addWidget(self.editClassButton)

        self.senseList = QtWidgets.QListWidget()
        self.senseList.currentItemChanged.connect(self.updateSense)

        self.senseListLayout = QtWidgets.QVBoxLayout()
        self.senseListLayout.addWidget(self.senseList)
        self.senseListLayout.addWidget(self.selectSenseButton)

        self.editSenseLayout = QtWidgets.QHBoxLayout()
        self.editSenseLayout.addLayout(self.senseListLayout)
        self.editSenseLayout.addLayout(self.classesListLayout)

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
                senseItem = QtWidgets.QListWidgetItem(str(sense))
                senseItem.setData(QtCore.Qt.UserRole, sense)
                # senseItem.setFlags(senseItem.flags() | QtCore.Qt.ItemIsEditable)
                self.senseList.addItem(senseItem)

    def updateClassesList(self):
        if self.currentSense:
            self.classesList.clear()
            for cls_id in self.currentSense.mappings.vn:
                classItem = QtWidgets.QListWidgetItem(cls_id)
                classItem.setData(QtCore.Qt.UserRole, classItem)
                self.classesList.addItem(classItem)

    def clearPlotPoint(self):
        self.currentSense = None
        self.currentClass = None
        self.senseList.clear()
        self.classesList.clear()
        self.editArgsWidget.clearWidget()

    def setSelectedSense(self, sense):
        if sense:
            for i in range(self.senseList.count()):
                if self.senseList.item(i).text() == str(sense):
                    self.senseList.setCurrentItem(self.senseList.item(i))
                    break

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updatePlotPoint(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentPlotPoint = current.data(QtCore.Qt.UserRole)
            self.clearPlotPoint()
            self.updateSenseList()
            self.setSelectedSense(self.currentPlotPoint.selected)
        else:
            self.clearPlotPoint()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updateSense(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentSense = current.data(QtCore.Qt.UserRole)
            self.updatePlotPointArgs()
            self.updateClassesList()
        else:
            self.clearPlotPoint()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updateClass(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentClass = current.data(QtCore.Qt.UserRole)
        else:
            self.currentClass = None

    @pyqtSlot()
    def selectSense(self):
        if self.currentSense:
            self.currentPlotPoint.selected = self.currentSense
