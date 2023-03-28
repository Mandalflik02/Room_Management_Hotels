from models import *

def menu():
	choose = -1
	while choose != 11:
		print("\n-------------------Menu-------------------\n"
		      "1) add order\n"
		      "2) view order\n"
		      "3) update order\n"
		      "4) orders list\n"
		      "5) rooms status\n"
		      "6) check-in\n"
		      "7) check-out\n"
		      "9) LOGS\n"
		      "10)Delete order\n"
			  "11)Exit\n"
			  "------------------------------------------")
		try:
			choose = int(input("\nChoose option: "))
			match choose:
				case 1:
					print(add_new_order())
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
					print(delete_order_by_id(DELETE_CODE,"00000002"))
				case 11:
					continue
				case _:
					print("[ ERROR ] - not in the range of the options")
		except ValueError:
			print("-------------------Enter a number-------------------")
			continue
		except KeyboardInterrupt:
			break


d1=Dates_Range("01/01/2025","09/01/2025",1)
d2=Dates_Range("01/02/2025","09/02/2025",2)
d3=Dates_Range("01/03/2025","09/03/2025",3)
ROOMS.append(Room(1,5))
ROOMS.append(Room(2,5))
ROOMS.append(Room(3,5))
ORDERS.append(Order(customer_name="naor",num_of_guests=5,dates_range=d1,order_num=1,room_num=1))
ORDERS.append(Order(customer_name="naor",num_of_guests=2,dates_range=d2,order_num=2,room_num=2))
ORDERS.append(Order(customer_name="naor",num_of_guests=3,dates_range=d3,order_num=3,room_num=3))
menu()
