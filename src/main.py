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


def menu():
	choose = -1
	while choose != 10:
		print("\n-------------------Menu-------------------\n"
		      "1) add order\n"
		      "2) view order\n"
		      "3) update order\n"
		      "4) orders list\n"
		      "5) rooms status\n"
		      "6) check-in\n"
		      "7) check-out\n"
		      "9) LOGS\n"
		      "10) EXIT\n")
		try:
			choose = int(input("Choose option: "))
			match choose:
				case 1:
					add_new_order()
				case 2:
					view_order()
				case 3:
					update_order()
				case 4:
					show_orders()
				case 5:
					show_rooms_status()
				case 6:
					check_in()
				case 7:
					check_out()
				case 9:
					show_logs_by_date()
				case 10:
					continue
				case _:
					print("[ ERROR ] - not in the range of the options")
		except ValueError:
			print("-------------------Enter a number-------------------")
			continue
		except KeyboardInterrupt:
			break


def main():
	for r in range(1):
		room = Room(r + 1, random.choice(
			[ 2, 4, 6, 8 ]))  # create room with random capacity and room number between 1 and 10
		ROOMS.append(room)  # add the room to the rooms list
	create_app()


if __name__ == '__main__':
	main()
