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
		
		self.home_btn.clicked.connect(self.home)
		
	def home(self):
		self.clear_ui
		self.widget.setCurrentIndex(windows_indexes [ "home-menu" ]) #return to home menu
	
	def clear_ui(self):
		pass
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
		for t in order_vars_and_widget_labels:
			if t [ 0 ] == True:
				t [ 1 ].setPixmap(QPixmap('UI/ICONS/checked.png'))
			else:
				t [ 1 ].setPixmap(QPixmap('UI/ICONS/unchecked.png'))
		# results = [t [ 1 ].setPixmap(QPixmap('UI/ICONS/checked.png')) if  t [ 0 ] == True else t [ 1 ].setPixmap(QPixmap('UI/ICONS/unchecked.png')) for t in order_vars_and_widget_labels]
	
	def set_order_to_display(self, order_to_display):
		self.order_to_display = order_to_display
		print(self.order_to_display)
