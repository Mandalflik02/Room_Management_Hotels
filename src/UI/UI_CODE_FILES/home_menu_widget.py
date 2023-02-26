from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import string

from models import *


class Home_Menu_Widget(QWidget):
	def __init__(self, widget):
		print(bool("0"))
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Home_Menu_Widget, self).__init__()
		loadUi("UI/UI_Files/home_menu_widget.ui", self)  # load the UI of the page
		self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget
		
		############### buttons section #############
		self.new_order_button.clicked.connect(self.new_order_function)  # click event to the new order button
		self.rooms_button.clicked.connect(self.rooms_function)  # click event to the rooms button
		
		self.search_order_button.clicked.connect(self.search_order_function)  # click event to the search order button
	
	#############################################
	
	def new_order_function(self):
		# start when click on the new-order button
		self.widget.setCurrentIndex(windows_indexes [ "new-order" ])
		print("new-order")
	
	def rooms_function(self):
		# start when click on the rooms button
		print("rooms")
	
	def search_order_function(self):
		# start when click on the search-order button
		
		text_to_search = self.search_order_line_edit.text()
		finds_orders = [ ]
		if text_to_search.isnumeric():
			finds_orders = search_order(order_id=text_to_search.zfill(8))
		elif text_to_search.isalpha():
			finds_orders = search_order(customer_name=text_to_search)
		else:
			return ""
		if len(finds_orders) == 1:
			self.widget.widget(windows_indexes [ "view-order" ]).set_order_to_display(finds_orders [ 0 ])
			self.widget.widget(windows_indexes [ "view-order" ]).display_order()

			self.widget.setCurrentIndex(windows_indexes [ "view-order" ])
		elif len(finds_orders) > 1:
			for i in finds_orders:
				print(i)
		else:
			print("can't find orders with the data that given")
