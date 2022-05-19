import logging

from .logs_levels import *

orders_rooms_logger=None
errors_logger=None


def create_logger( name, log_file, level=logging.INFO):
	formatter = logging.Formatter('[%(asctime)s] || %(levelname)s || %(message)s')
	
	heandler = logging.FileHandler(log_file)
	heandler.setFormatter(formatter)
	
	logger = logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(heandler)
	
	return logger


def create_log_order_room(level_value, msg):
	global orders_rooms_logger
	orders_rooms_logger.log(level_value, msg)


def add_new_levels():
	for k, v in ORDERS_LOGGER_LEVELS.items():
		logging.addLevelName(v [ "value" ], v [ "name" ])
	for k, v in ROOMS_LOGGER_LEVELS.items():
		logging.addLevelName(v [ "value" ], v [ "name" ])


def read_logs(file):
	with open("orders_rooms.log", "r") as f:
		logs = f.read()
		logs = logs.split("\n")
		try:
			logs.remove('')
		except:
			pass
	return logs


def logs_by_date( date):
	logs = read_logs("../../orders_rooms.log")
	dates = [ ]
	for l in logs:
		if l [ 1:11 ] == date:
			dates.append(l)
	return dates


def setup_logging_system():
	global orders_rooms_logger,errors_logger
	orders_rooms_logger = create_logger("orders_rooms", "database/orders_rooms.log")
	errors_logger = create_logger("errors", "database/errors.log")
	add_new_levels()

# log.order_or_room_log(ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "value" ],ORDERS_LOGGER_LEVELS [ "order-check-in" ] [ "msg" ]%"0000055555")
# for k,v in ORDERS_LOGGER_LEVELS.items():
# order_or_room_log(v["value"],v["msg"])
# for l in logs_by_date("2022-05-01"):
# 	print(l)

