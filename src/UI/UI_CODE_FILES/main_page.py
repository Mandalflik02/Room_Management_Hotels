import datetime
import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from datetime import datetime
from threading import Thread

from models import *
from .title_bar import Title_Bar
from .home_menu_widget import Home_Menu_Widget
from .new_order_widget import New_Order_Widget



class Main_Page(QMainWindow):
	def __init__(self):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Main_Page, self).__init__()
		loadUi("UI/UI_Files/main_page.ui", self)  # load the UI of the page
		self.setWindowFlag(Qt.FramelessWindowHint)# this will hide the title bar

		######################## add title widget ########################
		title_Bar=Title_Bar(self)
		self.top_widget.addWidget(title_Bar)
		##################################################################


		######################## buttons section #########################
		self.setting_button.clicked.connect(self.settings_function)  # click event to the settings button
		##################################################################


		####################### add widgets section ######################
		main_menu=Home_Menu_Widget(self.widget_section)#create a home menu widget
		self.widget_section.insertWidget(windows_indexes["home-menu"], main_menu)#add home menu widget to the stack
		#--------------------------------------------------------------------------------------------------------------#
		new_order=New_Order_Widget(self.widget_section)  # create a new order widget
		self.widget_section.insertWidget(windows_indexes["new-order"], new_order)  # add new order widget to the stack
		# --------------------------------------------------------------------------------------------------------------#


		##################################################################
		self.widget_section.setCurrentIndex(windows_indexes["new-order"])#start the program with the home menu widget
		self.widget_section.setFixedWidth(1300)# set width
		self.widget_section.setFixedHeight(780)#set height

		# self.time_date_thread=Thread(target=self.set_time_for_display)
		# self.time_date_thread.start()


	def settings_function(self):
		# start when click on the settings button
		print("settings")


	def set_time_for_display(self):
		try:
			while True:
				current_time=datetime.now().strftime(" %H:%M:%S\n%d/%m/%Y")
				self.time_label.setText(current_time)
				if stop_time_thread:
					break
		except:
			return



