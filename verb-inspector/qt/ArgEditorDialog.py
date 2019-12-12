import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import qt.QtUtils as QtUtils


class ArgEditorDialog(QtWidgets.QDialog):
    def __init__(self, arg, parent=None):
        super(ArgEditorDialog, self).__init__(parent)
        self.left = 40
        self.top = 40
        self.width = 200
        self.height = 200
        self.arg = arg
        self.title = 'Argument Editor'
        self.name = ' '.join(arg.value)

        self.layout = QtWidgets.QGridLayout()

        self.edit_name_line = QtWidgets.QLineEdit(self.name)

        self.implicit_checkbox = QtWidgets.QCheckBox('ImplicitCheckBox')
        self.implicit_checkbox.setChecked(arg.implicit)
        self.implicit_checkbox.stateChanged.connect(lambda: self.checkbox_state(self.implicit_checkbox))
        self.implicit_checkbox.setStyleSheet("color: white")

        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.setPalette(QtUtils.DarkPalette())
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.layout)
        self.layout.addWidget(self.edit_name_line)
        self.layout.addWidget(self.implicit_checkbox)
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.setPalette(QtUtils.DarkPalette())
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile(f'../gui/icons/32x32.png', QtCore.QSize(32, 32))
        self.setWindowIcon(self.app_icon)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.parent().reset()

    def checkbox_state(self, b):
        if b.text() == 'ImplicitCheckBox':
            self.arg.implicit = b.isChecked()
