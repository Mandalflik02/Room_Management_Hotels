from models import room, order,logs

ORDERS = [ ]
ROOMS = [ ]
LOGS=[]

def show_logs():
	global LOGS
	print("-------------------LOGS-------------------")
	for l in LOGS:
		print(l)
def create_log(type,data):
	global LOGS
	log=logs.Log(type,data)
	LOGS.append(log)

def show_rooms_status():
	global ROOMS
	print("------------------Rooms status------------------")
	for r in ROOMS:
		print(r)









##### search order #####

order_typy = {
	"id": 0,
	"name": 1,
	"num_of_guests": 2,
	"arrivel": 3,
	"leaving": 4,
	"food": 5
}


def look_for_order_by_value(type, value):
	orders_filtered = [ ]
	for o in ORDERS:
		if value == o.look_in_the_order() [ type ]:
			orders_filtered.append(o)
	
	return orders_filtered


def search_order():
	try:
		print("Data types")
		for i in order_typy.keys():
			print("%s) %s" % (order_typy [ i ], i))
		type_to_search = int(input("Choose the type of data for the list you want to filter by: "))
		data_to_search = input("Write the data you want to search: ")
		
		orders_filtered = look_for_order_by_value(order_typy [ type_to_search ], data_to_search)
		if len(orders_filtered) == 0:
			print("\nNot found order with the data you search\ntype: %s\ndata: %s" % (type_to_search, data_to_search))
		else:
			print("\nWe found a %s orders with the data you search\ntype: %s\ndata: %s" % (
				len(orders_filtered), type_to_search, data_to_search))
			for o in orders_filtered:
				print(o)
	except:
		print("An Error")


# search_order()

##### add new order #####
def search_available_room(number_of_guests):
	global ROOMS
	
	for r in ROOMS:
		print(r.get_room_faults())
		if r.get_room_status() == False and r.get_room_capacity() >= number_of_guests and len(r.get_room_faults()) == 0:
			return r


def add_new_order():
	global ROOMS
	print("------------------Add order------------------")

	try:
		order_id = 0
		customer_name = input("Enter customer name: ")
		while True:
			# cheack if the user enter number
			number_of_guests = input("Enter the number of guests: ")
			try:
				number_of_guests = int(number_of_guests)
				break
			except:
				print("Enter a number!!")
		arrivel = input("Etner arrivel date: ")
		leaving = input("Enter leaving date: ")
		while True:
			# chack for yes/no answer
			food = input("The customer want food? ")
			if food in [ "yes", "YES", "Yes", "y", "Y" ]:
				food = True
				break
			elif food in [ "no", "NO", "No", "n", "N" ]:
				food = False
				break
			else:
				print("Not an answer!!")
		
		room = search_available_room(number_of_guests)  # look for empty room
		if room == None:
			print("--------------No room available--------------")
			return
		room_num = room.get_room_number()  # get room number
		ROOMS [ ROOMS.index(room) ].set_room_status(True)  # upstae the room status
		
		new_order = order.Order(order_id, customer_name, number_of_guests, arrivel, leaving, food,
		                        room_num)  # create the order
		ORDERS.append(new_order)  # add orser to the orders list
		create_log("NEW ORDER","New order create, order ID: %s"%(order_id))
		print(new_order, ROOMS [ ROOMS.index(room) ])
	except KeyboardInterrupt:
		exit()


def menu():
	choose = -1
	while choose != 10:
		print("\n\nMenu\n"
		      "1) add order\n"
		      "2) view order\n"
		      "3) update order\n"
		      "4) rooms status\n"
		      "5) chack-in\n"
		      "6) chack-out\n"
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
				add_new_order()
			case 2:
				search_order()
			case 3:
				pass
			case 4:
				show_rooms_status()
			case 5:
				pass
			case 6:
				pass
			case 9:
				show_logs()
			case 10:
				continue
			case _:
				print("[ ERROR ] - not in the range of the opstions")


def main():
	global ROOMS
	r1 = room.Room(1, 2)
	r2 = room.Room(2, 4)
	r3 = room.Room(3, 6)
	# print(f"{'-'*10}\nRooms list\n{'-'*10}")
	# o3 = order.Order(25, "Mosh Ban Hari", 2, "2/2/2020", "7/2/2020", True)
	# print(f"{'-'*10}\nOrders list\n{'-'*10}")
	ROOMS.append(r1)
	ROOMS.append(r2)
	ROOMS.append(r3)
	
	menu()


if __name__ == '__main__':
	main()
