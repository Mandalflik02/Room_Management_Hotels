import models
# from models import room, order, logs





def show_logs():
	print("-------------------LOGS-------------------")
	for l in models.global_ver.LOGS:
		print(l)


def create_log(type, data):
	log = models.Log(type, data)
	models.global_ver.LOGS.append(log)



def menu():
	choose = -1
	while choose != 10:
		print("\n\nMenu\n"
		      "1) add order\n"
		      "2) view order\n"
		      "3) update order\n"
		      "4) orders list\n"
		      "5) rooms status\n"
		      "6) chack-in\n"
		      "7) chack-out\n"
		      "9) LOGS\n"
		      "10) EXIT\n")
		try:
			choose = int(input("Choose opstion: "))
		except ValueError:
			print("       Enter a number")
			continue
		except KeyboardInterrupt:
			break
		match choose:
			case 1:
				models.menu_opstions.add_new_order()
			case 2:
				models.menu_opstions.view_order()
			case 3:
				models.menu_opstions.update_order()
			case 4:
				models.menu_opstions.show_orders()
			case 5:
				models.menu_opstions.show_rooms_status()
			case 6:
				models.menu_opstions.check_in()
			case 7:
				models.menu_opstions.check_out()
			case 9:
				show_logs()
			case 10:
				continue
			case _:
				print("[ ERROR ] - not in the range of the opstions")


def main():
	r1 = models.Room(1, 2)
	r2 = models.Room(2, 4)
	r3 = models.Room(3, 6)
	# print(f"{'-'*10}\nRooms list\n{'-'*10}")
	# o3 = order.Order(25, "Mosh Ban Hari", 2, "2/2/2020", "7/2/2020", True)
	# print(f"{'-'*10}\nOrders list\n{'-'*10}")
	models.global_ver.ROOMS.append(r1)
	models.global_ver.ROOMS.append(r2)
	models.global_ver.ROOMS.append(r3)
	
	menu()


if __name__ == '__main__':
	main()
