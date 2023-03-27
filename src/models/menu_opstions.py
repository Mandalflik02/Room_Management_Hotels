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


def print_one_or_more_order(order: Order=None):
	try:
		for o in order: print(o)
	except:
		print(order)


def search_order_in_database(name: str="", id: str="00000000"):
	orders_filtered = [ ]
	for o in ORDERS:
		# if the customer in the order is the one I look for add to list
		if o.get_customer_name() == name or o.get_order_id() == id:
			orders_filtered.append(o)
	return orders_filtered  # return list with all the orders


def search_order(customer_name="", order_id="00000000"):
	try:
		print(customer_name, order_id)
		orders_filtered = search_order_in_database(customer_name, order_id)  # search order by customer name or order ID
		if type(orders_filtered) == type([ ]) and len(orders_filtered) == 0:
			# if the is no orders with the customer name print a msg
			print(f"\nNot found orders you search for ->  name:{customer_name}, ID:{order_id}")
			# return orders_filtered
		elif type(orders_filtered) == type([ ]):
			# if the is no orders with the customer name print a msg
			print(f"\nWe found orders you search for ->  name:{customer_name}, ID:{order_id}")
			return orders_filtered
	except:
		print("An Error")


def move_order_to_history(order: Order=None):
	ORDERS_HISTORY.append(order)

# ---------------------- menu options ----------------------

#10) delete order

def delete_order_by_id( delete_code: int=0 ,order_id: str="00000000" ):
	if delete_code != DELETE_CODE:#Must have a delete code to confirm the delete
		return ERROR_CODE,f"Error -> Delete code not mach : {delete_code}"
	order = search_order("",order_id)# Search the order
	# print(order)
	order_index_to_delete = ORDERS.index(order[0])#Find the index of the order
	# print(order_index_to_delete)
	ORDERS.pop(order_index_to_delete)#Delete the order from the orders list
	move_order_to_history(order)#Add the order to history
	create_log_order_room(ORDERS_LOGGER_LEVELS [ "order-deleted" ] [ "value" ],
		                      ORDERS_LOGGER_LEVELS [ "order-deleted" ] [ "msg" ] % (order_id,LOGIN_USER))#log the delete of the order
	return OK_CODE,f"Order number {order_id} deleted (siil live in history)"


# 9) LOGS

def show_logs_by_date():
	date = "2023-02-07"  # input("Enter date to see logs")
	regex = r'[\d]{4}-[\d]{2}-[\d]{1,2}'  # date format
	if re.fullmatch(regex, date) != None:  # check the string is in date format
		
		print(f"from what logger:\n"
		      f"room and order - 1\n"
		      f"error - 2\n")
		logger = input("Enter you logger number: ")
		if logger not in [ "1", "2" ]: print("The number you enter is not 1 or 2.");return
		
		print(f"choose option:\n"
		      f"1) logs from exact day.\n"
		      f"2) logs from starting date.\n")
		logs_date_type = input("Enter you option: ")
		if logs_date_type not in [ "1", "2" ]: print("The number you enter is not 1 or 2.");return
		
		match logs_date_type:
			case "1":
				logs = logs_by_exact_date(logger, date)
			case "2":
				logs = logs_starting_on_date(logger, date)
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
def check_out(order: Order=None):
	try:
		if order.get_check_in_status() and not order.get_check_out_status():
			#  change check-out in the order and change room catch status
			order.check_out_customers()
			create_log_order_room(ORDERS_LOGGER_LEVELS [ "order-check-out" ] [ "value" ],
			                      ORDERS_LOGGER_LEVELS [ "order-check-out" ] [ "msg" ] % order.get_order_id())
			search_room_by_number(order.get_room_number()).set_room_status(False)
			return True,""
		elif order.get_check_out_status():
			return False, "The customer is already check out!!"
		elif not order.get_check_in_status():
			return False, "The customer not check-in yet!!"
	except Exception as e:
		print("check out in menu",e)


# 6) check-in
def check_in(order: Order=None):
	try:
		if not order.get_check_in_status() and not order.get_check_out_status():
			# when  the order it is not check in or out, change check-in in the order and change room catch status
			order.check_in_customers()
			create_log_order_room(ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "value" ],
			                      ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "msg" ] % order.get_order_id())
			search_room_by_number(order.get_room_number()).set_room_status(True)
			return True, ""
		elif order.get_check_in_status():
			return False, "The customer is already check in!!"
		elif order.get_check_out_status():
			return False, "The customer is already check out!!"
	except Exception as e:
		print("check-in in menu",e)


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
	order = search_order()  # search order/s by name
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


def add_new_order(customer_name, guests, meal_options, electric_car, pet, arrival, leaving):
	"""
	Get data of the order and create new one and add to the ORDERS list

	:return: Error if there is one
	"""
	print("------------------Add order------------------")
	
	try:
		order_id = str(len(ORDERS) + 1).zfill(8)  # order number
		
		if guests < 1:  # check if the guests number is ok
			return "Can be 0 guests"
		dates_range = Dates_Range(arrival, leaving)  # create date range for the order
		if dates_range is None:  # check the dates range was created
			return "Cannot create a date range"
		if not dates_range.range_ok:  # check if there is a error in the date range
			return dates_range.error_text
		room = search_available_room(guests, dates_range)  # look for available room
		if room == None:
			return "No room available"
		room_num = room.get_room_number()  # get room number
		if len(search_order(customer_name=customer_name)) > 3:
			return "The customer have 3 order and can have more"
		new_order = Order(order_id, customer_name, guests,
		                  dates_range, meal_options, electric_car, pet, room_num)  # create the order
		
		ROOMS [ ROOMS.index(room) ].add_date_catch(arrival,
		                                           leaving,
		                                           order_id)  # add date_range to the room -> range when the room is caught
		
		ORDERS.append(new_order)  # add order to the orders list
		# create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
		# print("----------------Order create---------------", new_order)  # , ROOMS [ ROOMS.index(room) ])
		create_log_order_room(ORDERS_LOGGER_LEVELS [ "new-order" ] [ "value" ],
		                      ORDERS_LOGGER_LEVELS [ "new-order" ] [ "msg" ] % order_id)
		print(new_order)
		return OK_CODE
	except KeyboardInterrupt:
		exit()
		return "keyboard error"
