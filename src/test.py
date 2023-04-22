from models import *

def menu(order):
	choose = -1
	while choose != 11:
		print("\n-------------------Menu-------------------\n"
		      "1) add order\n"
		      "2) update order\n"
		    #   "3) update order\n"
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
					up=update_order(order=order,guests=7,arrival_date="10/01/2025",leaving_date="01/01/2025")
					order=up[1]
					print(up[0])
					print(up[1])
				case 3:
					try:
						room_capacity = int(input("Enter room capacity: "))
						add_new_room()
					except:
						print("Not valid room capacity")
				case 4:
					pass
				case 5:
					pass
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


d1=create_range("01/01/2025","09/01/2025",1)
ROOMS.append(Room(1,4))
ROOMS.append(Room(2,8))
order1=Order(customer_name="naor",num_of_guests=2,dates_range=d1,order_num=1,room_num=1)
ROOMS[0].add_date_catch(d1.get_arrival_date(),d1.get_leaving_date(),order1.get_order_id())
ORDERS.append(order1)
menu(order1)
