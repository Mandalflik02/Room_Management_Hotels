from .range_of_dates import Dates_Range


class Order():
	def __init__(self, order_num=-1, cusromer_name="", num_of_guests=0, arrivel="", leaving="",
	             with_food=False, room_num=-1):
		self.order_ID = str(order_num).zfill(7)  # set order id format as 8 digit, the space fill with 0
		self.customer_name = cusromer_name
		self.number_of_guests = num_of_guests
		self.dates_range = Dates_Range(arrivel, leaving)
		self.with_food = with_food
		self.room_number = room_num
		self.check_in = False
		self.check_out = False
	
	def set_arrivel_date(self, arrivel_date):
		self.dates_range.set_arrivel_date(arrivel_date)
	
	def get_arrivel_date(self):
		return self.dates_range.get_arrivel_date()
	
	def set_leaving_date(self, leaving_date):
		self.dates_range.set_leaving_date(leaving_date)
	
	def get_leaving_date(self):
		return self.dates_range.get_leaving_date()
	
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
	
	def get_room_number(self):
		return self.room_number
	
	def get_order_id(self):
		return self.order_ID
	
	def __str__(self):
		len1 = len(str(str("Customer name: %s" % (self.customer_name))))
		
		order_num = str(str(str("Order number: %s" % (self.order_ID))).ljust(len1 + 10)) + "||"
		customer_name = str(str(str("Customer name: %s" % (self.customer_name))).ljust(len1 + 10)) + "||"
		number_of_guests = str(str(str("Number of guests: %s" % (self.number_of_guests))).ljust(len1 + 10)) + "||"
		with_food = str(str(str("With food: %s" % (self.with_food))).ljust(len1 + 10)) + "||"
		room_num = str(str(str("Room: %s" % (self.room_number))).ljust(len1 + 10)) + "||"
		check_in = str(str(str("Check-in: %s" % (self.check_in))).ljust(len1 + 10)) + "||"
		check_out = str(str(str("Check-out: %s" % (self.check_out))).ljust(len1 + 10)) + "||"
		return (f"\n{'=' * (len1 + 12)}\n"
		        f"{order_num}\n"
		        f"{customer_name}\n"
		        f"{number_of_guests}\n"
		        f"{with_food}\n"
		        f"{room_num}\n"
		        f"{check_in}\n"
		        f"{check_out}\n"
		        f"{self.dates_range.__str__(len1)}\n"
		        f"{'=' * (len1 + 12)}\n")
