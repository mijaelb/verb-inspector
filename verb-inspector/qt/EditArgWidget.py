import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot
from qt.ArgDragWidget import ArgDragWidget, ArgDragLabel
import qt.QtUtils as QtUtils
from utils import utils


class EditArgWidget(QtWidgets.QWidget):
    def __init__(self, dataset='vn', pp_container=None, parent=None):
        super().__init__(parent)
        self.pp_container = pp_container
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
        self.implicitValuesText = QtWidgets.QTextEdit()

        self.argsImplicitCheckBox = QtWidgets.QCheckBox('Implicit')

        self.descrLine.textChanged.connect(self.changeDescr)
        self.nameLine.textChanged.connect(self.changeValue)
        self.classLine.textChanged.connect(self.changeClass)
        self.argsSlot.valueChanged.connect(self.changeSlot)
        self.implicitValuesText.textChanged.connect(self.changeImplicitValues)
        self.argsImplicitCheckBox.stateChanged.connect(self.implicitUpdate)

        self.addArgButton = QtWidgets.QPushButton('Add')
        self.removeArgButton = QtWidgets.QPushButton('Remove')
        self.addArgButton.released.connect(self.addArg)
        self.removeArgButton.released.connect(self.removeArg)

        self.vLine = QtUtils.QVLine()
        self.argsEditLayout = QtWidgets.QGridLayout()

        if dataset == 'vn':
            self.argsEditLayout.addWidget(self.nameLabel, 0, 0)
            self.argsEditLayout.addWidget(self.slotLabel, 1, 0)
            self.argsEditLayout.addWidget(self.nameLine, 0, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsSlot, 1, 1, 1, 2)
            self.argsEditLayout.addWidget(self.argsImplicitCheckBox, 2, 1, 1, 1)
            self.argsEditLayout.addWidget(self.addArgButton, 3, 0, 1, 1)
            self.argsEditLayout.addWidget(self.removeArgButton, 3, 1, 1, 1)
            self.argsEditLayout.addWidget(self.vLine, 0, 3, 4, 1)
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
            self.argsEditLayout.addWidget(self.implicitValuesText, 5, 0, 3, 3)
            self.argsEditLayout.addWidget(self.addArgButton, 8, 0, 1, 1)
            self.argsEditLayout.addWidget(self.removeArgButton, 8, 1, 1, 1)
            self.argsEditLayout.addWidget(self.vLine, 0, 3, 9, 1)

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
            self.argsSlot.setMinimum(0)
            self.argsSlot.setMaximum(args[-1].slot + 1 if args else 0)

    def clear(self):
        self.currentObj = None
        self.currentArg = None
        self.resetArg()
        self.argDragWidget.clearWidget()
        self.argsSlot.setMinimum(0)
        self.argsSlot.setMaximum(0)
        self.descrLine.setEnabled(False)
        self.nameLine.setEnabled(False)
        self.classLine.setEnabled(False)
        self.argsSlot.setEnabled(False)
        self.argsImplicitCheckBox.setEnabled(False)
        self.implicitValuesText.setEnabled(False)

    def resetArg(self):
        self.descrLine.setText('')
        self.nameLine.setText('')
        self.classLine.setText('')
        self.argsSlot.setValue(0)
        self.argsImplicitCheckBox.setChecked(False)
        self.implicitValuesText.setText('')

    def updateArg(self, current):
        if current:
            self.currentArg = current
            self.descrLine.blockSignals(True)
            self.nameLine.blockSignals(True)
            self.classLine.blockSignals(True)
            self.implicitValuesText.blockSignals(True)
            self.descrLine.setText(self.currentArg.arg.descr if self.dataset == 'pp' else '')
            self.nameLine.setText(self.currentArg.arg.value)
            self.classLine.setText(self.currentArg.arg.cls)
            self.argsSlot.setValue(self.currentArg.arg.slot)
            if len(self.currentArg.arg.implicit_values) > 1:
                implicit_values = ','.join(self.currentArg.arg.implicit_values)
            else:
                implicit_values = ''.join(self.currentArg.arg.implicit_values)
            self.implicitValuesText.setText(implicit_values)
            self.argsImplicitCheckBox.setChecked(self.currentArg.arg.implicit)
            self.descrLine.blockSignals(False)
            self.nameLine.blockSignals(False)
            self.classLine.blockSignals(False)
            self.implicitValuesText.blockSignals(False)
            self.descrLine.setEnabled(True)
            self.nameLine.setEnabled(True)
            self.classLine.setEnabled(True)
            self.argsSlot.setEnabled(True)
            self.implicitValuesText.setEnabled(True)
            self.argsImplicitCheckBox.setEnabled(True)

    @pyqtSlot(ArgDragLabel)
    def selectArg(self, current: ArgDragLabel):
        if current:
            self.updateArg(current)
        else:
            self.currentArg = None
            self.resetArg()

    @pyqtSlot(str)
    def changeValue(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.setValue(text)
            self.update()

    @pyqtSlot(str)
    def changeDescr(self, text):
        if self.currentObj and self.currentArg:
            self.currentArg.setDescr(text)
            self.update()

    @pyqtSlot(str)
    def changeClass(self, text):
        if self.pp_container and self.currentObj and self.currentArg:
            self.currentArg.setClass(text, self.currentObj, self.pp_container.verbnet)
            self.parent().updateClassesList()
            self.update()

    @pyqtSlot(int)
    def changeSlot(self, num):
        if self.currentObj and self.currentArg:
            if self.currentObj.get_args()[-1].slot + 1 >= num:
                self.currentArg.setSlot(num)
            self.currentObj.update_slots()
            self.update()

    @pyqtSlot()
    def changeImplicitValues(self):
        if self.currentObj and self.currentArg:
            values = ' '.join(self.implicitValuesText.toPlainText().split(',')).lstrip().rstrip().split()
            if isinstance(values, list):
                self.currentArg.setImplicitValues(values)
            elif values != '':
                self.currentArg.setImplicitValues([values])

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
