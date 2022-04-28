class Order():
	def __init__(self, order_num=-1, cusromer_name="", num_of_guests=0, arrivel="1/1/1900", leaving="1/1/1900",
	             with_food=False,room_num=-1):
		self.order_ID = str(order_num).zfill(7)
		self.customer_name = cusromer_name
		self.number_of_guests = num_of_guests
		self.arrivel_date = arrivel
		self.leaving_date = leaving
		self.with_food = with_food
		self.room_number=room_num
	
	def set_arrivel_date(self, arrivel_date):
		self.arrivel_date = arrivel_date
	
	def set_leaving_date(self, leaving_date):
		self.leaving_date = leaving_date
	
	def look_in_the_order(self):
		return [ self.order_ID, self.customer_name, self.number_of_guests, self.arrivel_date, self.leaving_date,
		         self.with_food ,self.room_number]
	
	def __str__(self):
		len1 = len(str(str("Customer name: %s" % (self.customer_name))))
		
		order_num = str(str(str("Order number: %s" % (self.order_ID))).ljust(len1 + 5)) + "||"
		customer_name = str(str(str("Customer name: %s" % (self.customer_name))).ljust(len1 + 5)) + "||"
		number_of_guests = str(str(str("Number of guests: %s" % (self.number_of_guests))).ljust(len1 + 5)) + "||"
		with_food = str(str(str("With food: %s" % (self.with_food))).ljust(len1 + 5)) + "||"
		arrivel = str(str(str("Arrivel date: %s" % (self.arrivel_date))).ljust(len1 + 5)) + "||"
		leaving = str(str(str("Leaving date: %s" % (self.leaving_date))).ljust(len1 + 5)) + "||"
		room_num = str(str(str("Room: %s" % (self.room_number))).ljust(len1 + 5)) + "||"
		return (
				f"\n{'=' * (len1 + 7)}\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n{'=' * (len1 + 7)}\n" % (
			order_num, customer_name, number_of_guests, with_food, arrivel, leaving,room_num)
		)
