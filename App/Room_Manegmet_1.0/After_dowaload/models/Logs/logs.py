import logging
from datetime import datetime

from .logs_levels import *

orders_rooms_logger=None
errors_logger=None


def create_logger(name, log_file, level=logging.INFO):
	formatter=logging.Formatter('[%(asctime)s] || %(levelname)s || %(message)s')

	heandler=logging.FileHandler(log_file)
	heandler.setFormatter(formatter)

	logger=logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(heandler)

	return logger


def add_new_levels():
	for k, v in ORDERS_LOGGER_LEVELS.items():
		logging.addLevelName(v["value"], v["name"])
	for k, v in ROOMS_LOGGER_LEVELS.items():
		logging.addLevelName(v["value"], v["name"])


def create_log_order_room(level_value=logging.CRITICAL, msg="Something go very very wrong"):
	global orders_rooms_logger
	orders_rooms_logger.log(level_value, msg)


def create_log_error(level_value=logging.CRITICAL, msg="Something go very very wrong"):
	global errors_logger
	errors_logger.log(level_value, msg)


def read_logs(file):
	with open(file, "r") as f:
		logs=f.read()
		logs=logs.split("\n")
		try:
			logs.remove('')
		except:
			pass
	return logs


def find_logger_by_number(logger):
	global orders_rooms_logger, errors_logger
	match logger:
		case "1":
			return read_logs(orders_rooms_logger.handlers[0].baseFilename)
		case "2":
			return read_logs(errors_logger.handlers[0].baseFilename)
		case _:
			print("not ok number")
			return None


def logs_by_exact_date(logger, date):
	"""
	Find log in specific logger in specific date

	:return: List of logs
	"""
	global orders_rooms_logger, errors_logger
	logs=find_logger_by_number(logger)
	if logs == None: 
		# if there is not logger found need to raise exption
		print("not find logs/logger") 
		return
	dates=[]
	for l in logs:
		if l[1:11] == date:# if the date on the log is the date that was givin, add to list.
			dates.append(l)
	return dates


def logs_starting_on_date(logger, date):
	global orders_rooms_logger, errors_logger
	logs=find_logger_by_number(logger)
	if logs == None: print("not find logs/logger")
	dates=[]
	for l in logs:
		if datetime.strptime(l[1:11], "%Y-%m-%d") >= datetime.strptime(date, "%Y-%m-%d"):
			dates.append(l)
	return dates


def setup_logging_system():
	global orders_rooms_logger, errors_logger
	orders_rooms_logger=create_logger("orders_rooms", ".\database\orders_rooms.log")
	errors_logger=create_logger("errors", ".\database\errors.log")
	add_new_levels()

# log.order_or_room_log(ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "value" ],ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "msg" ]%"0000055555")
# for k,v in ORDERS_LOGGER_LEVELS.items():
# order_or_room_log(v["value"],v["msg"])
# for l in logs_by_date("2022-05-01"):
# 	print(l)
