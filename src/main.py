import random,sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from models import *
from UI.UI_CODE_FILES import Main_Page
# self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")



def create_app():
	app=QApplication(sys.argv)  # create the app
	# widget=QtWidgets.QStackedWidget()  # create list of all views
	# widget.setWindowFlag(Qt.FramelessWindowHint)# this will hide the title bar


	main_page=Main_Page(windows_indexes)  # create main page
	# widget.insertWidget(windows_indexes["main-page"], main_page)# set the main page as widget in the widgets stack



	# widget.setCurrentIndex(0)
	# widget.setFixedWidth(1300)
	# widget.setFixedHeight(780)
	main_page.show()
	app.exec_()

def menu():
	choose=-1
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
			choose=int(input("Choose option: "))
		except ValueError:
			print("-------------------Enter a number-------------------")
			continue
		except KeyboardInterrupt:
			break
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


def main():
	for r in range(10):
		room=Room(r+1, random.choice(
			[2, 4, 6, 8]))  # create room with random capacity and room number between 1 and 10
		ROOMS.append(room)  # add the room to the rooms list
	# print(f"{'-'*10}\nRooms list\n{'-'*10}")
	# o3 = order.Order(25, "Mosh Ban Hari", 2, "2/2/2020", "7/2/2020", True)
	# print(f"{'-'*10}\nOrders list\n{'-'*10}")
	#####################################
	# menu()
	create_app()

	# widget.show()
	# app.exec_()

if __name__ == '__main__':
	main()
