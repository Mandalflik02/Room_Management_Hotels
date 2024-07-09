from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget,QFrame
from PyQt5.uic import loadUi

from models import *

class Title_Bar(QFrame):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Title_Bar, self).__init__()
		loadUi("UI/UI_Files/title_bar.ui", self)  # load the UI of the page
		self.widget=widget  # the widget-stack that has all widgets --> so I can move to any other widget

		self.close_button.clicked.connect(self.close_app)
		self.minimize_button.clicked.connect(self.minimize_app)



	def close_app(self):
		DB_CON.commit()
		DB_CURSER.close()
		DB_CON.close()
		self.widget.close()
	def minimize_app(self):
		self.widget.showMinimized()