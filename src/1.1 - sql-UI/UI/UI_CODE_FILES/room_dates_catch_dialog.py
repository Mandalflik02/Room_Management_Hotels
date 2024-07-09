from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFrame, QLabel,QDialog
from PyQt5.uic import loadUi

from models import *


class Dates_Catch_Dialog(QDialog):
	def __init__(self, room_number,room_dates_catch_list):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Dates_Catch_Dialog, self).__init__()
		loadUi("UI/UI_Files/room_dates_catch_dialog.ui", self)  # load the UI of the page	



		self.room_number_label.setText(str(room_number))

		for d in room_dates_catch_list:
			self.dates_catch_widget.addWidget(self.create_date_frame(d))




	def create_date_frame(self,date):
		dates_frame = QFrame(self)
		dates_frame.setObjectName(u"dates_frame")
		dates_frame.setFixedHeight(40)
		dates_frame.setFixedWidth(350)
		dates_frame.setGeometry(10, 10, 350, 40)
		dates_frame.setStyleSheet(u"background-color: rgb(141, 193, 231)")

		start_date_label = QLabel(dates_frame)
		start_date_label.setObjectName(u"start_date_label")
		start_date_label.setGeometry(10, 10, 130, 20)
		start_date_label.setText(date[0])
		start_date_label.setStyleSheet(u"font: 19pt \"Calibri\";")

		end_date_label = QLabel(dates_frame)
		end_date_label.setObjectName(u"end_date_label")
		end_date_label.setGeometry(190, 10, 130, 20)
		end_date_label.setText(date[1])
		end_date_label.setStyleSheet(u"font: 19pt \"Calibri\";")

		to_label = QLabel(dates_frame)
		to_label.setObjectName(u"to_label")
		to_label.setGeometry(150, 10, 30, 20)
		to_label.setText("To")
		to_label.setStyleSheet(u"font: 18pt \"Calibri\";")
		to_label.setAlignment(Qt.AlignCenter)

		return dates_frame