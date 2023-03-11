from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from models import *


class View_Order_Widget(QDialog):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(View_Order_Widget, self).__init__()
		loadUi("UI/UI_Files/view_order_widget.ui", self)  # load the UI of the page
		self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget
		self.order_to_display = None
		
		self.check_in_status = False
		self.check_out_status = False
		
		self.check_in_btn.clicked.connect(self.check_in_order)
		self.check_out_btn.clicked.connect(self.check_out_order)
		self.delete_btn.clicked.connect(self.delete_order)
		self.update_btn.clicked.connect(self.update_order)
		self.home_btn.clicked.connect(self.home)
	
	def check_in_order(self):
		msg_label = "Check-in customer??" if not self.check_in_status else "Cancel check-in customer??"
		q = MSG_Dialog(msg_label, "Yes", "No")
		q.exec_()
		if q.status == "No":
			return
		self.check_in_status = not self.check_in_status
		try:
			if self.check_in_status:
				error = check_in(self.order_to_display)
				if error [ 0 ]:
					self.change_btn_color(self.check_in_btn, self.check_in_status)
				else:
					self.check_in_status = not self.check_in_status
					MSG_Popup(error [ 1 ]).exec_()
			# print(error[1])
			else:
				if not self.order_to_display.get_check_out_status():
					self.order_to_display.cancel_check_in_customers()
					search_room_by_number(self.order_to_display.get_room_number()).set_room_status(False)
					self.change_btn_color(self.check_in_btn, self.check_in_status)
				else:
					self.check_in_status = not self.check_in_status
					MSG_Popup("The customer is already check out!!").exec_()
		# print("The customer is already check out!!")
		
		except Exception as e:
			print("check-in in widget", e)
	
	# finally:
	# 	print(self.order_to_display)
	def check_out_order(self):
		msg_label = "Check-out customer??" if not self.check_out_status else "Cancel check-out customer??"
		q = MSG_Dialog(msg_label, "Yes", "No")
		q.exec_()
		if q.status == "No":
			return
		self.check_out_status = not self.check_out_status
		try:
			if self.check_out_status:
				error = check_out(self.order_to_display)
				if error [ 0 ]:
					self.change_btn_color(self.check_out_btn, self.check_out_status)
				else:
					self.check_out_status = not self.check_out_status
					MSG_Popup(error [ 1 ]).exec_()
			# print(error[1])
			else:
				self.order_to_display.cancel_check_out_customers()
				search_room_by_number(self.order_to_display.get_room_number()).set_room_status(True)
				self.change_btn_color(self.check_out_btn, self.check_out_status)
		
		except Exception as e:
			print("check-out in widget", e)
	
	# finally:
	# 	print(self.order_to_display)
	
	def change_btn_color(self, btn, status):
		style = """
					QPushButton:hover {
						background-color: rgb(10, 123, 204);
					}
					QPushButton{
						font: 18pt "Calibri";
						border-radius:15px;
						border-radius:10px;
						color: rgb(255, 255, 255);
						border:2px solid  rgb(255, 255, 255);
				"""  # the basic style for the button
		if status:
			style += """	background: rgb(10, 123, 204);	"""  # add background color when the status is true
		style += """	}	"""  # close style
		btn.setStyleSheet(style)  # set the style sheet for the button
	
	def delete_order(self):
		pass
	
	def update_order(self):
		pass
	
	def home(self):
		self.clear_ui()
		self.widget.setCurrentIndex(windows_indexes [ "home-menu" ])  # return to home menu
	
	def clear_ui(self):
		self.order_id_label.setText("View order: ")
		self.created_by_label.setText("Order created by:")
		self.creation_date_label.setText("Order creation date: ")
		self.customer_name_label.setText("Customer name: ")
		self.adults_label.setValue(0)
		self.kids_label.setValue(0)
		self.arrivel_label.setText("")
		self.leaving_label.setText("")
		order_widget_labels = [ self.electric_car_label,
		                        self.pet_label,
		                        self.breakfast_label,
		                        self.lunch_label,
		                        self.dinner_label ]
		for label in order_widget_labels:
			label.setPixmap(QPixmap('UI/ICONS/unchecked.png'))
	
	def display_order(self):
		
		self.order_id_label.setText(f"View order: {self.order_to_display.get_order_id()}")
		self.created_by_label.setText(f"Order created by: {self.order_to_display.get_crete_by()}")
		self.creation_date_label.setText(f"Order creation date: {self.order_to_display.get_creation_time()}")
		self.customer_name_label.setText(f"Customer name: {self.order_to_display.get_customer_name()}")
		self.adults_label.setValue(self.order_to_display.get_guests_num())
		self.kids_label.setValue(self.order_to_display.get_guests_num())
		self.arrivel_label.setText(f"{self.order_to_display.get_arrival_date()}")
		self.leaving_label.setText(f"{self.order_to_display.get_leaving_date()}")
		order_vars_and_widget_labels = [ (self.order_to_display.get_electric_car(), self.electric_car_label),
		                                 (self.order_to_display.get_pet(), self.pet_label),
		                                 (self.order_to_display.get_breakfast(), self.breakfast_label),
		                                 (self.order_to_display.get_lunch(), self.lunch_label),
		                                 (self.order_to_display.get_dinner(), self.dinner_label) ]
		for order_stat in order_vars_and_widget_labels:
			if order_stat [ 0 ] == True:
				order_stat [ 1 ].setPixmap(QPixmap('UI/ICONS/checked.png'))
			else:
				order_stat [ 1 ].setPixmap(QPixmap('UI/ICONS/unchecked.png'))


	# results = [t [ 1 ].setPixmap(QPixmap('UI/ICONS/checked.png')) if  t [ 0 ] == True else t [ 1 ].setPixmap(QPixmap('UI/ICONS/unchecked.png')) for t in order_vars_and_widget_labels]

	def set_order_to_display(self, order_to_display=None | Order):
		self.order_to_display = order_to_display
		print(self.order_to_display)
