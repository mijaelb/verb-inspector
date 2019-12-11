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


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Plot Point Editor (Verb Inspector)'
        self.pp_container = pp.PlotPointContainer()
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.path = os.path.dirname(__file__)
        self.classes_list = self.__create_vn_classes_list()

        self.args_class_table = QtWidgets.QTableWidget()
        self.edit_class_layout = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QHBoxLayout()

        self.edit_class_layout.addWidget(self.args_class_table)
        self.layout.addWidget(self.classes_list)
        self.layout.addLayout(self.edit_class_layout)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(600, 400)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.init_palette()
        self.setLayout(self.layout)

        self.app_icon = QIcon()
        self.app_icon.addFile(f'{self.path}/gui/icons/32x32.png', QSize(32, 32))
        self.setWindowIcon(self.app_icon)


        self.reloadClassesButton = QtWidgets.QPushButton('Reload vn classes')
        self.reloadClassesButton.setToolTip('Reload verbnet corpora classes into a json file')
        self.reloadClassesButton.move(100, 70)
        self.reloadClassesButton.clicked.connect(self.reload_classes)

        self.layout.addWidget(self.reloadClassesButton)
        self.show()

    def init_palette(self):
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

    def __create_vn_classes_list(self):
        vn_classes_list = QtWidgets.QListWidget()
        vn_classes = self.pp_container.verbnet.get_classes()
        for cls_id, cls in vn_classes.items():
            vn_class_item = QtWidgets.QListWidgetItem(cls_id)
            vn_class_item.setData(Qt.UserRole, cls)
            vn_classes_list.addItem(vn_class_item)

        vn_classes_list.currentItemChanged.connect(self.change_vn_class)
        return vn_classes_list

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def change_vn_class(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        vn_class = current.data(Qt.UserRole)

        self.clear_table(self.args_class_table)
        self.args_class_table.insertColumn(self.args_class_table.columnCount())
        for group in vn_class.args:
            if isinstance(group, list):
                text = ' '.join([arg for arg in group])
            else:
                text = group

            self.args_class_table.insertRow(self.args_class_table.rowCount())
            print(text)
            self.args_class_table.setItem(self.args_class_table.rowCount()-1, self.args_class_table.columnCount()-1, QtWidgets.QTableWidgetItem(text))

        print(vn_class.pprint())

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):

            widget = layout.takeAt(i).widget()
            if widget:
                widget.setParent(None)

    def clear_table(self, table):
        table.setRowCount(0)
        table.setColumnCount(0)

    @pyqtSlot()
    def reload_classes(self):
        # TODO: Reload every class into the json file if it exists
        print('Reload Classes')


class DragArgButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(DragArgButton, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
            for url in e.mimeData().urls():
                self.openFile(url.toLocalFile())
        else:
            e.ignore()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
