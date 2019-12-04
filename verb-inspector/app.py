# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:58:40 2019

@author: Mijael
"""
import sys
import json
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot, Qt,QSize
from PyQt5.QtGui import QPalette, QColor, QIcon

verbnet_json = 'verbnet.json'
propbank_json = 'propbank.json'

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Verb Inspector (Plot Points Inspector)'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.initPalette()
        
        self.app_icon = QIcon()
        self.app_icon.addFile('gui/icons/32x32.png', QSize(32,32))
        self.setWindowIcon(self.app_icon)
        
        self.reloadClassesButton = QPushButton('Reload vn classes', self)
        self.reloadClassesButton.setToolTip('Reload verbnet corpora classes into a json file')
        self.reloadClassesButton.move(100,70)
        self.reloadClassesButton.clicked.connect(self.reloadClasses)
        
        self.show()
    
    def initPalette(self):
        
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.setPalette(dark_palette)
        
    
    @pyqtSlot()
    def reloadClasses(self):
        # TODO: Reload every class into the json file if it exists
        print('Reload Classes')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    