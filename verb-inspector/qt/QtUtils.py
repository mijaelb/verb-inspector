import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import os
import qtpy

QT_VERSION = tuple(int(v) for v in qtpy.QT_VERSION.split('.'))
""" tuple: Qt version. """

def DarkPalette():
    darkPalette = QtGui.QPalette()
    darkPalette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    darkPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    #darkPalette.setColor(QtGui.QPalette.)
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtCore.Qt.darkGray)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtCore.Qt.darkGray)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtCore.Qt.darkGray)
    return darkPalette


def clearLayout(layout):
    for i in reversed(range(layout.count())):
        widget = layout.takeAt(i).widget()
        if widget:
            widget.setParent(None)

def clearTable(table):
    table.setRowCount(0)
    table.setColumnCount(0)

_STYLESHEET =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/style.qss')
""" str: Main stylesheet. """

def _apply_base_theme(app):
    """ Apply base theme to the application.

        Args:
            app (QApplication): QApplication instance.
    """

    if QT_VERSION < (5,):
        app.setStyle(QtWidgets.QStyleFactory.create('plastique'))
    else:
        app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    with open(_STYLESHEET) as stylesheet:
        app.setStyleSheet(stylesheet.read())


def dark(app):
    """ Apply Dark Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    darkPalette = QtGui.QPalette()

    # base
    darkPalette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.Light, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Midlight, QtGui.QColor(90, 90, 90))
    darkPalette.setColor(QtGui.QPalette.Dark, QtGui.QColor(35, 35, 35))
    darkPalette.setColor(QtGui.QPalette.Text, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(42, 42, 42))
    darkPalette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.Shadow, QtGui.QColor(20, 20, 20))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(56, 252, 196))
    darkPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(66, 66, 66))
    darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(180, 180, 180))

    # disabled
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         QtGui.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text,
                         QtGui.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText,
                         QtGui.QColor(127, 127, 127))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight,
                         QtGui.QColor(80, 80, 80))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText,
                         QtGui.QColor(127, 127, 127))

    app.setPalette(darkPalette)

    _apply_base_theme(app)


def light(app):
    """ Apply Light Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    lightPalette = QtGui.QPalette()

    # base
    lightPalette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))
    lightPalette.setColor(QtGui.QPalette.Button, QtGui.QColor(240, 240, 240))
    lightPalette.setColor(QtGui.QPalette.Light, QtGui.QColor(180, 180, 180))
    lightPalette.setColor(QtGui.QPalette.Midlight, QtGui.QColor(200, 200, 200))
    lightPalette.setColor(QtGui.QPalette.Dark, QtGui.QColor(225, 225, 225))
    lightPalette.setColor(QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))
    lightPalette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(0, 0, 0))
    lightPalette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0))
    lightPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(237, 237, 237))
    lightPalette.setColor(QtGui.QPalette.Window, QtGui.QColor(240, 240, 240))
    lightPalette.setColor(QtGui.QPalette.Shadow, QtGui.QColor(20, 20, 20))
    lightPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(76, 163, 224))
    lightPalette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0, 0, 0))
    lightPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(0, 162, 232))
    lightPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(225, 225, 225))
    lightPalette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(240, 240, 240))
    lightPalette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(0, 0, 0))

    # disabled
    lightPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                          QtGui.QColor(115, 115, 115))
    lightPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text,
                          QtGui.QColor(115, 115, 115))
    lightPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText,
                          QtGui.QColor(115, 115, 115))
    lightPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight,
                          QtGui.QColor(190, 190, 190))
    lightPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText,
                          QtGui.QColor(115, 115, 115))

    app.setPalette(lightPalette)

    _apply_base_theme(app)

def sizeHint(list):
    s = QtCore.QSize()
    s.setHeight(list.sizeHint().height())
    s.setWidth(list.sizeHintForColumn(0))
    return s

class QHLine(QtWidgets.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Plain)


class QVLine(QtWidgets.QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setFrameShadow(QtWidgets.QFrame.Plain)

# self.args_class_table.setMaximumHeight(32)
# hheader = self.args_class_table.horizontalHeader()
# vheader = self.args_class_table.verticalHeader()
# hheader.hide()
# vheader.hide()
# vheader.setStretchLastSection(True)
# #hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
# vheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
# hheader.setDefaultAlignment(Qt.AlignCenter)
# self.args_class_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
# # tableview.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum) # ---
# self.args_class_table.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
# #hheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)