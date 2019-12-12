import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

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
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    darkPalette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtCore.Qt.darkGray)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtCore.Qt.darkGray)
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtCore.Qt.darkGray)
    return darkPalette

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