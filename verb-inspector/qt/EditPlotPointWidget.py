import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot
from utils import utils
from qt.EditArgWidget import EditArgWidget
from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
import qt.QtUtils as QtUtils

VERB_LIST_WIDTH = 225


class EditPlotPointWidget(QtWidgets.QWidget):
    def __init__(self, pp_container, parent=None):
        super().__init__(parent)
        self.pp_container = pp_container

        self.editClassWidget = None
        self.currentPlotPoint = None
        self.currentPlotPoints = None
        self.currentSense = None
        self.currentClass = None

        self.plotpointNameLabel = QtWidgets.QLabel()
        self.selectedSenseLabel = QtWidgets.QLabel()

        self.plotpointsLabel = QtWidgets.QLabel('PlotPoints ▾')

        self.plotPointsList = QtWidgets.QListWidget()
        self.plotPointsList.currentItemChanged.connect(self.updatePlotPoint)
        self.updatePlotPointsList()

        self.plotPointCleanedCheckBox = QtWidgets.QCheckBox('Cleaned')
        self.plotPointCleanedCheckBox.stateChanged.connect(self.plotPointCleaned)

        self.plotPointUnFilterButton = QtWidgets.QPushButton('Unfilter')
        self.plotPointUnFilterButton.released.connect(self.unfilter)
        self.plotPointFilterByClassButton = QtWidgets.QPushButton('Filter By Class')
        self.plotPointFilterByClassButton.released.connect(self.filterByClass)

        self.editArgWidget = EditArgWidget('pp', self.pp_container, self)

        self.editArgsLayout = QtWidgets.QHBoxLayout()
        self.editArgsLayout.addWidget(self.editArgWidget)

        self.classesList = QtWidgets.QListWidget()
        self.classesList.currentItemChanged.connect(self.updateClass)


        self.editClassButton = QtWidgets.QPushButton('Edit Class')
        self.addClassButton = QtWidgets.QPushButton('Add Class')
        self.removeClassButton = QtWidgets.QPushButton('Remove Class')
        self.selectSenseButton = QtWidgets.QPushButton('Select Sense')
        self.editClassButton.released.connect(self.editClass)
        self.addClassButton.released.connect(self.addClass)
        self.removeClassButton.released.connect(self.removeClass)
        self.selectSenseButton.released.connect(self.selectSense)

        self.classesButtonsLayout = QtWidgets.QHBoxLayout()
        self.classesButtonsLayout.addWidget(self.editClassButton)
        self.classesButtonsLayout.addWidget(self.addClassButton)
        self.classesButtonsLayout.addWidget(self.removeClassButton)

        self.classesListLayout = QtWidgets.QVBoxLayout()
        self.classesListLayout.addWidget(self.classesList)
        self.classesListLayout.addLayout(self.classesButtonsLayout)

        self.senseList = QtWidgets.QListWidget()
        self.senseList.currentItemChanged.connect(self.updateSense)

        self.senseListLayout = QtWidgets.QVBoxLayout()
        self.senseListLayout.addWidget(self.senseList)
        self.senseListLayout.addWidget(self.selectSenseButton)

        self.compiledPredicateList = QtWidgets.QListWidget()
        self.compilePredicatesButton = QtWidgets.QPushButton('Compile Predicates')
        self.compilePredicatesButton.released.connect(self.compilePredicates)
        self.updateCompiledPredicateList()

        self.compiledPredicateLayout = QtWidgets.QVBoxLayout()
        self.compiledPredicateLayout.addWidget(self.compiledPredicateList)
        self.compiledPredicateLayout.addWidget(self.compilePredicatesButton)

        self.editSenseLayout = QtWidgets.QHBoxLayout()
        self.editSenseLayout.addLayout(self.senseListLayout)
        self.editSenseLayout.addLayout(self.classesListLayout)
        self.editSenseLayout.addLayout(self.compiledPredicateLayout)

        self.plotpointsEditLayout = QtWidgets.QVBoxLayout()
        self.plotpointsEditLayout.addWidget(self.plotpointNameLabel)
        self.plotpointsEditLayout.addWidget(self.selectedSenseLabel)
        self.plotpointsEditLayout.addLayout(self.editArgsLayout)
        self.plotpointsEditLayout.addLayout(self.editSenseLayout)

        self.plotpointsListLayout = QtWidgets.QVBoxLayout()
        self.plotpointsListLayout.addWidget(self.plotpointsLabel)
        self.plotpointsListLayout.addWidget(self.plotPointsList)
        self.plotpointsListLayout.addWidget(self.plotPointCleanedCheckBox)
        self.plotpointsListLayout.addWidget(self.plotPointFilterByClassButton)
        self.plotpointsListLayout.addWidget(self.plotPointUnFilterButton)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.plotpointsListLayout)
        self.layout.addLayout(self.plotpointsEditLayout)

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        font = QtGui.QFont('Helvetica', 10)
        font.setBold(True)
        self.plotpointNameLabel.setFont(font)
        self.selectedSenseLabel.setFont(font)
        self.plotPointsList.setStyleSheet('QLabel { color: palette(midlight); }')
        self.plotPointsList.setMaximumWidth(self.plotPointsList.sizeHint().width())
        self.layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    def refreshClasses(self):
        if self.currentPlotPoint and self.currentSense:
            self.updateClassesList()
            self.editArgWidget.update(self.currentSense)

    def updatePlotPointsList(self):
        self.plotPointsList.clear()
        plotpoints = self.pp_container.get_plotpoints() if not self.currentPlotPoints else self.currentPlotPoints
        for pp in plotpoints.values():
            ppItem = QtWidgets.QListWidgetItem(pp.lemma)
            ppItem.setData(QtCore.Qt.UserRole, pp)
            ppItem.setFlags(ppItem.flags() | QtCore.Qt.ItemIsEditable)
            if pp.cleaned:
                ppItem.setBackground(QtGui.QColor.green())
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
                classItem.setData(QtCore.Qt.UserRole, cls_id)
                self.classesList.addItem(classItem)

    def updateCompiledPredicateList(self):
        if self.currentSense:
            self.compiledPredicateList.clear()
            for pred in self.currentSense.get_compiled_predicates(self.pp_container.verbnet):
                predItem = QtWidgets.QListWidgetItem(str(pred))
                predItem.setData(QtCore.Qt.UserRole, pred)
                self.compiledPredicateList.addItem(predItem)

    def clear(self):
        self.currentSense = None
        self.currentClass = None
        self.plotpointNameLabel.setText('')
        self.senseList.clear()
        self.classesList.clear()
        self.compiledPredicateList.clear()
        self.editArgWidget.clear()

    def setSelectedSense(self, sense):
        if sense:
            str_ = str(sense)
            self.selectedSenseLabel.setText(f'Selected Sense: {str_[0:50 if len(str_) > 50 else len(str_)]}...')
            for i in range(self.senseList.count()):
                if self.senseList.item(i).text() == str(sense):
                    self.senseList.setCurrentItem(self.senseList.item(i))
                    break

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updatePlotPoint(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentPlotPoint = current.data(QtCore.Qt.UserRole)
            self.plotPointCleanedCheckBox.setChecked(self.currentPlotPoint.cleaned)
            self.clear()
            self.plotpointNameLabel.setText(f'Current Plot Point: {self.currentPlotPoint.lemma}')
            self.updateSenseList()
            self.setSelectedSense(self.currentPlotPoint.selected)
        else:
            self.clear()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updateSense(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentSense = current.data(QtCore.Qt.UserRole)
            self.editArgWidget.clear()
            self.editArgWidget.update(self.currentSense)
            self.updateClassesList()
            self.updateCompiledPredicateList()
        else:
            self.clear()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def updateClass(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        self.currentClass = current.data(QtCore.Qt.UserRole) if current else None

    @pyqtSlot()
    def selectSense(self):
        if self.currentSense:
            self.currentPlotPoint.selected = self.currentSense
            self.setSelectedSense(self.currentPlotPoint.selected)

    @pyqtSlot()
    def compilePredicates(self):
        self.updateCompiledPredicateList()

    @pyqtSlot()
    def plotPointCleaned(self):
        if self.currentPlotPoint:
            self.currentPlotPoint.cleaned = self.plotPointCleanedCheckBox.isChecked()

    @pyqtSlot()
    def editClass(self):
        if self.currentClass and self.editClassWidget:
            self.editClassWidget.selectClass(self.currentClass)

    @pyqtSlot()
    def addClass(self):
        if self.editClassWidget:
            self.currentSense.add_class(self.editClassWidget.getClass())
            self.editArgWidget.update(self.currentSense)
            self.updateClassesList()
            self.updateCompiledPredicateList()

    @pyqtSlot()
    def removeClass(self):
        if self.currentClass and self.editClassWidget:
            self.currentSense.remove_class(self.pp_container.verbnet.get_class(self.currentClass))
            self.editArgWidget.update(self.currentSense)
            self.updateClassesList()
            self.updateCompiledPredicateList()

    @pyqtSlot()
    def filterByClass(self):
        cls = self.editClassWidget.getClass()
        if cls:
            self.currentPlotPoints = self.pp_container.get_plotpoints(cls.id)
            self.updatePlotPointsList()

    @pyqtSlot()
    def unfilter(self):
        self.currentPlotPoints = None
        self.updatePlotPointsList()

    def setClassWidget(self, classWidget):
        self.editClassWidget = classWidget
