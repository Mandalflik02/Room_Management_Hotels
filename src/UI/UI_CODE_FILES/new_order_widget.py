from datetime import *

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from models import *
from models.range_of_dates import Dates_Range


class New_Order_Widget(QWidget):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(New_Order_Widget, self).__init__()
		loadUi("UI/UI_Files/new_order_widget.ui", self)  # load the UI of the page
		self.widget=widget  # the widget-stack that has all widgets --> so I can move to any other widget

		self.create_btn.clicked.connect(self.create_order)  # click event to the create order button

		###############################self values##############################
		self.electric_car_status=False  # tell if the customer has electric car
		self.pet_status=False  # tell if the customer has a pet
		self.breakfast_status=False # tell if the customer want breakfast
		self.lunch_status=False# tell if the customer want lunch
		self.dinner_status=False# tell if the customer want dinner
		#######################################################################

		##########################clicked events ##############################
		self.check_electric_car_btn.clicked.connect(self.electric_car)
		self.check_pet_btn.clicked.connect(self.pet)
		self.breakfast_btn.clicked.connect(self.breakfast)
		self.lunch_btn.clicked.connect(self.lunch)
		self.dinner_btn.clicked.connect(self.dinner)
		# self.arrivel_date.editingFinished.connect(self.get_arrivel_date)
		######################################################################

	def arrange_data(self):
		current_time=datetime.now().strftime("%H:%M:%S , %d/%m/%Y")
		customer_name =self.customer_name_input.text()
		guests=int(self.adults_input.text()) + int(self.kids_input.text())
		meal_options=[self.breakfast_status , self.lunch_status , self.dinner_status]
		electric_car=self.electric_car_status
		pet=self.pet_status
		arrivel=str(self.arrivel_date.date().toPyDate().strftime("%d/%m/%Y"))
		leaving=str(self.leaving_date.date().toPyDate().strftime("%d/%m/%Y"))
		print(f"{current_time}\n"
		      f"{customer_name}\n"
		      f"{guests}\n"
		      f"{meal_options}\n"
		      f"{electric_car}\n"
		      f"{pet}\n"
		      f"{arrivel}\n"
		      f"{leaving}\n")
		# add_new_order()

	def create_order(self):
		print("-------------start create-----------")
		self.arrange_data()
		print("-------------end create------------")

	def breakfast(self):
		self.breakfast_status=not self.breakfast_status #change status for the select
		style="""
			QPushButton:hover {
				background-color: rgb(48, 120, 200);
			}
			QPushButton{
				border-radius:15px;
				font: 25px "Calibri";
				border:1px solid rgb(255, 255, 255);
		"""
		if self.breakfast_status:
			style+= """background-color: rgb(48, 120, 200);"""# add background color when the status is true
		style+= """
		}				
		"""
		self.breakfast_btn.setStyleSheet(style)  # set the style sheet for the button

	def lunch(self):
		self.lunch_status=not self.lunch_status #change status for the select
		style="""
			QPushButton:hover {
				background-color: rgb(48, 120, 200);
			}
			QPushButton{
				border-radius:15px;
				font: 25px "Calibri";
				border:1px solid rgb(255, 255, 255);
		"""
		if self.lunch_status:
			style+= """background-color: rgb(48, 120, 200);"""# add background color when the status is true
		style+= """
		}				
		"""
		self.lunch_btn.setStyleSheet(style)  # set the style sheet for the button

	def dinner(self):
		self.dinner_status=not self.dinner_status #change status for the select
		style="""
			QPushButton:hover {
				background-color: rgb(48, 120, 200);
			}
			QPushButton{
				border-radius:15px;
				font: 25px "Calibri";
				border:1px solid rgb(255, 255, 255);
		"""
		if self.dinner_status:
			style+= """background-color: rgb(48, 120, 200);"""# add background color when the status is true
		style+= """
		}				
		"""
		self.dinner_btn.setStyleSheet(style)  # set the style sheet for the button


	def electric_car(self):
		self.electric_car_status=not self.electric_car_status#change status for the select
		style="""
			QPushButton:hover {
				background-color: rgb(10, 123, 204);
			}
			QPushButton{
				border-radius:15px;
				border-radius:10px;
				color: rgb(255, 255, 255);
				border:2px solid  rgb(255, 255, 255);	
		"""
		if self.electric_car_status:
			style+="""	background: rgb(10, 123, 204);	"""# add background color when the status is true
		style+="""	}	"""
		self.check_electric_car_btn.setStyleSheet(style)  # set the style sheet for the button

	def pet(self):
		self.pet_status=not self.pet_status#change status for the select
		style="""
					QPushButton:hover {
						background-color: rgb(10, 123, 204);
					}
					QPushButton{
						border-radius:15px;
						border-radius:10px;
						color: rgb(255, 255, 255);
						border:2px solid  rgb(255, 255, 255);	
				"""
		if self.pet_status:
			style+="""	background: rgb(10, 123, 204);	"""# add background color when the status is true
		style+="""	}	"""
		self.check_pet_btn.setStyleSheet(style)  # set the style sheet for the button
