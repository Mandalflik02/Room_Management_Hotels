import datetime


class Log():
	def __init__(self, log_type="ERROR", log_data="NOT SET"):
		self.type = log_type
		self.data = log_data
		self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	
	def __str__(self):
		return ("%s: "
		        "[%s]--"
		        "[%s]"
		        ) % (str(self.time), self.type, self.data)
