import random, sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from models import *
from UI.UI_CODE_FILES import Main_Page


# self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def create_app():
	app = QApplication(sys.argv)  # create the app
	main_page = Main_Page()  # create main page
	
	main_page.show()
	app.exec_()


def main():
	
	arrivel="01/01/2025"
	leaving="09/01/2025"
	for r in range(15):
		room = Room(r + 1, random.choice(
			[ 2, 4, 6, 8 ]))  # create room with random capacity and room number between 1 and 10
		ROOMS.append(room)  # add the room to the rooms list
	print(add_new_order(customer_name="naor",guests=2,arrival_date=arrivel,leaving_date=leaving,meal_options="000",electric_car=False,pet=True))
	print(add_new_order(customer_name="naor",guests=5,arrival_date=arrivel,leaving_date=leaving,meal_options="000",electric_car=False,pet=True))
	print(add_new_order(customer_name="naor",guests=3,arrival_date=arrivel,leaving_date=leaving,meal_options="000",electric_car=False,pet=True))
	
	create_app()


if __name__ == '__main__':
	main()
