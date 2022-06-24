import random

import models


# self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
				models.add_new_order()
			case 2:
				models.view_order()
			case 3:
				models.update_order()
			case 4:
				models.show_orders()
			case 5:
				models.show_rooms_status()
			case 6:
				models.check_in()
			case 7:
				models.check_out()
			case 9:
				models.show_logs_by_date()
			case 10:
				continue
			case _:
				print("[ ERROR ] - not in the range of the options")


def main():
	for r in range(10):
		room=models.Room(r+1, random.choice(
			[2, 4, 6, 8]))  # create room with random capacity and room number between 1 and 10
		models.ROOMS.append(room)  # add the room to the rooms list
	# print(f"{'-'*10}\nRooms list\n{'-'*10}")
	# o3 = order.Order(25, "Mosh Ban Hari", 2, "2/2/2020", "7/2/2020", True)
	# print(f"{'-'*10}\nOrders list\n{'-'*10}")
	menu()


if __name__ == '__main__':
	main()
