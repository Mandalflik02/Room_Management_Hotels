from datetime import *


class Order():
	def __init__(self, order_num=-1, customer_name="", num_of_guests=0, dates_range=None,
	             meal_options="000", electric_car=False, pet=False, room_num=-1):
		self.order_ID = str(order_num).zfill(8)  # set order id format as 8 digit, the space fill with 0
		self.create_time = datetime.now().strftime("%H:%M:%S , %d/%m/%Y")
		self.created_by = "Admin"
		self.customer_name = customer_name
		self.number_of_guests = num_of_guests
		self.dates_range = dates_range
		self.meal_options = meal_options
		self.electric_car = electric_car
		self.pet = pet
		self.room_number = room_num
		self.check_in = False
		self.check_out = False
	
	def set_arrival_date(self, arrival_date):
		return self.dates_range.set_arrival_date(arrival_date)
	def get_arrival_date(self):
		return self.dates_range.get_arrival_date()
	def set_leaving_date(self, leaving_date):
		return self.dates_range.set_leaving_date(leaving_date)
	def get_leaving_date(self):
		return self.dates_range.get_leaving_date()
	def get_date_range(self):
		return f"{self.dates_range.get_arrival_date()} - {self.dates_range.get_leaving_date()}"
	def get_date_range_obj(self):
		return self.dates_range
	def set_date_range(self, new_date_range):
		if new_date_range == None:
			return VERABLE_ERROR_CODE
		self.dates_range=new_date_range

	def get_meal_options(self):
		return self.meal_options
	def get_breakfast(self):
		try:
			return bool(int(self.meal_options [ 0 ]))
		except Exception as e:
			print(e)
	def get_lunch(self):
		try:
			return bool(int(self.meal_options [ 1 ]))
		except Exception as e:
			print(e)
	def get_dinner(self):
		try:
			return bool(int(self.meal_options [ 2 ]))
		except Exception as e:
			print(e)
	def set_meal_options(self, meal_options="000"):
		self.meal_options = meal_options
	
	def get_electric_car(self):
		return self.electric_car
	def set_electric_car(self, electric_car):
		self.electric_car = electric_car
	
	def get_pet(self):
		return self.pet
	def set_pet(self, pet):
		self.pet = pet


	def get_guests_num(self):
		return self.number_of_guests
	def set_guests_num(self,new_guests_num):
		self.number_of_guests = new_guests_num

	def check_in_customers(self):
		self.check_in = True
	def cancel_check_in_customers(self):
		self.check_in = False
	def get_check_in_status(self):
		return self.check_in
	
	def check_out_customers(self):
		self.check_out = True
	def cancel_check_out_customers(self):
		self.check_out = False
	def get_check_out_status(self):
		return self.check_out
	
	def get_customer_name(self):
		return self.customer_name
	def set_customer_name(self,customer_name):
		self.customer_name=customer_name
	
	def get_room_number(self):
		return self.room_number
	def set_room_number(self,new_room_number):
		self.room_number=new_room_number
	
	def get_order_id(self):
		return self.order_ID
	
	def get_crete_by(self):
		return self.created_by
	def get_creation_time(self):
		return self.create_time
	
	def __str__(self):
		len1 = len(str(str("Customer name: %s" % (self.customer_name))))
		
		order_num = str(str(str("Order number: %s" % (self.order_ID))).ljust(len1 + 10)) + "||"
		customer_name = str(str(str("Customer name: %s" % (self.customer_name))).ljust(len1 + 10)) + "||"
		number_of_guests = str(str(str("Number of guests: %s" % (self.number_of_guests))).ljust(len1 + 10)) + "||"
		meal_options = str(str(str("Meals: %s" % (self.meal_options))).ljust(len1 + 10)) + "||"
		room_num = str(str(str("Room: %s" % (self.room_number))).ljust(len1 + 10)) + "||"
		check_in = str(str(str("Check-in: %s" % (self.check_in))).ljust(len1 + 10)) + "||"
		check_out = str(str(str("Check-out: %s" % (self.check_out))).ljust(len1 + 10)) + "||"
		return (f"\n{'=' * (len1 + 12)}\n"
		        f"{order_num}\n"
		        f"{customer_name}\n"
		        f"{number_of_guests}\n"
		        f"{meal_options}\n"
		        f"{room_num}\n"
		        f"{check_in}\n"
		        f"{check_out}\n"
		        f"{self.dates_range.__str__(len1)}\n"
		        f"{'=' * (len1 + 12)}\n")
