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

        self.argsLabel = QtWidgets.QLabel('Argument structure: ')
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

        self.classesList = self.createClassesList()
        self.classesList.itemChanged.connect(self.updateClassList)
        self.classSelectLayout = QtWidgets.QVBoxLayout()
        self.classSelectLayout.addWidget(self.classesLabel)
        self.classSelectLayout.addWidget(self.classesList)
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

        self.initUI()

    def initUI(self):
        self.addArgButton.setMaximumWidth(self.addArgButton.sizeHint().width() - 30)
        self.removeArgButton.setMaximumWidth(self.removeArgButton.sizeHint().width() - 20)
        self.argsSlot.setMaximumWidth(self.argsSlot.sizeHint().width())
        self.argsLine.setMaximumWidth(self.argsLine.sizeHint().width()-50)
        self.classesList.setMaximumWidth(self.classesList.sizeHint().width())
        self.argsLabel.setStyleSheet('QLabel { color: palette(midlight); }')
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.vLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.argsEditLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(self.argsEditLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(self.argsDragLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)

    def createClassesList(self):
        classesList = QtWidgets.QListWidget()
        for id, cls in self.verbnet.get_classes().items():
            classItem = QtWidgets.QListWidgetItem(id)
            classItem.setData(QtCore.Qt.UserRole, cls)
            classItem.setFlags(classItem.flags() | QtCore.Qt.ItemIsEditable)
            classesList.addItem(classItem)

        classesList.currentItemChanged.connect(self.changeClass)
        return classesList

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
        cls = current.data(QtCore.Qt.UserRole)
        self.currentClass = cls
        self.currentArg = None
        self.argsLine.setText('')
        self.createClassArgs(cls)
        self.editPredWidget.updateClass(cls)

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