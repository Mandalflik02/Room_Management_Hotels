import re


from .Logs import *
from .global_ver import *
from .order import Order
from .room import Room
from .range_of_dates import Dates_Range,create_range

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
		orders_filtered = search_order_in_database(customer_name, order_id)  # search order by customer name or order ID
		if len(orders_filtered) != 0:
			return orders_filtered
	except Exception as e:
		print("An Error search order in database" , e)

def move_order_to_history(order: Order=None):
	ORDERS_HISTORY.append(order)

def get_room_by_order(order: Order=None) -> Room:
	room_num=order.get_room_number()
	return search_room_by_number(room_num)

# ---------------------- menu options ----------------------


#10) delete order
def delete_order_by_id( delete_code: int=0 ,order_id: str="00000000" ):
	try:
		if delete_code != DELETE_CODE:#Must have a delete code to confirm the delete
			return ERROR_CODE,f"Error -> Delete code not mach : {delete_code}"
		order = search_order("",order_id)[0]# Search the order
		if not get_room_by_order(order).remove_date_catch(order.get_date_range_obj()):#remove the order dates from the room
			return ERROR_CODE,f"Error -> Can't remove date_range from room {order.get_room_num()}"
		ORDERS.remove(order)#Delete the order
		move_order_to_history(order)#Add the order to history
		create_log_order_room(ORDERS_LOGGER_LEVELS [ "order-deleted" ] [ "value" ],
								ORDERS_LOGGER_LEVELS [ "order-deleted" ] [ "msg" ] % (order_id,CURRENT_USER))#log the delete of the order
		return OK_CODE,f"Order number {order_id} deleted (siil live in history)"
	except Exception as e:
		return ERROR_CODE,f"Error -> {e}"

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
		if logs_date_type not in [ "1", "2" ]: 
			print("The number you enter is not 1 or 2.")
			return
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


# 3) add room

def add_new_room(room_capacity: int=0):
	if room_capacity < 2 or room_capacity > 12:
		#must have a room capacity to add
		return ERROR_CODE,f"Error -> Room capacity must be between 2 and 12"
	else:
		room = Room( room_num = len(ROOMS) +1 ,room_cap = room_capacity)
		ROOMS.append(room)
		create_log_order_room(ROOMS_LOGGER_LEVELS [ "new-room" ] [ "value" ],
                      ROOMS_LOGGER_LEVELS [ "new-room" ] [ "msg" ] % (room.get_room_number(), CURRENT_USER))
		return OK_CODE,f"Room {room.get_room_number()} added"


# 2) update order
def new_date_range(order:Order=None ,arrival_date: str=None, leaving_date: str=None): 
	new_dates=None
	if arrival_date == order.get_arrival_date() and leaving_date == order.get_leaving_date():
		#if the dates is the same as the current dates
		return None
	elif arrival_date!= None and leaving_date== None:
		#if the arrival date is diffrent
		new_dates=create_range(arrival_date,order.get_leaving_date(),order.get_order_id())
	elif arrival_date== None and leaving_date!= None:
		#if the leaving date is diffrent
		new_dates=create_range(order.get_arrival_date(),leaving_date,order.get_order_id())
	else:
		#if both dates are diffrent
		new_dates = create_range(arrival_date,leaving_date,order.get_order_id())
	return new_dates

def update_order(order: Order=None,customer_name: str=None, guests: int=None, meal_options: str=None, electric_car: bool=None, pet: bool=None, arrival_date: str=None, leaving_date: str=None):
	if order == None:
		#must have an order to update
		return ERROR_CODE,f"Error -> Order not found"
	order_room=search_room_by_number(order.get_room_number())#find the current room number
	if customer_name != None:
		#update the customer name
		order.set_customer_name(customer_name)
	if meal_options!= None:
		#update the meal options
		order.set_meal_options(meal_options)
	if electric_car!= None:
		#update the electric car
		order.set_electric_car(electric_car)
	if pet!= None:
		#update the pet
		order.set_pet(pet)
	if guests!= None and (arrival_date != None or leaving_date!= None):
		#if the guests is different and one of the dates is different
		print("guests!= None and (arrival_date != None or leaving_date!= None)")
		if  order_room.get_room_capacity() >= guests:
			#the same room can by use 
			new_dates=new_date_range(order,arrival_date,leaving_date)#creat new dates
			if new_dates == None:
				#the datas are the same as the current dates
				new_dates=order.get_date_range()
			order_room.add_date_catch(new_dates.get_arrival_date(),new_dates.get_leaving_date(),order.get_order_id())# add the new dates to the room
			order_room.remove_date_catch(order.get_date_range_obj())#remove the old dates from the room
			order.set_guests_num(guests)# set the new number of guest in the order
			order.set_date_range(new_dates)#set the new date range in the order
		else:
			#the same room can not be used and need to find a new one
			new_dates=new_date_range(order,arrival_date,leaving_date)# creat new dates
			if new_dates == None:
				#the datas are the same as the current dates
				new_dates=order.get_date_range_obj()
			elif new_dates == ERROR_CODE:
				return ERROR_CODE,f"Error -> Can't create a new date range for the order"
			new_order_room=search_available_room(guests,new_dates)# find the new room
			if new_order_room== None:
				# if there is no available room
				return ERROR_CODE,f"Error -> No available room"
			order_room.remove_date_catch(order.get_date_range_obj())# remove the old dates from the room
			# print(new_dates)
			print("test:",new_dates.get_arrival_date())
			new_order_room.add_date_catch(new_dates.get_arrival_date(),new_dates.get_leaving_date(),order.get_order_id()) # add the new dates to the room
			order.set_guests_num(guests)#set the new number of guest in the order
			order.set_room_number(new_order_room.get_room_number())# set the new room number in the order
			order.set_date_range(new_dates)#set the new date range in the order
		create_log_order_room(ORDERS_LOGGER_LEVELS [ "order-update" ] [ "value" ],
                                  ORDERS_LOGGER_LEVELS [ "order-update" ] [ "msg" ] % order.get_order_id())# create log for update the order
	elif guests!= None and arrival_date == None and leaving_date== None:
		#if the guests is different and no one of the dates is different
		print("guests!= None and arrival_date == None and leaving_date== None")
		if order_room.get_room_capacity() >= guests:
			# the same room can by use 
			order.set_guests_num(guests)
		else:
			#the same room can not be used and need to find a new one
			dates=order.get_date_range_obj()
			new_order_room=search_available_room(guests,dates)
			if new_order_room== None:
				return ERROR_CODE,f"Error -> No available room"
			order_room.remove_date_catch(order.get_date_range_obj())
			new_order_room.add_date_catch(dates.get_arrival_date(),dates.get_leaving_date(),order.get_order_id())
			order.set_guests_num(guests)
			order.set_room_number(new_order_room.get_room_number())
	elif arrival_date!= None or leaving_date!= None:
		print("arrival_date!= None or leaving_date!= None")
		new_dates=new_date_range(order,arrival_date,leaving_date)
		if new_dates == None:
				new_dates=order.get_date_range()
				return ERROR_CODE,f"Error -> Dates are the same"
		new_order_room=search_available_room(order.get_guests_num(),new_dates)
		if new_order_room!= None:
			return ERROR_CODE,f"Error -> No available room"
		order_room.remove_date_catch(order.get_date_range_obj())
		new_order_room.add_date_catch(new_dates.get_arrival_date(),new_dates.get_leaving_date(),order.get_order_id())
		order.set_date_range(new_dates)
		order.set_room_number(new_order_room.get_room_number())
		order.set_date_range(new_dates)#set the new date range in the order

	return OK_CODE,order
	

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
	return None

def add_new_order(customer_name: str=None, guests: int=None, meal_options: str=None, electric_car: bool=None, pet: bool=None, arrival_date: str=None, leaving_date: str=None):
	"""
	Get data of the order and create new one and add to the ORDERS list

	:return: Error if there is one
	"""
	if customer_name == None or guests == None or meal_options == None or electric_car == None or pet == None or arrival_date == None or leaving_date == None:
		return VERABLE_ERROR_CODE ,"Please fill all the fields"
	try:
		# print("------------------Start create order------------------")
		order_id = str(len(ORDERS) + 1).zfill(8)  # order number
		if guests < 1:  # check if the guests number is ok
			return VERABLE_ERROR_CODE ,"Can be 0 guests"
		dates_range = Dates_Range(arrival_date, leaving_date)  # create date range for the order
		if dates_range is None:  # check the dates range was created
			return VERABLE_ERROR_CODE ,"Cannot create a date range"
		if not dates_range.range_ok:  # check if there is a error in the date range
			return dates_range.error_text
		room = search_available_room(guests, dates_range)  # look for available room
		if room == None:
			return ROOM_ERROR_CODE,"No room available"
		room_num = room.get_room_number()  # get room number
		customer_exist_orders= search_order(customer_name=customer_name)
		if type(customer_exist_orders) is list and len(customer_exist_orders) >= 3:
			return MAX_ORDERS_CODE,"The customer have 3 order and can have more"
		new_order = Order(order_id, customer_name, guests,
		                  dates_range, meal_options, electric_car, pet, room_num)  # create the order
		ROOMS [ ROOMS.index(room) ].add_date_catch(arrival_date,leaving_date,order_id)  # add date_range to the room -> range when the room is caught
		ORDERS.append(new_order)  # add order to the orders list
		# create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
		# print("----------------Order create---------------", new_order)  # , ROOMS [ ROOMS.index(room) ])
		create_log_order_room(ORDERS_LOGGER_LEVELS [ "new-order" ] [ "value" ],
		                      ORDERS_LOGGER_LEVELS [ "new-order" ] [ "msg" ] % order_id)
		# print(new_order)
		# print("-------------END create order------------")
		return OK_CODE,"Order created successfully"
	except KeyboardInterrupt:
		exit()
		return ERROR_CODE,"keyboard error"

