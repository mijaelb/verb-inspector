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
from pathlib import Path
import pp
from qt.AppWidget import AppWidget
import qt.QtUtils as QtUtils
from qt.QtUtils import QT_VERSION

_FL_STYLESHEET = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qt/resources/frameless.qss')


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Plot Point Editor (Verb Inspector)'
        self.path = os.path.dirname(__file__)
        self.pp_container = pp.PlotPointContainer()
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 800
        self.app_icon = QtGui.QIcon()
        self.app_widget = AppWidget(self.pp_container, self)

        self.setCentralWidget(self.app_widget)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        with open(_FL_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())
        QtUtils.dark(self)

        self.app_icon.addFile(f'{self.path}/gui/icons/32x32.png', QtCore.QSize(32, 32))
        self.setWindowIcon(self.app_icon)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
