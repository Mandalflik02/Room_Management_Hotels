from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


from .title_bar import Title_Bar
from .home_menu_widget import Home_Menu_Widget



class Main_Page(QMainWindow):
	def __init__(self, windows_indexes):
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


		##################################################################
		self.widget_section.setCurrentIndex(windows_indexes["home-menu"])#start the program with the home menu widget

	def settings_function(self):
		# start when click on the settings button
		print("settings")



