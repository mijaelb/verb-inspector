import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot
from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
import qt.QtUtils as QtUtils
from utils import utils


class EditArgWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.currentArg = None
        self.currentObj = None

        self.slotLabel = QtWidgets.QLabel('Slot: ')
        self.nameLabel = QtWidgets.QLabel('Name: ')

        self.argsLine = QtWidgets.QLineEdit()
        self.argsSlot = QtWidgets.QSpinBox()
        self.argsImplicitCheckBox = QtWidgets.QCheckBox('Implicit')
        self.argsLine.textChanged.connect(self.changeArgText)
        self.argsSlot.valueChanged.connect(self.changeArgSlot)
        self.argsImplicitCheckBox.stateChanged.connect(self.implicitUpdate)

        self.addArgButton = QtWidgets.QPushButton('Add')
        self.removeArgButton = QtWidgets.QPushButton('Remove')
        self.addArgButton.released.connect(self.addArg)
        self.removeArgButton.released.connect(self.removeArg)

        self.vLine = QtUtils.QVLine()
        self.argsEditLayout = QtWidgets.QGridLayout()
        self.argsEditLayout.addWidget(self.nameLabel, 0, 0)
        self.argsEditLayout.addWidget(self.slotLabel, 1, 0)
        self.argsEditLayout.addWidget(self.argsLine, 0, 1, 1, 2)
        self.argsEditLayout.addWidget(self.argsSlot, 1, 1, 1, 2)
        self.argsEditLayout.addWidget(self.argsImplicitCheckBox, 2, 1, 1, 1)
        self.argsEditLayout.addWidget(self.addArgButton, 3, 0, 1, 1)
        self.argsEditLayout.addWidget(self.removeArgButton, 3, 1, 1, 1)
        self.argsEditLayout.addWidget(self.vLine, 0, 3, 4, 1)

        self.argDragWidget = ArgDragWidget(None)
        self.argDragWidget.selected.connect(self.selectArg)

        self.argsLayout = QtWidgets.QHBoxLayout()
        self.argsDragLayout = QtWidgets.QHBoxLayout()

        self.argsDragLayout.addWidget(self.argDragWidget)

        self.argsLayout.addLayout(self.argsEditLayout)
        self.argsLayout.addLayout(self.argsDragLayout)
        self.argsLayout.addStretch(1)

        self.groupEditArgs = QtWidgets.QGroupBox('Argument Structure')
        self.groupEditArgs.setLayout(self.argsLayout)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.groupEditArgs)
        self.setLayout(self.layout)

    def initUI(self):
        self.argsSlot.setMaximumWidth(self.argsSlot.sizeHint().width())
        self.argsLine.setMaximumWidth(self.argsLine.sizeHint().width() - 50)
        self.vLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.addArgButton.setMaximumWidth(self.addArgButton.sizeHint().width() - 30)
        self.removeArgButton.setMaximumWidth(self.removeArgButton.sizeHint().width() - 20)
        self.argsLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignLeft)
        self.argsDragLayout.setAlignment(QtCore.Qt.AlignHCenter)
        self.argsLayout.setAlignment(self.argsDragLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(self.argsEditLayout, QtCore.Qt.AlignLeft)
        self.argsLayout.setAlignment(self.argsDragLayout, QtCore.Qt.AlignLeft)

    def update(self, obj=None):
        self.currentObj = obj if obj else self.currentObj
        if self.currentObj:
            args = self.currentObj.get_args()
            self.argDragWidget.resetWidget(args, self.currentArg)
            self.updateArg(self.currentArg)
            if args:
                self.argsSlot.setMinimum(0)
                self.argsSlot.setMaximum(len(args) + 1)

    def clear(self):
        self.currentObj = None
        self.resetArg()
        self.argDragWidget.resetWidget()
        self.argsSlot.setMinimum(0)
        self.argsSlot.setMaximum(0)
        self.argsLine.setEnabled(False)
        self.argsSlot.setEnabled(False)
        self.argsImplicitCheckBox.setEnabled(False)

    def resetArg(self):
        self.argsLine.setText('')
        self.argsImplicitCheckBox.setChecked(False)
        self.argsSlot.setValue(0)

    def updateArg(self, current):
        if current:
            self.currentArg = current
            self.argsLine.setText(self.currentArg.arg.value)
            self.argsImplicitCheckBox.setChecked(self.currentArg.arg.implicit)
            self.argsSlot.setValue(self.currentArg.arg.slot)
            self.argsLine.setEnabled(True)
            self.argsSlot.setEnabled(True)
            self.argsImplicitCheckBox.setEnabled(True)
        else:
            self.resetArg()

    @pyqtSlot(ArgDragLabel)
    def selectArg(self, current: ArgDragLabel):
        if current:
            self.updateArg(current)
        else:
            self.currentArg = None

    @pyqtSlot(str)
    def changeArgText(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.value = text
            self.update()

    @pyqtSlot(int)
    def changeArgSlot(self, num):
        if self.currentObj and self.currentArg:
            if len(self.currentObj.get_args()) > num:
                self.currentArg.arg.slot = num
            self.currentObj.updateSlots()
            self.update()

    @pyqtSlot()
    def removeArg(self):
        if self.currentObj and self.currentArg:
            self.currentObj.remove_arg(self.currentArg.arg)
            self.currentObj.updateSlots()
            self.currentArg = None
            self.update()

    @pyqtSlot()
    def addArg(self):
        if self.currentObj:
            if self.argsDragWidget.args:
                self.currentObj.add_arg('empty', False, self.argDragWidget.args[-1].slot + 1, '')
            else:
                self.currentObj.add_arg('empty', False, 0, '')

            self.update()

    @pyqtSlot()
    def implicitUpdate(self):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.implicit = self.argsImplicitCheckBox.isChecked()
            self.update()
