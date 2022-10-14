from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class Main_Page(QDialog):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Main_Page, self).__init__()
		loadUi("UI/UI_Files/main_page.ui", self)  # load the UI of the page
		self.widget=widget  # the widget-stack that has all widgets --> so I can move to any other widget

		############### buttons section #############
		self.new_order_button.clicked.connect(self.new_order_function)  # click event to the new order button
		self.rooms_button.clicked.connect(self.rooms_function)  # click event to the rooms button
		self.search_order_button.clicked.connect(self.search_order_function)  # click event to the search order button
		self.setting_button.clicked.connect(self.settings_function)  # click event to the settins button

	def new_order_function(self):
		print("new-order")

	def rooms_function(self):
		print("rooms")

	def search_order_function(self):
		print("search-order")

	def settings_function(self):
		print("settings")
