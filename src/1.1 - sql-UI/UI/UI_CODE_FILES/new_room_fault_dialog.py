from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from models import *


class New_Fault_Dialog(QDialog):
	def __init__(self):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(New_Fault_Dialog, self).__init__()
		loadUi("UI/UI_Files/new_room_fault_dialog.ui", self)  # load the UI of the page

		
		self.add_fault_btn.clicked.connect(self.add_fault)
		self.cencel_btn.clicked.connect(self.cencel_btn_click)
		
		self.room_number=0
		self.fault=""
		
		
	def add_fault(self):
		self.room_number = int(self.room_number_input.text())
		self.fault = self.fault_text_edit.toPlainText()
		self.close()
	def cencel_btn_click(self):
		self.close()

