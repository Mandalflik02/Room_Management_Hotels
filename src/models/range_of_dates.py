import re


class Dates_Range():
	def __init__(self, start, end):
		self.start = self.is_date(start)
		self.end = self.is_date(end)
		self.range_ok = False
		self.error_text = ""
		if self.start == "" or self.end == "":
			self.range_ok = None
			self.error_text = "One of the dates is not good"
			return
		self.range_ok, self.error_text = self.check_range(start, end)
	
	def is_date(self, string):
		date = string
		regex = r'[\d]{1,2}/[\d]{1,2}/[\d]{4}'  # date format
		if re.fullmatch(regex, date) != None:
			check_date_numbers = self.conver_to_int(date.split("/"))
			if (check_date_numbers [ 0 ] > 31 or check_date_numbers [ 0 ] < 1) or (
					check_date_numbers [ 1 ] > 12 or check_date_numbers [ 1 ] < 1):
				return ""
			return date
		return ""
	
	def conver_to_int(self, list_to_convert):
		new_list = [ ]
		for i in list_to_convert:
			try:
				new_list.append(int(i))
			except:
				print("----ERROR: can not convert to int-----")
		return new_list
	
	def check_range(self, start, end):
		arrivel = self.conver_to_int(start.split("/"))
		leaving = self.conver_to_int(end.split("/"))
		# 30/10/2020
		# 1/11/2020
		if arrivel [ 2 ] == leaving [ 2 ]:
			count = leaving [ 1 ] - arrivel [ 1 ]
			if count > 2:
				return False, "More then 2 month"
			if arrivel [ 1 ] == leaving [ 1 ]:
				if arrivel [ 0 ] == leaving [ 0 ]:
					return False, "The same date"
				elif arrivel [ 0 ] < leaving [ 0 ]:
					return True, ""
				elif arrivel [ 0 ] > leaving [ 0 ]:
					return False, "Day of arrivel is after day of leaving"
			elif arrivel [ 1 ] < leaving [ 1 ]:
				return True, ""
			elif arrivel [ 1 ] > leaving [ 1 ]:
				return False, "Month of arrivel is after month of leaving"
		elif arrivel [ 2 ] < leaving [ 2 ]:
			yaer_count = leaving [ 2 ] - arrivel [ 2 ]
			month_count = (12 - arrivel [ 1 ]) + leaving [ 1 ]
			if yaer_count > 1:
				return False, "More then a yaer"
			elif month_count > 2:
				return False, "More then 2 month"
			return True, ""
		elif arrivel [ 2 ] > leaving [ 2 ]:
			return False, "Year of arrivel is after year of leaving"
	
	def set_arrivel_date(self, arrivel_date):
		self.start = arrivel_date
	
	def get_arrivel_date(self):
		return self.start
	
	def set_leaving_date(self, leaving_date):
		self.end = leaving_date
	
	def get_leaving_date(self):
		return self.end
	
	def __str__(self, len1):
		title = str(str(str("---Range of dates---")).ljust(len1 + 10)) + "||"
		start = str(str(str("Start: %s" % (self.start))).ljust(len1 + 10)) + "||"
		end = str(str(str("End: %s" % (self.end))).ljust(len1 + 10)) + "||"
		
		return (f"{title}\n"
		        f"{start}\n"
		        f"{end}")

# r1 = Dates_Range("1/15/2020", "3/1/2021")
# print(r1)
