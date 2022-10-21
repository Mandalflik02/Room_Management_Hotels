from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from models import *

class New_Order_Widget(QWidget):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(New_Order_Widget, self).__init__()
		loadUi("UI/UI_Files/new_order_widget.ui", self)  # load the UI of the page
		self.widget=widget  # the widget-stack that has all widgets --> so I can move to any other widget