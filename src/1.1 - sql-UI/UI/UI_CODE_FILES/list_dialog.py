from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from models import *


class List_Dialog(QDialog):
	def __init__(self, widget, orders_list, customer_name):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(List_Dialog, self).__init__()
		loadUi("UI/UI_Files/list_dialog.ui", self)  # load the UI of the page
		self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget
		
		self.list_titel.setText(f"{customer_name.strip()}'s orders")
		
		self.frame1 = [ self.order_frame_1, self.order_dates_1, self.order_guests_1,
		                self.order_view_btn_1 ]  # componnets of frame 1
		self.frame2 = [ self.order_frame_2, self.order_dates_2, self.order_guests_2,
		                self.order_view_btn_2 ]  # componnets of frame 2
		self.frame3 = [ self.order_frame_3, self.order_dates_3, self.order_guests_3,
		                self.order_view_btn_3 ]  # componnets of frame 3
		
		self.frame1 [ 0 ].hide()  # hide frame 1 in the start
		self.frame2 [ 0 ].hide()  # hide frame 2 in the start
		self.frame3 [ 0 ].hide()  # hide frame 3 in the start
		
		self.frames = [ self.frame1, self.frame2, self.frame3 ]  # all frames in one place
		
		self.orders = orders_list  # save orders list in object variable
		orders_count = len(orders_list)
		print(f"order count :{orders_count}")
		self.show_frames(orders_count)  # show the relevant frames
		if orders_count > 3:  # if there is more than 3 orders
			print("Too mach orders")
			return
	
	def show_frames(self, count):
		self.setFixedHeight(120 + (count * 100))  # setup the size of the dialog base on the orders number
		for i in range(count):
			self.frames [ i ] [ 0 ].show()  # shows the amount of frames according to the amount of orders
		
		self.setup_order_in_list(count)  # display data in the frames
	
	def setup_order_in_list(self, count):
		for i in range(count):
			self.frames [ i ] [ 1 ].setText(self.orders [ i ].get_date_range())
			self.frames [ i ] [ 2 ].setText(str(self.orders [ i ].get_guests_num()) + " Guests")
		try:
			self.frames [ 0 ] [ 3 ].clicked.connect(lambda: self.go_to_order(self.orders [ 0 ]))
			self.frames [ 1 ] [ 3 ].clicked.connect(lambda: self.go_to_order(self.orders [ 1 ]))
			self.frames [ 2 ] [ 3 ].clicked.connect(lambda: self.go_to_order(self.orders [ 2 ]))
		except Exception as e:
			print(e)
	
	def go_to_order(self, order: Order=None):
		print(order)
		self.widget.widget(windows_indexes [ "view-order" ]).set_order_to_display(order)
		self.widget.widget(windows_indexes [ "view-order" ]).display_order()
		self.widget.widget(windows_indexes [ "home-menu" ]).search_order_line_edit.setText("")
		self.widget.setCurrentIndex(windows_indexes [ "view-order" ])
		self.close()
