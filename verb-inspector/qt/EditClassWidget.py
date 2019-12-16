import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot

from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
from qt.EditPredWidget import EditPredWidget
import qt.QtUtils as QtUtils

CLASS_LIST_WIDTH = 225


class EditClassWidget(QtWidgets.QWidget):
    def __init__(self, vn, parent=None):
        super().__init__(parent)
        self.verbnet = vn
        self.filename = None
        self.currentArg = None
        self.currentClass = None
        self.currentPred = None
        self.currentClasses = None

        self.argsLabel = QtWidgets.QLabel('Argument structure: ')
        self.argsLabel.setStyleSheet('QLabel { color: palette(midlight); }')
        self.slotLabel = QtWidgets.QLabel('Slot: ')
        self.nameLabel = QtWidgets.QLabel('Name: ')
        self.classesLabel = QtWidgets.QLabel('Classes ▾')

        self.editArgsWidget = self.createClassArgs(None)
        self.addArgButton = QtWidgets.QPushButton('Add')
        self.addArgButton.released.connect(self.addArg)
        self.removeArgButton = QtWidgets.QPushButton('Remove')
        self.removeArgButton.released.connect(self.removeArg)

        self.argsLine = QtWidgets.QLineEdit()
        self.argsLine.textChanged.connect(self.changeArgText)
        self.argsSlot = QtWidgets.QSpinBox()
        self.argsSlot.valueChanged.connect(self.changeArgSlot)

        self.hLine = QtUtils.QHLine()
        self.vLine = QtUtils.QVLine()
        self.saveButton = QtWidgets.QPushButton('Save')
        self.saveButton.released.connect(self.save)
        self.saveAsButton = QtWidgets.QPushButton('Save As')
        self.saveAsButton.released.connect(self.saveAs)
        self.openButton = QtWidgets.QPushButton('Open')
        self.openButton.released.connect(self.open)

        self.classButtons = QtWidgets.QHBoxLayout()
        self.classButtons.addWidget(self.saveButton)
        self.classButtons.addWidget(self.saveAsButton)
        self.classButtons.addWidget(self.openButton)

        self.filterByPredicateButton = QtWidgets.QPushButton('Class by predicate')
        self.removeFilterButton = QtWidgets.QPushButton('Unfilter')
        self.filterByPredicateButton.released.connect(self.filterByPredicate)
        self.removeFilterButton.released.connect(self.removeFilter)
        self.filterButtons = QtWidgets.QHBoxLayout()
        self.filterButtons.addWidget(self.filterByPredicateButton)
        self.filterButtons.addWidget(self.removeFilterButton)

        self.predsListLabel = QtWidgets.QLabel('All predicates ▾')
        self.predsList = QtWidgets.QListWidget()
        self.createPredsList()
        self.predsList.itemChanged.connect(self.updatePredsList)

        self.classesList = QtWidgets.QListWidget()
        self.createClassesList()
        self.classesList.itemChanged.connect(self.updateClassList)

        self.classSelectLayout = QtWidgets.QVBoxLayout()
        self.classSelectLayout.addWidget(self.classesLabel)
        self.classSelectLayout.addWidget(self.classesList)
        self.classSelectLayout.addWidget(self.predsListLabel)
        self.classSelectLayout.addWidget(self.predsList)
        self.classSelectLayout.addLayout(self.filterButtons)
        self.classSelectLayout.addLayout(self.classButtons)

        self.editPredWidget = EditPredWidget()

        self.argsEditLayout = QtWidgets.QGridLayout()
        self.argsImplicitCheckBox = QtWidgets.QCheckBox('Implicit')
        self.argsImplicitCheckBox.stateChanged.connect(self.implicitUpdate)

        self.argsEditLayout.addWidget(self.argsLabel, 0, 0, 1, 4)
        self.argsEditLayout.addWidget(self.nameLabel, 1, 0)
        self.argsEditLayout.addWidget(self.slotLabel, 2, 0)
        self.argsEditLayout.addWidget(self.argsLine, 1, 1, 1, 2)
        self.argsEditLayout.addWidget(self.argsSlot, 2, 1, 1, 2)
        self.argsEditLayout.addWidget(self.argsImplicitCheckBox, 3, 1, 1, 1)
        self.argsEditLayout.addWidget(self.addArgButton, 4, 0, 1, 1)
        self.argsEditLayout.addWidget(self.removeArgButton, 4, 1, 1, 1)
        self.argsEditLayout.addWidget(self.vLine, 0, 3, 5, 1)

        self.argsLayout = QtWidgets.QHBoxLayout()
        self.argsDragLayout = QtWidgets.QHBoxLayout()

        self.argsLayout.addLayout(self.argsEditLayout)
        self.argsLayout.addLayout(self.argsDragLayout)

        self.editClassLayout = QtWidgets.QVBoxLayout()
        self.editClassLayout.addLayout(self.argsLayout)
        self.editClassLayout.addWidget(self.hLine)
        self.editClassLayout.addWidget(self.editPredWidget)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.classSelectLayout)
        self.layout.addLayout(self.editClassLayout)

        self.setLayout(self.layout)
        self.initUI()

    def initUI(self):
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.vLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.predsListLabel.setStyleSheet('QLabel { color: palette(midlight); }')
        self.argsSlot.setMaximumWidth(self.argsSlot.sizeHint().width())
        self.argsLine.setMaximumWidth(self.argsLine.sizeHint().width() - 50)
        self.classesList.setMaximumWidth(self.classesList.sizeHint().width())
        self.predsList.setMaximumWidth(self.predsList.sizeHint().width())
        self.predsList.setMaximumHeight(150)
        self.addArgButton.setMaximumWidth(self.addArgButton.sizeHint().width() - 30)
        self.removeArgButton.setMaximumWidth(self.removeArgButton.sizeHint().width() - 20)

        self.argsLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.classSelectLayout.setAlignment(QtCore.Qt.AlignTop)
        self.argsLayout.setAlignment(self.argsEditLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(self.argsDragLayout, QtCore.Qt.AlignLeft)
        self.layout.setAlignment(self.classSelectLayout, QtCore.Qt.AlignTop)

    def createClassesList(self):
        self.classesList.clear()
        self.classesList.currentItemChanged.connect(self.changeClass)
        classes = self.verbnet.get_classes() if not self.currentClasses else self.currentClasses
        for cls in classes.values():
            classItem = QtWidgets.QListWidgetItem(cls.id)
            classItem.setData(QtCore.Qt.UserRole, cls)
            classItem.setFlags(classItem.flags() | QtCore.Qt.ItemIsEditable)
            self.classesList.addItem(classItem)

    def createPredsList(self):
        self.predsList.currentItemChanged.connect(self.changePredicate)
        for pred in self.verbnet.get_all_predicates_name():
            predItem = QtWidgets.QListWidgetItem(pred)
            predItem.setData(QtCore.Qt.UserRole, pred)
            predItem.setFlags(predItem.flags() | QtCore.Qt.ItemIsEditable)
            self.predsList.addItem(predItem)

    def createClassArgs(self, vnclass, selected=None):
        if vnclass:
            QtUtils.clearLayout(self.argsDragLayout)
            widget = ArgDragWidget(vnclass.args, self, selected)
            widget.selected.connect(self.selectArg)
            self.argsDragLayout.addWidget(widget)
            self.argsDragLayout.setAlignment(QtCore.Qt.AlignHCenter)
            self.argsLayout.setAlignment(self.argsDragLayout, QtCore.Qt.AlignLeft)
            isSelected = True if selected else False
            self.argsLine.setEnabled(isSelected)
            self.argsImplicitCheckBox.setEnabled(isSelected)
            self.argsSlot.setEnabled(isSelected)
            self.argsSlot.setMinimum(0)
            self.argsSlot.setMaximum(len(self.currentClass.args) - 1)
            return widget
        return None

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changeClass(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            cls = current.data(QtCore.Qt.UserRole)
            self.currentClass = cls
            self.currentArg = None
            self.argsLine.setText('')
            self.createClassArgs(cls)
            self.editPredWidget.updateClass(cls)
        else:
            self.currentClass = None

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changePredicate(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.currentPred = current.data(QtCore.Qt.UserRole)
        else:
            self.currentPred = None

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updateClassList(self, current):
        if current:
            cls = current.data(QtCore.Qt.UserRole)
            cls.id = current.text()

    @pyqtSlot(ArgDragLabel)
    def selectArg(self, current: ArgDragLabel):
        self.currentArg = current
        self.argsLine.setText(current.arg.value)
        self.argsImplicitCheckBox.setChecked(current.arg.implicit)
        self.argsSlot.setValue(current.arg.slot)

    @pyqtSlot(str)
    def changeArgText(self, text):
        if self.currentArg:
            self.currentArg.arg.value = text
            self.editArgsWidget = self.createClassArgs(self.currentClass, self.currentArg)

    @pyqtSlot(int)
    def changeArgSlot(self, num):
        if self.currentArg:
            if len(self.currentClass.args) > num:
                self.currentArg.arg.slot = num
            self.currentClass.updateSlots()
            self.editArgsWidget = self.createClassArgs(self.currentClass, self.currentArg)

    @pyqtSlot()
    def removeArg(self):
        if self.currentArg:
            ...

    @pyqtSlot()
    def addArg(self):
        ...

    @pyqtSlot()
    def implicitUpdate(self):
        if self.currentArg:
            self.currentArg.arg.implicit = self.argsImplicitCheckBox.isChecked()
            self.editArgsWidget = self.createClassArgs(self.currentClass, self.currentArg)

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

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updatePredsList(self, current):
        if current:
            pred = current.data(QtCore.Qt.UserRole)
            self.verbnet.replace_predicate_name(pred, current.text())
            self.editPredWidget.updateClass(self.currentClass)
            self.predsList.clear()
            for pred in self.verbnet.get_all_predicates_name():
                predItem = QtWidgets.QListWidgetItem(pred)
                predItem.setData(QtCore.Qt.UserRole, pred)
                predItem.setFlags(predItem.flags() | QtCore.Qt.ItemIsEditable)
                self.predsList.addItem(predItem)

    @pyqtSlot()
    def filterByPredicate(self):
        if self.currentPred:
            self.currentClasses = self.verbnet.get_classes_by_predicate(self.currentPred)
            self.createClassesList()

    @pyqtSlot()
    def removeFilter(self):
        self.currentClasses = None
        self.createClassesList()
