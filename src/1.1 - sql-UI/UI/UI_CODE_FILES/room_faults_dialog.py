
from PyQt5.QtWidgets import QWidget, QFrame, QLabel,QDialog
from PyQt5.uic import loadUi

from models import *


class Faults_Dialog(QDialog):
	def __init__(self, room_number,room_faults_list):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Faults_Dialog, self).__init__()
		loadUi("UI/UI_Files/room_faults_dialog.ui", self)  # load the UI of the page



		self.room_number_label.setText(str(room_number))

		for f in room_faults_list:
			self.faults_widget.addWidget(self.create_fault_frame(f[0]))




	def create_fault_frame(self,fault):
		faults_frame = QFrame(self)
		faults_frame.setObjectName(u"faults_frame")
		faults_frame.setFixedHeight(40)
		faults_frame.setFixedWidth(350)
		faults_frame.setGeometry(10, 10, 350, 40)
		faults_frame.setStyleSheet(u"background-color: rgb(141, 193, 231)")

		start_date_label = QLabel(faults_frame)
		start_date_label.setObjectName(u"fault_label")
		start_date_label.setGeometry(10, 10, 130, 20)
		start_date_label.setText(fault)
		start_date_label.setStyleSheet(u"font: 19pt \"Calibri\";")



		return faults_frame