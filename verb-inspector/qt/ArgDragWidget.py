#!/usr/bin/env python

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

from qt.ArgEditorDialog import ArgEditorDialog


class ArgDragLabel(QtWidgets.QLabel):
    def __init__(self, arg, parent=None, select=False):
        super(ArgDragLabel, self).__init__(parent)
        self.arg = arg
        self.dialog = None
        self.isSelected = select
        self.label_text = f'{self.arg.slot}: {self.arg.value}'
        self.reset()

    def reset(self):
        metric = QtGui.QFontMetrics(self.font())

        if self.isSelected:
            size = metric.size(QtCore.Qt.TextSelectableByMouse, self.label_text)
            offset = 16
        else:
            size = metric.size(QtCore.Qt.TextSingleLine, self.label_text)
            offset = 12

        image = QtGui.QImage(size.width() + offset, size.height() + offset, QtGui.QImage.Format_ARGB32_Premultiplied)
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

        painter.drawRoundedRect(QtCore.QRectF(0.5, 0.5, image.width() - 1, image.height() - 1), 25, 25,
                                QtCore.Qt.RelativeSize)

        painter.setFont(font)

        painter.setBrush(QtCore.Qt.black)

        painter.drawText(QtCore.QRect(QtCore.QPoint(offset / 2, offset / 2), size), QtCore.Qt.AlignCenter,
                         self.label_text)
        painter.end()
        self.setPixmap(QtGui.QPixmap.fromImage(image))

    def mousePressEvent(self, event):
        self.last = "Click"
        itemData = QtCore.QByteArray()
        dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
        dataStream << QtCore.QByteArray().append(str(dict(self.arg))) << QtCore.QPoint(
            event.pos() - self.rect().topLeft()) << QtCore.QRect(self.rect())

        mimeData = QtCore.QMimeData()
        mimeData.setData('application/x-fridgemagnet', itemData)
        mimeData.setText(self.arg.value)

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.setPixmap(self.pixmap())

        self.hide()

        if drag.exec_(QtCore.Qt.MoveAction | QtCore.Qt.CopyAction, QtCore.Qt.CopyAction) == QtCore.Qt.MoveAction:
            self.close()
        else:
            self.show()

        self.parent().setSelection(self)

    def mouseReleaseEvent(self, event):
        if self.last == "Double Click":
            self.dialog = ArgEditorDialog(self.arg, self)
            self.dialog.show()


class ArgDragWidget(QtWidgets.QWidget):
    selected = QtCore.pyqtSignal(ArgDragLabel)

    def __init__(self, args, parent=None, selected=None):
        super(ArgDragWidget, self).__init__(parent)
        self.args = args
        self.labels = list()
        new_palette = self.palette()
        new_palette.setColor(QtGui.QPalette.Window, QtCore.Qt.white)
        self.setPalette(new_palette)
        self.setWindowTitle("Fridge Magnets")
        self.setAcceptDrops(True)
        self.currentSelection = selected
        self.resetWidget()

    def setSelection(self, selection):
        self.selected.emit(selection)
        self.currentSelection = selection

    def selection(self):
        return self.currentSelection

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

            arg = QtCore.QByteArray()
            offset = QtCore.QPoint()
            rect = QtCore.QRect()
            dataStream >> arg >> offset >> rect

            point = event.pos()
            i = self.getItemIndex(arg)
            j = self.getDropIndex(point)
            print(f'{i} {j}')

            if i != j:
                stor = self.args[i]
                del self.args[i]
                if j == len(self.args):
                    self.args.append(stor)
                else:
                    self.args.insert(j, stor)

                self.moveItems(i, j)

                i = self.getItemIndex(arg)
                self.args[i].slot = self.args[i - 1].slot + 1 if i > 0 else 0

            self.resetWidget()

            if event.source() in self.children():
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def moveItems(self, src, dest):
        n = 1 if dest > src else -1
        if dest > src:
            ran = list(range(src, dest))
        else:
            ran = list(reversed(range(dest + 1, src + 1)))

        if dest != src:
            print(ran)
            for i in ran:
                print(i)
                self.args[i].slot = self.args[i].slot - n

    def getItemIndex(self, arg_str):
        for i, a in enumerate(self.args):
            if str(dict(a)) == arg_str:
                return i
        return -1

    def getDropIndex(self, point):
        if self.labels[0].x() + self.labels[0].width() > point.x():
            return 0

        for j, label in enumerate(self.labels):
            if j + 1 < len(self.labels):
                if self.labels[j + 1].x() + self.labels[j + 1].width() > point.x() >= self.labels[j].x():
                    return j + 1
            else:
                return j + 1

    def resetWidget(self):
        self.clearWidget()
        x, y = (0, 2)

        slot = -1
        for arg in self.args:
            select = True if self.currentSelection and self.currentSelection.arg == arg else False
            label = ArgDragLabel(arg, self, select)
            if slot != arg.slot:
                x += 4
                label.move(x, y)
            else:
                x -= 1
                label.move(x, y)
            label.show()
            x += label.width()
            self.labels.append(label)
            slot = arg.slot

        self.setMinimumSize(x, 29)
        self.setMaximumHeight(29)

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