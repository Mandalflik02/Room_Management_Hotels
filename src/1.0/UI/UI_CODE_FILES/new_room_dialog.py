from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from models import *


class New_Room_Dialog(QDialog):
	def __init__(self):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(New_Room_Dialog, self).__init__()
		loadUi("UI/UI_Files/new_room_dialog.ui", self)  # load the UI of the page

		
		self.add_room_btn.clicked.connect(self.add_room_btn_click)
		self.cencel_btn.clicked.connect(self.cencel_btn_click)
		
		self.capacity=0
		
		
	def add_room_btn_click(self):
		capacity = int(self.capacity_input.text())
		if capacity < 2 or capacity > 12:
			MSG_Popup("Room capacity must be between 2 and 12").exec_()
			return
		self.capacity = capacity
		self.close()
	def cencel_btn_click(self):
		self.close()

