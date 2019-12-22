import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot
from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
import qt.QtUtils as QtUtils
from utils import utils


class EditArgWidget(QtWidgets.QWidget):
    def __init__(self, dataset='vn', parent=None):
        super().__init__(parent)
        self.dataset = dataset
        self.currentArg = None
        self.currentObj = None

        self.descrLabel = QtWidgets.QLabel('Descr: ')
        self.nameLabel = QtWidgets.QLabel('Name: ')
        self.classLabel = QtWidgets.QLabel('Class: ')
        self.slotLabel = QtWidgets.QLabel('Slot: ')

        self.descrLine = QtWidgets.QLineEdit()
        self.nameLine = QtWidgets.QLineEdit()
        self.argsSlot = QtWidgets.QSpinBox()
        self.classLine = QtWidgets.QLineEdit()
        self.argsImplicitCheckBox = QtWidgets.QCheckBox('Implicit')

        self.descrLine.textChanged.connect(self.changeDescrText)
        self.nameLine.textChanged.connect(self.changeArgText)
        self.classLine.textChanged.connect(self.changeClassText)
        self.argsSlot.valueChanged.connect(self.changeArgSlot)
        self.argsImplicitCheckBox.stateChanged.connect(self.implicitUpdate)

        self.addArgButton = QtWidgets.QPushButton('Add')
        self.removeArgButton = QtWidgets.QPushButton('Remove')
        self.addArgButton.released.connect(self.addArg)
        self.removeArgButton.released.connect(self.removeArg)

        self.vLine = QtUtils.QVLine()
        self.argsEditLayout = QtWidgets.QGridLayout()

        if dataset == 'vn':
            self.argsEditLayout.addWidget(self.nameLabel, 0, 0)
            self.argsEditLayout.addWidget(self.classLabel, 1, 0)
            self.argsEditLayout.addWidget(self.slotLabel, 2, 0)
            self.argsEditLayout.addWidget(self.nameLine, 0, 1, 1, 2)
            self.argsEditLayout.addWidget(self.classLine, 1, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsSlot, 2, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsImplicitCheckBox, 3, 1, 1, 1)
            self.argsEditLayout.addWidget(self.addArgButton, 4, 0, 1, 1)
            self.argsEditLayout.addWidget(self.removeArgButton, 4, 1, 1, 1)
            self.argsEditLayout.addWidget(self.vLine, 0, 3, 5, 1)
        elif dataset == 'pp':
            self.argsEditLayout.addWidget(self.descrLabel, 0, 0)
            self.argsEditLayout.addWidget(self.nameLabel, 1, 0)
            self.argsEditLayout.addWidget(self.classLabel, 2, 0)
            self.argsEditLayout.addWidget(self.slotLabel, 3, 0)
            self.argsEditLayout.addWidget(self.descrLine, 0, 1, 1, 2)
            self.argsEditLayout.addWidget(self.nameLine, 1, 1, 1, 2)
            self.argsEditLayout.addWidget(self.classLine, 2, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsSlot, 3, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsImplicitCheckBox, 4, 1, 1, 1)
            self.argsEditLayout.addWidget(self.addArgButton, 5, 0, 1, 1)
            self.argsEditLayout.addWidget(self.removeArgButton, 5, 1, 1, 1)
            self.argsEditLayout.addWidget(self.vLine, 0, 3, 6, 1)

        self.argDragWidget = ArgDragWidget(None)
        self.argDragWidget.selected.connect(self.selectArg)

        self.argsDragLayout = QtWidgets.QHBoxLayout()
        self.argsDragLayout.addWidget(self.argDragWidget)

        self.argsLayout = QtWidgets.QHBoxLayout()
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
        self.nameLine.setMaximumWidth(self.nameLine.sizeHint().width() - 50)
        self.vLine.setStyleSheet('QFrame { color: palette(midlight) }')
        self.addArgButton.setMaximumWidth(self.addArgButton.sizeHint().width() - 30)
        self.removeArgButton.setMaximumWidth(self.removeArgButton.sizeHint().width() - 20)
        self.argsDragLayout.setAlignment(QtCore.Qt.AlignHCenter)
        self.argsLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignLeft)
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
                self.argsSlot.setMaximum(args[-1].slot + 1)

    def clear(self):
        self.currentObj = None
        self.currentArg = None
        self.resetArg()
        self.argDragWidget.resetWidget()
        self.argsSlot.setMinimum(0)
        self.argsSlot.setMaximum(0)
        self.descrLine.setEnabled(False)
        self.nameLine.setEnabled(False)
        self.classLine.setEnabled(False)
        self.argsSlot.setEnabled(False)
        self.argsImplicitCheckBox.setEnabled(False)

    def resetArg(self):
        self.descrLine.setText('')
        self.nameLine.setText('')
        self.classLine.setText('')
        self.argsSlot.setValue(0)
        self.argsImplicitCheckBox.setChecked(False)

    def updateArg(self, current):
        if current:
            self.currentArg = current
            self.descrLine.setText(self.currentArg.arg.descr if self.dataset == 'pp' else '')
            self.nameLine.setText(self.currentArg.arg.value)
            self.classLine.setText(self.currentArg.arg.cls)
            self.argsSlot.setValue(self.currentArg.arg.slot)
            self.argsImplicitCheckBox.setChecked(self.currentArg.arg.implicit)
            self.descrLine.setEnabled(True)
            self.nameLine.setEnabled(True)
            self.classLine.setEnabled(True)
            self.argsSlot.setEnabled(True)
            self.argsImplicitCheckBox.setEnabled(True)

    @pyqtSlot(ArgDragLabel)
    def selectArg(self, current: ArgDragLabel):
        if current:
            self.updateArg(current)
        else:
            self.currentArg = None
            self.resetArg()

    @pyqtSlot(str)
    def changeArgText(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.value = text
            self.update()

    @pyqtSlot(str)
    def changeDescrText(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.descr = text
            self.update()

    @pyqtSlot(str)
    def changeClassText(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.cls = text
            self.update()

    @pyqtSlot(int)
    def changeArgSlot(self, num):
        if self.currentObj and self.currentArg:
            if len(self.currentObj.get_args()) > num:
                self.currentArg.arg.slot = num
            self.currentObj.update_slots()
            self.update()

    @pyqtSlot()
    def removeArg(self):
        if self.currentObj and self.currentArg:
            self.currentObj.remove_arg(self.currentArg.arg)
            self.currentObj.update_slots()
            self.currentArg = None
            self.resetArg()
            self.update()

    @pyqtSlot()
    def addArg(self):
        if self.currentObj:
            if self.argDragWidget.args:
                self.currentObj.add_arg('empty', '', self.argDragWidget.args[-1].slot + 1,  False)
            else:
                self.currentObj.add_arg('empty', '', 0,  False)

            self.update()

    @pyqtSlot()
    def implicitUpdate(self):
        if self.currentObj and self.currentArg:
            self.currentArg.arg.implicit = self.argsImplicitCheckBox.isChecked()
            self.update()
