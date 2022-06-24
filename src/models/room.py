from datetime import datetime

from .range_of_dates import Dates_Range


class Room():
	def __init__(self, room_num=0, room_cap=2):
		self.room_number=room_num
		self.room_capacity=room_cap
		self.room_is_catch=False
		self.room_is_clean=True
		self.room_faults=[]
		self.dates_catch=[]

	def check_available_date_range(self, date_range):
		for r in self.dates_catch:
			if datetime.strptime(r.get_arrivel_date(), "%d/%m/%Y") <= datetime.strptime(date_range.get_arrivel_date(),
			                                                                            "%d/%m/%Y") and datetime.strptime(
				date_range.get_arrivel_date(), "%d/%m/%Y") <= datetime.strptime(r.get_leaving_date(), "%d/%m/%Y"):
				# if the start date of the received date range is between one of the date ranges that the room is not available, then it is not possible to book the room
				return False
			elif datetime.strptime(r.get_arrivel_date(), "%d/%m/%Y") <= datetime.strptime(date_range.get_leaving_date(),
			                                                                              "%d/%m/%Y") and datetime.strptime(
				date_range.get_leaving_date(), "%d/%m/%Y") <= datetime.strptime(r.get_leaving_date(), "%d/%m/%Y"):
				# if the end date of the received date range is between one of the date ranges that the room is not available, then it is not possible to book the room
				return False
		return True

	def add_date_catch(self, start, end, order_id):
		date_catch=Dates_Range(start, end, order_id)  # create new range
		self.dates_catch.append(date_catch)  # add the new range to the ranges list

	def get_dates_catch(self):
		return self.dates_catch

	def set_room_status(self, room_status):
		self.room_is_catch=room_status

	def get_room_status(self):
		return self.room_is_catch

	def set_clean_status(self, clean_status):
		self.room_is_clean=clean_status

	def get_clean_status(self):
		return self.room_is_clean

	def add_fault(self, fault):
		if fault == "" or type(fault) is not type(""):  # if the variable is not string or is empty string don't add it
			return False
		self.room_faults.append(fault)
		return True

	def remove_fault(self, fault):
		if fault not in self.room_faults:  # if not in the faults list don't try to remove it
			return False
		self.room_faults.remove(fault)
		return True

	def get_room_faults(self):
		return self.room_faults

	def get_room_capacity(self):
		return self.room_capacity

	def get_room_number(self):
		return self.room_number

	def date_range_to_string(self):
		date_range_str=""
		for r in self.dates_catch:
			date_range_str+=r.get_arrivel_date()+"||"+r.get_leaving_date()+"\n"
		return date_range_str

	def __str__(self):

		room_num=str(str(str("Room number: %s." % (self.room_number))).ljust(25))+"||"
		room_cap=str(str(str("Room capacity: %s." % (self.room_capacity))).ljust(25))+"||"
		room_clean=str(str(str("Room clean status: %r." % (self.room_is_clean))).ljust(25))+"||"
		room_catch=str(str(str("Room is catch: %r." % (self.room_is_catch))).ljust(25))+"||"
		room_faults=str(str(str("Room have fault: %r." % (len(self.room_faults) != 0))).ljust(25))+"||"
		date_range_str=self.date_range_to_string()
		return (
			f"\n===========================\n"
			f"{room_num}\n"
			f"{room_cap}\n"
			f"{room_catch}\n"
			f"{room_clean}\n"
			f"{room_faults}\n"
			f"-----Room dates catch-----\n"
			f"{date_range_str}"
			f"===========================\n"
		)
