from models import room, order, logs

ORDERS = [ ]
ROOMS = [ ]
LOGS = [ ]


def show_logs():
	global LOGS
	print("-------------------LOGS-------------------")
	for l in LOGS:
		print(l)


def create_log(type, data):
	global LOGS
	log = logs.Log(type, data)
	LOGS.append(log)


def show_rooms_status():
	global ROOMS
	print("------------------Rooms status------------------")
	for r in ROOMS:
		print(r)


def show_orders():
	global ORDERS
	print("------------------Orders status------------------")
	for o in ORDERS:
		print(o)


def look_order_by_name(name):
	orders_filtered = [ ]
	for o in ORDERS:
		if name == o.get_customer_name():
			orders_filtered.append(o)
	if len(orders_filtered) == 1:
		return orders_filtered [ 0 ]
	return orders_filtered


def search_order():
	try:
		customer_to_search = input("Enter customer name to search is order: ")
		
		orders_filtered = look_order_by_name(customer_to_search)
		if type(orders_filtered) == type([ ]) and len(orders_filtered) == 0:
			print("\nNot found orders with the name you search: %s" % (customer_to_search))
		else:
			print("\nWe found a order with the name you search: %s" % (customer_to_search))
			return orders_filtered
	except:
		print("An Error")


def one_or_more_orders():
	orders = search_order()
	try:
		return orders
	except:
		return orders


def print_one_or_more_order(order):
	try:
		for o in order:
			print(o)
	except:
		print(order)


def view_order():
	order = one_or_more_orders()
	print_one_or_more_order(order)


def check_in():
	order = one_or_more_orders()
	if type(order) == type([ ]):
		try:
			print_one_or_more_order(order)
			choose_order = int(input("Enter the id of the order you want to check-in: "))
		except:
			print("not a number")
		for o in order:
			if int(o.get_order_id()) == choose_order:
				o.check_in_customers()
				create_log("CHECK IN","order-id: %s"%(o.get_order_id()))
				return
	else:
		order.check_in_customers()
		create_log("CHECK IN", "order-id: %s" % (o.get_order_id()))
		return


def check_out():
	order = one_or_more_orders()
	if type(order) == type([ ]):
		try:
			print_one_or_more_order(order)
			choose_order = int(input("Enter the id of the order you want to check-out: "))
		except:
			print("not a number")
		for o in order:
			if int(o.get_order_id()) == choose_order and o.get_check_in_status() == True:
				o.check_out_customers()
				create_log("CHECK OUT","order-id: %s"%(o.get_order_id()))
				return
		print("The customer not check-in yet!!")
	else:
		if order.get_check_in_status() == True:
			order.check_out_customers()
			create_log("CHECK OUT", "order-id: %s" % (o.get_order_id()))
			return
		else:
			print("The customer not check-in yet!!")


##### add new order #####
def search_available_room(number_of_guests):
	global ROOMS
	
	for r in ROOMS:
		if r.get_room_status() == False and r.get_room_capacity() >= number_of_guests and len(r.get_room_faults()) == 0:
			return r


def add_new_order():
	global ROOMS
	global ORDERS
	print("------------------Add order------------------")
	
	try:
		order_id = str(len(ORDERS) + 1).zfill(7)
		customer_name = input("Enter customer name: ")
		while True:
			# cheack if the user enter number
			number_of_guests = input("Enter the number of guests: ")
			try:
				number_of_guests = int(number_of_guests)
				break
			except:
				print("Enter a number!!")
		arrivel = ""
		leaving = ""
		while True:
			# chack for yes/no answer
			# food = input("The customer want food? ")
			food = "y"
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
		create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
		print("Order create", new_order)  # , ROOMS [ ROOMS.index(room) ])
	except KeyboardInterrupt:
		exit()


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
				add_new_order()
			case 2:
				view_order()
			case 3:
				pass
			case 4:
				show_orders()
			case 5:
				show_rooms_status()
			case 6:
				check_in()
			case 7:
				check_out()
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
