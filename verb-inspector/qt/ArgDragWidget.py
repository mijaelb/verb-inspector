#!/usr/bin/env python

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

from qt.ArgEditorDialog import ArgEditorDialog

class ArgDragLabel(QtWidgets.QLabel):
    def __init__(self, arg, parent=None):
        super(ArgDragLabel, self).__init__(parent)
        self.label_text = ' '.join(arg.value)
        self.implicit = arg.implicit
        self.arg = arg
        self.dialog = None
        self.reset()

    def reset(self):
        metric = QtGui.QFontMetrics(self.font())
        size = metric.size(QtCore.Qt.TextSingleLine, self.label_text)

        image = QtGui.QImage(size.width() + 12, size.height() + 12,
                QtGui.QImage.Format_ARGB32_Premultiplied)
        image.fill(QtGui.qRgba(0, 0, 0, 0))

        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.ForceOutline)

        painter = QtGui.QPainter()
        painter.begin(image)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        if self.arg.implicit:
            painter.setBrush(QtCore.Qt.yellow)
        else:
            painter.setBrush(QtCore.Qt.white)

        painter.drawRoundedRect(
                QtCore.QRectF(0.5, 0.5, image.width()-1, image.height()-1),
                25, 25, QtCore.Qt.RelativeSize)

        painter.setFont(font)
        painter.setBrush(QtCore.Qt.black)
        painter.drawText(QtCore.QRect(QtCore.QPoint(6, 6), size), QtCore.Qt.AlignCenter, self.label_text)
        painter.end()
        self.setPixmap(QtGui.QPixmap.fromImage(image))

    def mousePressEvent(self, event):
        self.last = "Click"
        itemData = QtCore.QByteArray()
        dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
        dataStream << QtCore.QByteArray().append(self.label_text) << QtCore.QPoint(event.pos() - self.rect().topLeft()) << QtCore.QRect(self.rect())

        mimeData = QtCore.QMimeData()
        mimeData.setData('application/x-fridgemagnet', itemData)
        mimeData.setText(self.label_text)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.setPixmap(self.pixmap())

        self.hide()

        if drag.exec_(QtCore.Qt.MoveAction | QtCore.Qt.CopyAction, QtCore.Qt.CopyAction) == QtCore.Qt.MoveAction:
            self.close()
        else:
            self.show()

    def mouseReleaseEvent(self, event):
        if self.last == "Double Click":
            self.dialog = ArgEditorDialog(self.arg, self)
            self.dialog.show()


    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent):
        self.last = "Double Click"

class ArgDragWidget(QtWidgets.QWidget):
    def __init__(self, args, parent=None):
        super(ArgDragWidget, self).__init__(parent)
        self.args = args
        self.labels = list()
        self.resetWidget()
        new_palette = self.palette()
        new_palette.setColor(QtGui.QPalette.Window, QtCore.Qt.white)
        self.setPalette(new_palette)
        #self.setAutoFillBackground(True)
        self.setWindowTitle("Fridge Magnets")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-fridgemagnet'):
            if event.source() in self.children():
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        elif event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    dragMoveEvent = dragEnterEvent

    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-fridgemagnet'):
            mime = event.mimeData()
            itemData = mime.data('application/x-fridgemagnet')
            dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.ReadOnly)

            text = QtCore.QByteArray()
            offset = QtCore.QPoint()
            rect = QtCore.QRect()
            dataStream >> text >> offset >> rect
            text = str(text, encoding='latin1')

            point = event.pos()
            i = self.getItemIndex(text)
            if i != -1:
                for j, label in enumerate(self.labels):
                    if label.label_text != text:
                        if point.x() > label.x() and j > i:
                            self.args[i], self.args[j] = self.args[j], self.args[i]
                        elif point.x() < label.x() + label.width() and j < i:
                            self.args[i], self.args[j] = self.args[j], self.args[i]

            self.resetWidget()

            if event.source() in self.children():
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def getItemIndex(self, text):
        for i, arg in enumerate(self.args):
            if ' '.join(arg.value) == text:
                return i
        return -1

    def resetWidget(self):
        self.clearWidget()
        x, y = (5, 5)

        for arg in self.args:
            print(arg.pprint())
            label = ArgDragLabel(arg, self)
            label.move(x, y)
            label.show()
            x += label.width() + 2
            self.labels.append(label)

        self.setMinimumSize(x + 5, 35)
        self.setMaximumHeight(35)

    def clearWidget(self):
        for i, label in enumerate(self.labels):
            self.labels[i].deleteLater()
            self.labels[i] = None
        self.labels = []

# if __name__ == '__main__':
#
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = DragArgWidget()
#     window.show()
#     sys.exit(app.exec_())