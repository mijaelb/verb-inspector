import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import qt.QtUtils as QtUtils
from PyQt5.QtCore import pyqtSlot


class EditPredWidget(QtWidgets.QWidget):
    def __init__(self, vnclass=None, parent=None):
        super().__init__(parent)
        self.setObjectName('EditPredWidget')
        self.vnclass = vnclass
        self.argsLabel = QtWidgets.QLabel('Predicate arguments ▾ (Double click to edit)')
        self.predsLabel = QtWidgets.QLabel('Class predicates ▾')
        self.predsList = QtWidgets.QListWidget()
        self.argsList = QtWidgets.QListWidget()
        self.predsList.currentItemChanged.connect(self.changePred)
        self.argsList.currentItemChanged.connect(self.changeArg)
        self.argsList.itemChanged.connect(self.updateArg)
        self.predsList.itemChanged.connect(self.updatePred)
        self.argsLayout = QtWidgets.QVBoxLayout()
        self.predsLayout = QtWidgets.QVBoxLayout()

        self.argsButtonLayout = QtWidgets.QHBoxLayout()
        self.predsButtonLayout = QtWidgets.QHBoxLayout()

        self.addArgButton = QtWidgets.QPushButton('Add')
        self.addArgButton.released.connect(self.addArg)
        self.removeArgButton = QtWidgets.QPushButton('Remove')
        self.removeArgButton.released.connect(self.removeArg)
        self.upArgButton = QtWidgets.QToolButton()
        self.upArgButton.setArrowType(QtCore.Qt.UpArrow)
        self.upArgButton.released.connect(self.moveUpArg)
        self.downArgButton = QtWidgets.QToolButton()
        self.downArgButton.setArrowType(QtCore.Qt.DownArrow)
        self.downArgButton.released.connect(self.moveDownArg)

        self.addPredButton = QtWidgets.QPushButton('Add')
        self.addPredButton.released.connect(self.addPred)
        self.removePredButton = QtWidgets.QPushButton('Remove')
        self.removePredButton.released.connect(self.removePred)
        self.upPredButton = QtWidgets.QToolButton()
        self.upPredButton.setArrowType(QtCore.Qt.UpArrow)
        self.upPredButton.released.connect(self.moveUpPred)
        self.downPredButton = QtWidgets.QToolButton()
        self.downPredButton.setArrowType(QtCore.Qt.DownArrow)
        self.downPredButton.released.connect(self.moveDownPred)

        self.argsButtonLayout.addWidget(self.addArgButton)
        self.argsButtonLayout.addWidget(self.removeArgButton)
        self.argsButtonLayout.addWidget(self.upArgButton)
        self.argsButtonLayout.addWidget(self.downArgButton)

        self.predsButtonLayout.addWidget(self.addPredButton)
        self.predsButtonLayout.addWidget(self.removePredButton)
        self.predsButtonLayout.addWidget(self.upPredButton)
        self.predsButtonLayout.addWidget(self.downPredButton)

        self.argsLayout.addWidget(self.argsLabel)
        self.argsLayout.addWidget(self.argsList)
        self.argsLayout.addLayout(self.argsButtonLayout)

        self.predsLayout.addWidget(self.predsLabel)
        self.predsLayout.addWidget(self.predsList)
        self.predsLayout.addLayout(self.predsButtonLayout)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.predsLayout)
        self.layout.addLayout(self.argsLayout)
        self.initUI()

    def initUI(self):
        self.predsList.setMaximumHeight(self.predsList.sizeHint().height())
        self.argsList.setMaximumHeight(100)
        self.argsLayout.setAlignment(self.argsList, QtCore.Qt.AlignTop)
        self.predsLayout.setAlignment(self.predsList, QtCore.Qt.AlignTop)
        self.predsLayout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setAlignment(self.argsLayout, QtCore.Qt.AlignTop)
        self.layout.setAlignment(self.predsLayout, QtCore.Qt.AlignTop)
        self.setLayout(self.layout)

    def reset(self, keep=False):
        predRow = self.predsList.currentRow()
        argRow = self.argsList.currentRow()
        self.resetPredsList()
        self.resetArgsList()

        if keep:
            self.predsList.setCurrentRow(predRow)
            self.argsList.setCurrentRow(argRow)


    def resetArgsList(self):
        self.argsList.clear()
        currentItem = self.predsList.currentItem()
        if currentItem:
            pred = currentItem.data(QtCore.Qt.UserRole)
            for arg in pred.args:
                argItem = QtWidgets.QListWidgetItem(str(arg))
                argItem.setData(QtCore.Qt.UserRole, arg)
                argItem.setFlags(argItem.flags() | QtCore.Qt.ItemIsEditable)
                self.argsList.addItem(argItem)

    def resetPredsList(self):
        self.predsList.clear()
        if self.vnclass:
            for pred in self.vnclass.predicates:
                predItem = QtWidgets.QListWidgetItem(str(pred))
                predItem.setData(QtCore.Qt.UserRole, pred)
                predItem.setFlags(predItem.flags() | QtCore.Qt.ItemIsEditable)
                self.predsList.addItem(predItem)


    def updateClass(self, vnclass):
        self.vnclass = vnclass
        self.reset()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changePred(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            self.resetArgsList()

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def changeArg(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        if current:
            ...

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updateArg(self, current):
        if current:
            try:
                type_, value_ = tuple(current.text().split(': '))
                self.editedArg = current.data(QtCore.Qt.UserRole)
                self.editedArg.type = type_
                self.editedArg.value = value_
                print(self.editedArg.__repr__())
                self.reset(True)
            except:
                self.reset(True)

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def updatePred(self, current):
        if current:
            pred = current.data(QtCore.Qt.UserRole)
            text = current.text()
            str_arr = text.split('(')
            if len(str_arr) == 2:
                pred.name = str_arr[0][1:] if str_arr[0][0] == '!' else str_arr[0]
                pred.bool = str_arr[0][0] if str_arr[0][0] == '!' else ''
                str_arr[1] = str_arr[1].replace(')', '')
                print(str_arr)
                arg_arr = str_arr[1].split(',')
                if arg_arr[0] != '':
                    pred.edit_args_name(arg_arr)

            self.reset(True)

    def removeArg(self):
        if self.argsList.currentItem():
            row = self.argsList.currentRow()
            pred = self.predsList.currentItem().data(QtCore.Qt.UserRole)
            del pred.args[row]
            self.reset(True)
            self.argsList.setCurrentRow(row-1)

    def addArg(self):
        if self.predsList.currentItem():
            pred = self.predsList.currentItem().data(QtCore.Qt.UserRole)
            pred.add_arg('type', 'value')
            self.reset(True)

    def moveUpArg(self):
        if self.argsList.currentItem():
            row = self.argsList.currentRow()
            pred = self.predsList.currentItem().data(QtCore.Qt.UserRole)

            if row > 0:
                pred.args[row], pred.args[row-1] = pred.args[row-1], pred.args[row]
                self.reset(True)
                self.argsList.setCurrentRow(row-1)

    def moveDownArg(self):
        if self.argsList.currentItem():
            row = self.argsList.currentRow()
            pred = self.predsList.currentItem().data(QtCore.Qt.UserRole)

            if row < self.argsList.count() - 1:
                pred.args[row], pred.args[row + 1] = pred.args[row + 1], pred.args[row]
                self.reset(True)
                self.argsList.setCurrentRow(row+1)

    def removePred(self):
        if self.predsList.currentItem():
            row = self.predsList.currentRow()
            del self.vnclass.predicates[row]
            self.reset(True)
            self.predsList.setCurrentRow(row-1)

    def addPred(self):
        self.vnclass.add_pred('', 'name')
        self.reset(True)

    def moveUpPred(self):
        if self.predsList.currentItem():
            row = self.predsList.currentRow()
            preds = self.vnclass.predicates
            if row > 0:
                preds[row], preds[row-1] = preds[row-1], preds[row]
                self.reset(True)
                self.predsList.setCurrentRow(row-1)

    def moveDownPred(self):
        if self.predsList.currentItem():
            row = self.predsList.currentRow()
            preds = self.vnclass.predicates

            if row < self.predsList.count() - 1:
                preds[row], preds[row + 1] = preds[row + 1], preds[row]
                self.reset(True)
                self.predsList.setCurrentRow(row+1)