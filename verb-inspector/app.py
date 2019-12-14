# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:58:40 2019

@author: Mijael
"""
import sys
import os
import json
import xml.etree.ElementTree as ET
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QIcon
from pathlib import Path
import pp
from qt.EditClassWidget import EditClassWidget

import qt.QtUtils as QtUtils
from qt.QtUtils import QT_VERSION

_FL_STYLESHEET = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qt/resources/frameless.qss')

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Plot Point Editor (Verb Inspector)'
        self.path = os.path.dirname(__file__)
        self.pp_container = pp.PlotPointContainer()
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 800
        self.hLine = QtUtils.QHLine()
        self.editClassWidget = EditClassWidget(self.pp_container.verbnet_simplified)
        self.editClassWidget.setMaximumHeight(400)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.hLine)
        self.layout.addWidget(self.editClassWidget)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.hLine.setStyleSheet('QFrame { color: palette(midlight) }')

        with open(_FL_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())
        QtUtils.dark(self)

        self.editClassWidget.setStyleSheet(self.styleSheet())
        self.editClassWidget.setPalette(self.palette())

        self.app_icon = QIcon()
        self.app_icon.addFile(f'{self.path}/gui/icons/32x32.png', QSize(32, 32))
        self.setWindowIcon(self.app_icon)
        self.show()

    @pyqtSlot()
    def reload_classes(self):
        # TODO: Reload every class into the json file if it exists
        print('Reload Classes')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
