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
        self.currentArg = None
        self.currentClass = None

        self.argsLabel = QtWidgets.QLabel('Argument structure ')
        self.classesLabel = QtWidgets.QLabel('Classes ▾')

        self.editArgsWidget = self.createClassArgs(None)

        self.editArgsLine = QtWidgets.QLineEdit()
        self.editArgsLine.setMaximumWidth(self.argsLabel.sizeHint().width())
        self.editArgsLine.textChanged.connect(self.changeArgText)

        self.hLine = QtUtils.QHLine()

        self.classesList = self.createClassesList()
        self.classSelectLayout = QtWidgets.QVBoxLayout()
        self.classSelectLayout.addWidget(self.classesLabel)
        self.classSelectLayout.addWidget(self.classesList)

        self.editPredWidget = EditPredWidget()

        self.argsEditLabelLayout = QtWidgets.QVBoxLayout()
        self.argsEditLabelLayout.addWidget(self.argsLabel)
        self.argsEditLabelLayout.addWidget(self.editArgsLine)

        self.argsLayout = QtWidgets.QHBoxLayout()
        self.editArgsLayout = QtWidgets.QHBoxLayout()

        self.argsLayout.addLayout(self.argsEditLabelLayout)
        self.argsLayout.addLayout(self.editArgsLayout)

        self.editClassLayout = QtWidgets.QVBoxLayout()
        self.editClassLayout.addLayout(self.argsLayout)
        self.editClassLayout.addWidget(self.hLine)
        self.editClassLayout.addWidget(self.editPredWidget)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.classSelectLayout)
        self.layout.addLayout(self.editClassLayout)

        self.initUI()

    def initUI(self):
        self.argsLabel.setStyleSheet('QLabel { color: palette(midlight); }')
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.argsLayout.setAlignment(self.editArgsLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)

    def createClassesList(self):
        classesList = QtWidgets.QListWidget()
        for id, cls in self.verbnet.get_classes().items():
            classItem = QtWidgets.QListWidgetItem(id)
            classItem.setData(QtCore.Qt.UserRole, cls)
            classesList.addItem(classItem)

        classesList.currentItemChanged.connect(self.changeClass)
        return classesList

    def createClassArgs(self, vnclass):
        if vnclass:
            QtUtils.clearLayout(self.editArgsLayout)
            widget = ArgDragWidget(vnclass.args, self)
            widget.selected.connect(self.selectArg)
            self.editArgsLayout.addWidget(widget)
            self.editArgsLayout.setAlignment(QtCore.Qt.AlignHCenter)
            self.argsLayout.setAlignment(self.editArgsLayout, QtCore.Qt.AlignLeft)
            return widget
        return None

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changeClass(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        cls = current.data(QtCore.Qt.UserRole)
        self.currentClass = cls
        self.currentArg = None
        self.editArgsLine.setText('')
        self.createClassArgs(cls)
        self.editPredWidget.updateClass(cls)

    @pyqtSlot(ArgDragLabel)
    def selectArg(self, current: ArgDragLabel):
        self.currentArg = current
        self.editArgsLine.setText(current.label_text)
        print(current.label_text)

    @pyqtSlot(str)
    def changeArgText(self, text):
        if self.currentArg:
            self.currentArg.arg.edit(text)
            self.editArgsWidget = self.createClassArgs(self.currentClass)
            print(self.currentClass.args)
