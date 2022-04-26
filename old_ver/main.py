import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QDialog,
    QMessageBox,
    QDesktopWidget,
)
from PyQt5.uic import loadUi


class Rooms(QDialog):
    def __init__(self):
        super(Rooms, self).__init__()
        loadUi("UI\Rooms.ui", self)
        # self.to_the_center()
        self.loaddata()

    def loaddata(self):

        self.roomtable.setColumnWidth(0, 200)
        self.roomtable.setColumnWidth(1, 200)
        self.roomtable.setColumnWidth(2, 100)
        self.roomtable.setColumnWidth(3, 150)
        self.roomtable.setColumnWidth(4, 200)
        header_labels = [
            "Hosting status",
            "Cleaning status",
            "Faults",
            "Charges",
            "Type of vacation",
        ]
        self.roomtable.setHorizontalHeaderLabels(header_labels)

    # def to_the_center(self):
    # center the window
    # qr1 = widget.frameGeometry()
    # cp1 = QDesktopWidget().availableGeometry().center()
    # qr1.moveCenter(cp1)
    # widget.move(qr1.topLeft())


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
rooms = Rooms()
widget.addWidget(rooms)
widget.setFixedWidth(1300)
widget.setFixedHeight(600)
widget.show()
sys.exit(app.exec_())