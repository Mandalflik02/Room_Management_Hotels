


class Room():
	def __init__(self,room_num=0,room_cap=2):
		self.room_number = room_num
		self.room_capacity = room_cap
		self.room_is_catch = False
		self.room_is_clean = True
	
	def set_room_status(self, room_status):
		self.room_is_catch = room_status
	
	def set_clean_status(self, clean_status):
		self.room_is_clean = clean_status
	
	def __str__(self):
		
		room_num=str(str(str("Room number: %s." % (self.room_number))).ljust(25)) + "||"
		room_cap=str(str(str("Room capacity: %s." % (self.room_capacity))).ljust(25)) + "||"
		room_clean=str(str(str("Room clean status: %r." % (self.room_is_clean))).ljust(25)) + "||"
		room_catch=str(str(str("Room is catch: %r."%(self.room_is_catch))).ljust(25))+"||"
	
		return (
				"\n===========================\n%s\n%s\n%s\n%s\n===========================\n" % (
		room_num, room_cap,room_catch,room_clean)
		)

# test ="===========================\nRoom number: %s.\nRoom capacity: %s.\nRoom clean status: %r.\nRoom occupancy status: %r.\n===========================\n"%(0,2,False,False)
# print(test)