from .global_ver import *
from .order import Order
from .range_of_dates import Dates_Range

def show_rooms_status():
	print("------------------Rooms status------------------")
	for r in ROOMS:
		print(r)


def show_orders():
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


def print_one_or_more_order(order):
	try:
		for o in order:
			print(o)
	except:
		print(order)


def view_order():
	order = search_order()
	print_one_or_more_order(order)


def check_in():
	order = search_order()
	if type(order) == type([ ]):
		try:
			print_one_or_more_order(order)
			choose_order = int(input("Enter the id of the order you want to check-in: "))
		except:
			print("not a number")
		for o in order:
			if int(o.get_order_id()) == choose_order:
				o.check_in_customers()
				# create_log("CHECK IN", "order-id: %s" % (o.get_order_id()))
				return
	else:
		order.check_in_customers()
		# create_log("CHECK IN", "order-id: %s" % (o.get_order_id()))
		return


def check_out():
	order = search_order()
	if type(order) == type([ ]):
		try:
			print_one_or_more_order(order)
			choose_order = int(input("Enter the id of the order you want to check-out: "))
		except:
			print("not a number")
		for o in order:
			if int(o.get_order_id()) == choose_order and o.get_check_in_status() == True:
				o.check_out_customers()
				# create_log("CHECK OUT", "order-id: %s" % (o.get_order_id()))
				return
		print("The customer not check-in yet!!")
	else:
		if order.get_check_in_status() == True:
			order.check_out_customers()
			# create_log("CHECK OUT", "order-id: %s" % (order.get_order_id()))
			return
		else:
			print("The customer not check-in yet!!")


##### add new order #####
def search_available_room(number_of_guests,date_range):
	for r in ROOMS:
		if 	r.get_room_capacity() >= number_of_guests and \
				len(r.get_room_faults()) == 0 and \
				r.check_available_date_range(date_range) == True:
			return r


def add_new_order():
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
		arrivel = "1/12/2020"
		leaving = "3/1/2021"
		date_range=Dates_Range(arrivel,leaving)
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
		
		room = search_available_room(number_of_guests,date_range)  # look for empty room
		if room == None:
			print("--------------No room available--------------")
			return
		room_num = room.get_room_number()  # get room number
		# ROOMS [ ROOMS.index(room) ].set_room_status(True)  # upstae the room status
		ROOMS [ ROOMS.index(room) ].add_date_catch(arrivel,leaving)
		new_order = Order(order_id, customer_name, number_of_guests, arrivel, leaving, food,
		                  room_num)  # create the order
		ORDERS.append(new_order)  # add orser to the orders list
		# create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
		print("----------------Order create---------------", new_order)  # , ROOMS [ ROOMS.index(room) ])
	except KeyboardInterrupt:
		exit()


def update_order():
	return None


