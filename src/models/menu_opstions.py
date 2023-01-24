import re

from .Logs import *
from .global_ver import *
from .order import Order
from .range_of_dates import Dates_Range


# ---------------------- help functions ----------------------
def search_room_by_number(room_number):
	for r in ROOMS:
		# go over all the room and search the room with the number the function get
		if r.get_room_number() == room_number: return r


def print_one_or_more_order(order):
	try:
		for o in order: print(o)
	except:
		print(order)


def look_order_by_name(name):
	orders_filtered=[]
	for o in ORDERS:
		# if the customer in the order is the one I look for add to list
		if name == o.get_customer_name(): orders_filtered.append(o)
	if len(orders_filtered) == 1: return orders_filtered[0]
	# if there is one order on the name the function get return the order as order object
	return orders_filtered  # if there is more than one order on the name the function get return list with all the orders


def search_order():
	try:
		customer_to_search=input("Enter customer name to search is order: ")

		orders_filtered=look_order_by_name(customer_to_search)  # search order by the name the user enter
		if type(orders_filtered) == type([]) and len(orders_filtered) == 0:
			# if the is no orders with the customer name print a msg
			print(f"\nNot found orders with the name you search: {customer_to_search}")
		elif type(orders_filtered) == type([]):
			# if the is no orders with the customer name print a msg
			print(f"\nWe found orders with the name you search: {customer_to_search}")
			return orders_filtered
		else:
			# if the is orders with the customer name print a msg and return the order
			print(f"\nWe found a order with the name you search: {customer_to_search}")
			return orders_filtered
	except:
		print("An Error")


# ---------------------- menu options ----------------------

# 9) LOGS

def show_logs_by_date():
	date="2022-02-12"  # input("Enter date to see logs")
	regex=r'[\d]{4}-[\d]{2}-[\d]{1,2}'  # date format
	if re.fullmatch(regex, date) != None:  # check the string is in date format

		print(f"from what logger:\n"
		      f"room and order - 1\n"
		      f"error - 2\n")
		logger=input("Enter you logger number: ")
		if logger not in ["1", "2"]: print("The number you enter is not 1 or 2.");return

		print(f"choose option:\n"
		      f"1) logs from exact day.\n"
		      f"2) logs from starting date.\n")
		logs_date_type=input("Enter you option: ")
		if logs_date_type not in ["1", "2"]: print("The number you enter is not 1 or 2.");return

		match logs_date_type:
			case "1":
				logs=logs_by_exact_date(logger, date)
			case "2":
				logs=logs_starting_on_date(logger, date)
		match len(logs):
			case 0:
				print(f"No logs find from {date}")
			case _:
				print(f"LOGS from the date {date}")

		for l in logs: print(l)
	else:
		print("you not enter a date")
		return


# 7) check-out
def check_out():
	order=search_order()  # get the order the user is search
	if type(order) == type([]):
		# when there is more than one order on the customer name
		try:
			order_copy=order
			order=[]
			for i in order_copy:
				if not i.get_check_out_status() and i.get_check_in_status(): order.append(i)
			print_one_or_more_order(order)

			choose_order=int(
				input("Enter the id of the order you want to check-out: "))  # ask the user which order to check out
		except ValueError:
			print("not a number")
			return
		for o in order:
			# look for the order the user choose
			if int(o.get_order_id()) == choose_order and o.get_check_in_status() and not o.get_check_out_status():
				# when find the order, change check-out in the order and change room catch status
				o.check_out_customers()
				create_log_order_room(ORDERS_LOGGER_LEVELS["order-check-out"]["value"],
				                      ORDERS_LOGGER_LEVELS["order-check-out"]["msg"] % o.get_order_id())
				search_room_by_number(o.get_room_number()).set_room_status(False)
				return
			else:
				if order.get_check_out_status():
					print("The customer is already check out!!")
				elif not order.get_check_in_status():
					print("The customer not check-in yet!!")
		print("The customer not check-in yet!!")
	elif type(order) == "<class 'models.order.Order'>":
		# when there is one order on the customer name
		if order.get_check_out_status() == False and order.get_check_in_status() == True:
			# change check-out in the order and change room catch status
			order.check_out_customers()
			create_log_order_room(ORDERS_LOGGER_LEVELS["order-check-out"]["value"],
			                      ORDERS_LOGGER_LEVELS["order-check-out"]["msg"] % order.get_order_id())
			search_room_by_number(order.get_room_number()).set_room_status(False)
			return
		else:
			if order.get_check_out_status():
				print("The customer is already check out!!")
			elif not order.get_check_in_status():
				print("The customer not check-in yet!!")
	else:
		print("Error !!!!!!!!!!!!!!!!!!!!!!!!!!")


# 6) check-in
def check_in():
	order=search_order()
	if type(order) == type([]):
		choose_order=None
		# when there is more than one order on the customer name
		try:
			order_copy=order
			order=[]
			for i in order_copy:
				if not i.get_check_in_status():
					order.append(i)
			print_one_or_more_order(order)
			# ask the user which order to check in
			choose_order=int(input("Enter the id of the order you want to check-in: "))
		except:
			print("not a number")
		for o in order:
			# look for the order the user choose
			if int(o.get_order_id()) == choose_order and not o.get_check_in_status() and not o.get_check_out_status():
				# when find the order it is not check in or out, change check-in in the order and change room catch status
				o.check_in_customers()
				create_log_order_room(ORDERS_LOGGER_LEVELS["order-check-in"]["value"],
				                      ORDERS_LOGGER_LEVELS["order-check-in"]["msg"] % o.get_order_id())
				search_room_by_number(o.get_room_number()).set_room_status(True)
				return
			elif order.get_check_out_status():
				print("The customer is already check out!!")

	elif type(order) == "<class 'models.order.Order'>":
		# when there is one order on the customer name.
		# change check-in status in the order and change room catch status.
		if not order.get_check_in_status():
			print("You already check in")
			return
		order.check_in_customers()
		create_log_order_room(ORDERS_LOGGER_LEVELS["order-check-in"]["value"],
		                      ORDERS_LOGGER_LEVELS["order-check-in"]["msg"] % order.get_order_id())
		search_room_by_number(order.get_room_number()).set_room_status(True)
		return
	else:
		print("Error !!!!!!!!!!!!!!!!!!!!!!!!!!")
		print(type(order))


# 5) room status
def show_rooms_status():
	print("------------------Rooms status------------------")
	# print all the rooms
	for r in ROOMS:
		print(r)


# 4) show orders
def show_orders():
	print("------------------Orders status------------------")
	# print all the orders
	for o in ORDERS:
		print(o)


# 3) update order
def update_order():
	return None


# 2) view order
def view_order():
	order=search_order()  # search order/s by name
	print_one_or_more_order(order)  # print order/s


# 1) add new order
def search_available_room(number_of_guests, date_range):
	for r in ROOMS:
		if r.get_room_capacity() >= number_of_guests and \
				len(r.get_room_faults()) == 0 and \
				r.check_available_date_range(date_range) == True:
			# if the room capacity is more the number of guests,
			# and the room has no fault,
			# and the room is available in the range of date the customer want,
			# the room is available return the room.
			return r


def add_new_order(current_time,customer_name,guests,food,):
	print("------------------Add order------------------")

	try:
		order_id=str(len(ORDERS)+1).zfill(7)  # order number
		customer_name=input("Enter customer name: ")  # the name of the customer who orders --------------------------
		while True:
			# check if the user enter number
			number_of_guests=input("Enter the number of guests: ") #------------------------
			try:
				number_of_guests=int(number_of_guests)
				if number_of_guests < 1:
					raise ValueError
				break
			except:
				print("Enter a number!! (more then 0)")
		arrivel="1/1/1000"  # input("Enter arrivel date(format- day/month/year): ")  -------------------------------
		leaving="1/2/1000"  # input("Enter leaving date(format- day/month/year): ")  --------------------------------
		date_range=Dates_Range(arrivel, leaving)  # create date range for the order
		while True:
			# check for yes/no answer
			# food = input("The customer want food? ")
			food="y"#----------------------
			if food in ["yes", "YES", "Yes", "y", "Y"]:
				food=True
				break
			elif food in ["no", "NO", "No", "n", "N"]:
				food=False
				break
			else:
				print("Not an answer!!")

		room=search_available_room(number_of_guests, date_range)  # look for available room
		if room == None:
			print("--------------No room available--------------")
			return
		room_num=room.get_room_number()  # get room number
		ROOMS[ROOMS.index(room)].add_date_catch(arrivel,
		                                        leaving,
		                                        order_id)  # add date_range to the room -> range when the room is caught

		new_order=Order(order_id, customer_name, number_of_guests,
		                arrivel, leaving, food, room_num)  # create the order

		ORDERS.append(new_order)  # add order to the orders list
		# create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
		# print("----------------Order create---------------", new_order)  # , ROOMS [ ROOMS.index(room) ])
		create_log_order_room(ORDERS_LOGGER_LEVELS["new-order"]["value"],
		                      ORDERS_LOGGER_LEVELS["new-order"]["msg"] % order_id)
	except KeyboardInterrupt:
		exit()
