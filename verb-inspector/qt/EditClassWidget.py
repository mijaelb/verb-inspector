import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot
import os
from utils import utils
from qt.EditArgWidget import EditArgWidget
from qt.EditPredWidget import EditPredWidget
import qt.QtUtils as QtUtils

CLASS_LIST_WIDTH = 225
_FL_STYLESHEET = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/frameless.qss')


class EditClassWidget(QtWidgets.QWidget):
    def __init__(self, vn, parent=None):
        super().__init__(parent)
        self.verbnet = vn
        self.filename = self.verbnet.json_path
        self.currentClass = None
        self.currentPred = None
        self.currentClasses = None

        self.plotPointWidget = None
        self.editArgWidget = EditArgWidget()
        self.classesLabel = QtWidgets.QLabel('Classes ▾')

        self.hLine = QtUtils.QHLine()
        self.saveButton = QtWidgets.QPushButton('Save')
        self.saveAsButton = QtWidgets.QPushButton('Save As')
        self.openButton = QtWidgets.QPushButton('Open')
        self.saveButton.released.connect(self.save)
        self.saveAsButton.released.connect(self.saveAs)
        self.openButton.released.connect(self.open)

        self.classButtons = QtWidgets.QHBoxLayout()
        self.classButtons.addWidget(self.saveButton)
        self.classButtons.addWidget(self.saveAsButton)
        self.classButtons.addWidget(self.openButton)

        self.filterByPredicateButton = QtWidgets.QPushButton('Filter by predicate')
        self.removeFilterButton = QtWidgets.QPushButton('Unfilter')
        self.filterByPredicateButton.released.connect(self.filterByPredicate)
        self.removeFilterButton.released.connect(self.removeFilter)

        self.filterButtons = QtWidgets.QHBoxLayout()
        self.filterButtons.addWidget(self.filterByPredicateButton)
        self.filterButtons.addWidget(self.removeFilterButton)

        self.predsListLabel = QtWidgets.QLabel('All predicates ▾')

        self.predsList = QtWidgets.QListWidget()
        self.predsList.currentItemChanged.connect(self.changePred)
        self.predsList.itemChanged.connect(self.updatePred)
        self.updatePredsList()

        self.classesList = QtWidgets.QListWidget()
        self.classesList.currentItemChanged.connect(self.changeClass)
        self.classesList.itemChanged.connect(self.updateClass)
        self.updateClassesList()

        self.classSelectLayout = QtWidgets.QVBoxLayout()
        self.classSelectLayout.addWidget(self.classesLabel)
        self.classSelectLayout.addWidget(self.classesList)
        self.classSelectLayout.addWidget(self.predsListLabel)
        self.classSelectLayout.addWidget(self.predsList)
        self.classSelectLayout.addLayout(self.filterButtons)
        self.classSelectLayout.addLayout(self.classButtons)

        self.editPredWidget = EditPredWidget()

        self.editClassLayout = QtWidgets.QVBoxLayout()
        self.editClassLayout.addWidget(self.editArgWidget)
        self.editClassLayout.addWidget(self.hLine)
        self.editClassLayout.addWidget(self.editPredWidget)
        self.editClassLayout.addStretch(1)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.classSelectLayout)
        self.layout.addLayout(self.editClassLayout)

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.predsListLabel.setStyleSheet('QLabel { color: palette(midlight); }')
        self.classesList.setMaximumWidth(self.classesList.sizeHint().width())
        self.predsList.setMaximumWidth(self.predsList.sizeHint().width())
        self.predsList.setMaximumHeight(150)
        self.classSelectLayout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setAlignment(self.classSelectLayout, QtCore.Qt.AlignTop)

    def updateClassesList(self):
        self.classesList.clear()
        classes = self.verbnet.get_classes() if not self.currentClasses else self.currentClasses
        for cls in classes.values():
            classItem = QtWidgets.QListWidgetItem(cls.id)
            classItem.setData(QtCore.Qt.UserRole, cls)
            classItem.setFlags(classItem.flags() | QtCore.Qt.ItemIsEditable)
            self.classesList.addItem(classItem)

    def updatePredsList(self):
        self.predsList.clear()
        for pred in self.verbnet.get_all_predicates_name():
            predItem = QtWidgets.QListWidgetItem(pred)
            predItem.setData(QtCore.Qt.UserRole, pred)
            predItem.setFlags(predItem.flags() | QtCore.Qt.ItemIsEditable)
            self.predsList.addItem(predItem)

    def getClass(self):
        return self.currentClass

    def resetClass(self):
        self.editArgWidget.clear()
        self.currentClass = None
        self.currentPred = None

    def selectClass(self, cls_id):
        for i in range(self.classesList.count()):
            if self.classesList.item(i).text() == str(cls_id):
                self.classesList.setCurrentItem(self.classesList.item(i))

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changeClass(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentClass = current.data(QtCore.Qt.UserRole)
            self.editArgWidget.update(self.currentClass)
            self.editPredWidget.updateClass(self.currentClass)
        else:
            self.resetClass()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changePred(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        self.currentPred = current.data(QtCore.Qt.UserRole) if current else None

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updateClass(self, current):
        if current:
            cls = current.data(QtCore.Qt.UserRole)
            cls.id = current.text()

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updatePred(self, current):
        if current:
            pred = current.data(QtCore.Qt.UserRole)
            self.verbnet.replace_predicate_name(pred, current.text())
            self.editPredWidget.updateClass(self.currentClass)
            self.updatePredsList()

    @pyqtSlot()
    def save(self):
        if self.filename:
            self.verbnet.save(self.filename)
        else:
            self.saveAs()

    @pyqtSlot()
    def saveAs(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        if name:
            self.verbnet.save(name[0])
            self.filename = name[0]

    @pyqtSlot()
    def open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if name:
            self.verbnet.load(name[0])

    @pyqtSlot()
    def filterByPredicate(self):
        if self.currentPred:
            self.currentClasses = self.verbnet.get_classes_by_predicate(self.currentPred)
            self.updateClassesList()

    @pyqtSlot()
    def removeFilter(self):
        self.currentClasses = None
        self.updateClassesList()

    @pyqtSlot()
    def addClassInSense(self):
        self.plotPointWidget.addClassInSense(self.currentClass)

    def setPlotPointWidget(self, plotPointWidget):
        self.editPlotPointWidget = plotPointWidget
