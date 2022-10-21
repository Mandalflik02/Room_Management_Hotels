from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget,QFrame
from PyQt5.uic import loadUi


class Home_Menu_Widget(QWidget):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Home_Menu_Widget, self).__init__()
		loadUi("UI/UI_Files/home_menu_widget.ui", self)  # load the UI of the page
		self.widget=widget  # the widget-stack that has all widgets --> so I can move to any other widget

		############### buttons section #############
		self.new_order_button.clicked.connect(self.new_order_function)  # click event to the new order button
		self.rooms_button.clicked.connect(self.rooms_function)  # click event to the rooms button
		self.search_order_button.clicked.connect(self.search_order_function)  # click event to the search order button
		#############################################



	def new_order_function(self):
		#start when click on the new-order button
		print("new-order")

	def rooms_function(self):
		# start when click on the rooms button
		print("rooms")

	def search_order_function(self):
		# start when click on the search-order button
		print("search-order",self.search_order_line_edit.text())

