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
from qt.ArgDragWidget import ArgDragWidget
import qt.QtUtils as QtUtils

CLASS_LIST_WIDTH = 225

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Plot Point Editor (Verb Inspector)'
        self.path = os.path.dirname(__file__)
        self.pp_container = pp.PlotPointContainer()
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 800
        self.classes_list = self.__create_classes_list()
        # self.args_class_table = QtWidgets.QTableWidget()

        self.args_class_layout = QtWidgets.QHBoxLayout()
        self.edit_class_layout = QtWidgets.QVBoxLayout()

        self.class_select_layout = QtWidgets.QVBoxLayout()
        self.layout = QtWidgets.QHBoxLayout()


        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setLayout(self.layout)
        self.class_select_layout.addWidget(self.classes_list)
        self.edit_class_layout.addLayout(self.args_class_layout)
        self.layout.addLayout(self.class_select_layout)
        self.layout.addLayout(self.edit_class_layout)
        self.classes_list.setFixedWidth(CLASS_LIST_WIDTH)
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        self.setPalette(QtUtils.DarkPalette())
        self.app_icon = QIcon()
        self.app_icon.addFile(f'{self.path}/gui/icons/32x32.png', QSize(32, 32))
        self.setWindowIcon(self.app_icon)
        self.show()

    def __create_classes_list(self):
        vn_classes_list = QtWidgets.QListWidget()
        vn_classes = self.pp_container.verbnet_simplified.get_classes()
        for cls_id, cls in vn_classes.items():
            vn_class_item = QtWidgets.QListWidgetItem(cls_id)
            vn_class_item.setData(Qt.UserRole, cls)
            vn_classes_list.addItem(vn_class_item)

        vn_classes_list.currentItemChanged.connect(self.change_vn_class)
        return vn_classes_list

    def __create_class_args(self, vnclass):
        self.clear_layout(self.args_class_layout)
        widget = ArgDragWidget(vnclass.args, self)
        self.args_class_layout.addWidget(widget)
        return widget

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def change_vn_class(self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem):
        vnclass = current.data(Qt.UserRole)
        self.__create_class_args(vnclass)
        # self.clear_table(self.args_class_table)
        # self.args_class_table.insertRow(self.args_class_table.rowCount())
        # for group in vnclass.args:
        #     if isinstance(group, list):
        #         text = ' '.join([arg for arg in group])
        #     else:
        #         text = group
        #
        #     self.args_class_table.insertColumn(self.args_class_table.columnCount())
        #     self.args_class_table.setItem(self.args_class_table.rowCount()-1, self.args_class_table.columnCount()-1, QtWidgets.QTableWidgetItem(text))
        #
        # print(vn_class.pprint())

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



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
