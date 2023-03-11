from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class List_Dialog(QDialog):
	def __init__(self,label_text,btn1_text,btn2_text):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(List_Dialog, self).__init__()
		loadUi("models/dialogs/dialog_list/list_dialog.ui", self)  # load the UI of the page
		
		self.msg_label.setText(label_text)
		self.msg_btn_1.setText(btn1_text)
		self.msg_btn_2.setText(btn2_text)
		self.setWindowTitle(label_text)
		
		self.msg_btn_1.clicked.connect(self.btn1_click)
		self.msg_btn_2.clicked.connect(self.btn2_click)
		
		self.status=""
		
		
	def btn1_click(self):
		self.close()
		self.status =self.msg_btn_1.text()
	def btn2_click(self):
		self.close()
		self.status= self.msg_btn_2.text()
	
	
	
	