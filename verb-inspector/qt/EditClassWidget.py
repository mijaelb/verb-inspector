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
    def __init__(self, pp_container, parent=None):
        super().__init__(parent)
        self.pp_container = pp_container
        self.filename = self.pp_container.verbnet.json_path
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

        self.reloadClassButton = QtWidgets.QPushButton('Reload Class')
        self.reloadClassButton.released.connect(self.reloadClass)

        self.classButtons = QtWidgets.QHBoxLayout()
        self.classButtons.addWidget(self.saveButton)
        self.classButtons.addWidget(self.saveAsButton)
        self.classButtons.addWidget(self.openButton)

        self.classCleanedCheckBox = QtWidgets.QCheckBox('Cleaned')
        self.classCleanedCheckBox.stateChanged.connect(self.classCleaned)

        self.filterByCleanedButton = QtWidgets.QPushButton('By cleaned')
        self.filterByPredicateButton = QtWidgets.QPushButton('By predicate')
        self.removeFilterButton = QtWidgets.QPushButton('Unfilter')
        self.filterByCleanedButton.released.connect(self.filterByCleaned)
        self.filterByPredicateButton.released.connect(self.filterByPredicate)
        self.removeFilterButton.released.connect(self.removeFilter)

        self.filterButtons = QtWidgets.QHBoxLayout()
        self.filterButtons.addWidget(self.filterByPredicateButton)
        self.filterButtons.addWidget(self.filterByCleanedButton)
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
        self.classSelectLayout.addWidget(self.reloadClassButton)
        self.classSelectLayout.addWidget(self.classesLabel)
        self.classSelectLayout.addWidget(self.classesList)
        self.classSelectLayout.addWidget(self.classCleanedCheckBox)
        self.classSelectLayout.addWidget(self.predsListLabel)
        self.classSelectLayout.addWidget(self.predsList)
        self.classSelectLayout.addLayout(self.filterButtons)
        self.classSelectLayout.addLayout(self.classButtons)

        self.editPredWidget = EditPredWidget(parent=self)

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
        self.classesList.setStyleSheet('QLabel { color: palette(midlight); }')
        self.classesList.setMaximumWidth(self.classesList.sizeHint().width())
        self.predsList.setMaximumWidth(self.predsList.sizeHint().width())
        self.predsList.setMaximumHeight(150)
        self.classSelectLayout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setAlignment(self.classSelectLayout, QtCore.Qt.AlignTop)

    def updateClassesList(self):
        self.classesList.clear()
        classes = self.pp_container.verbnet.get_classes() if not self.currentClasses else self.currentClasses
        for cls in classes.values():
            classItem = QtWidgets.QListWidgetItem(cls.id)
            classItem.setData(QtCore.Qt.UserRole, cls)
            classItem.setFlags(classItem.flags() | QtCore.Qt.ItemIsEditable)
            classItem.setBackground(QtGui.QBrush(QtCore.Qt.green) if cls.cleaned else QtGui.QBrush(QtCore.Qt.white))
            self.classesList.addItem(classItem)

    def updatePredsList(self):
        self.predsList.clear()
        for pred in self.pp_container.verbnet.get_all_predicates_name():
            # utils.write('predicate_names.log', pred + '\n', 'a+')
            predItem = QtWidgets.QListWidgetItem(pred)
            predItem.setData(QtCore.Qt.UserRole, pred)
            predItem.setFlags(predItem.flags() | QtCore.Qt.ItemIsEditable)
            self.predsList.addItem(predItem)

    def getClass(self):
        return self.currentClass.data(QtCore.Qt.UserRole) if self.currentClass else None

    def getPredicate(self):
        return self.currentPred

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
            self.currentClass = current
            cls = current.data(QtCore.Qt.UserRole)
            self.classCleanedCheckBox.blockSignals(True)
            self.classCleanedCheckBox.setChecked(cls.cleaned)
            self.classCleanedCheckBox.blockSignals(False)
            self.editArgWidget.resetArg()
            self.editArgWidget.update(cls)
            self.editPredWidget.updateClass(cls)

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changePred(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        self.currentPred = current.data(QtCore.Qt.UserRole) if current else None

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updateClass(self, current):
        if current:
            cls = current.data(QtCore.Qt.UserRole)
            self.pp_container.change_class_name(cls.id, current.text())
            self.editArgWidget.update(cls)
            if self.editPlotPointWidget:
                self.editPlotPointWidget.refreshClasses()

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updatePred(self, current):
        if current:
            pred = current.data(QtCore.Qt.UserRole)
            cls = self.getClass()
            self.pp_container.replace_predicate_name(pred, current.text())
            self.editPredWidget.updateClass(cls)
            self.updatePredsList()
            if self.editPlotPointWidget:
                self.editPlotPointWidget.refreshPredicates()

    def reloadClass(self):
        cls = self.getClass()
        if cls:
            cls.reload()
            self.editArgWidget.update(cls)
            self.editPredWidget.updateClass(cls)
            self.updatePredsList()

    @pyqtSlot()
    def save(self):
        if self.filename:
            self.pp_container.verbnet.save(self.filename)
        else:
            self.saveAs()

    @pyqtSlot()
    def saveAs(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', "", "Json files (*.json)")[0]
        if name:
            if not QtCore.QFileInfo(name).suffix():
                name += ".json"
            self.pp_container.verbnet.save(name)
            self.filename = name

    @pyqtSlot()
    def open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if name:
            self.pp_container.verbnet.load(name[0])
            self.currentClasses = None
            self.resetClass()
            self.updateClassesList()
            self.editArgWidget.clear()
            self.editPredWidget.updateClass()
            self.updatePredsList()

    @pyqtSlot()
    def filterByPredicate(self):
        if self.currentPred:
            self.currentClasses = self.pp_container.verbnet.get_classes_by_predicate(self.currentPred)
            self.updateClassesList()

    @pyqtSlot()
    def filterByCleaned(self):
        self.currentClasses = self.pp_container.verbnet.get_cleaned_classes()
        self.updateClassesList()

    @pyqtSlot()
    def removeFilter(self):
        self.currentClasses = None
        self.updateClassesList()

    @pyqtSlot()
    def classCleaned(self):
        cls = self.getClass()
        if cls:
            cls.cleaned = self.classCleanedCheckBox.isChecked()
            self.currentClass.setBackground(QtGui.QBrush(QtCore.Qt.green) if cls.cleaned else QtGui.QBrush(QtCore.Qt.white))

    def setPlotPointWidget(self, plotPointWidget):
        self.editPlotPointWidget = plotPointWidget
