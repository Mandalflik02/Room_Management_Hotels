import re
import random


from Logs import *
from global_ver import *
from order import Order
# from .room import Room
from range_of_dates import Dates_Range, create_range

#################################### Setup Database ####################################
def create_DB():
    # DB_CURSER.execute("DROP TABLE IF EXISTS rooms")
    # DB_CURSER.execute("DROP TABLE IF EXISTS rooms_faults")
    # DB_CURSER.execute("DROP TABLE IF EXISTS dates_range")
    # DB_CURSER.execute("DROP TABLE IF EXISTS orders")

    DB_CURSER.execute(
        """CREATE TABLE IF NOT EXISTS rooms(room_number SERIAL  PRIMARY KEY,
        room_capacity INTEGER not null,
        room_is_catch bool DEFAULT false  check(room_is_catch in (false,true)),
        room_is_clean bool DEFAULT false  check(room_is_clean in (false,true)))"""
    )
    DB_CURSER.execute(
        """CREATE TABLE IF NOT EXISTS  rooms_faults(room_number INTEGER,
        fault text not null)"""
    )
    DB_CURSER.execute(
        """CREATE TABLE IF NOT EXISTS  dates_range(order_id INTEGER PRIMARY KEY,
        room_number INTEGER,
        start_date text not null,
        end_date text not null)"""
    )
    DB_CURSER.execute(
        """CREATE TABLE IF NOT EXISTS orders(id SERIAL  PRIMARY KEY,
        customer_name text not null,
        number_of_guests integer not null,
        room_number integer not null,
        breackfast bool check(breackfast in (false,true)), 
        lunch bool check(lunch in (false,true)), 
        diner bool check(diner in (false,true)), 
        electric_car bool check(electric_car in (false,true)), 
        pet bool check(pet in (false,true)), 
        check_in bool DEFAULT false check(check_in in (false,true)), 
        check_out bool DEFAULT false check(check_out in (false,true)),
        create_time text not null,
        create_by text not null)"""
    )
    DB_CON.commit()

#################################### Get data from DB ####################################
def get_order_from_db(order_id: int = -1):
    if order_id == -1:
        return ERROR_CODE, "ORDER_ID can't be -1"
    sql = DB_CURSER.mogrify("""
        SELECT * FROM orders WHERE id = %s
    """ % str(order_id))
    DB_CURSER.execute(sql)
    order = DB_CURSER.fetchone()
    if order == None:
        return [ERROR_CODE, f"ORDER_ID --{order_id}-- not exsist"]
    return order

def get_order_from_db_by_customer_name(customer_name: str = ""):
    if customer_name == "":
        return ERROR_CODE, "customer_name can't be empty"
    sql = DB_CURSER.mogrify("""
        SELECT * FROM orders WHERE customer_name = %s
    """, customer_name)
    DB_CURSER.execute(sql)
    order = DB_CURSER.fetchall()
    if order == []:
        return [ERROR_CODE, f"CUSTOMER_NAME {customer_name} not exsist"]
    return order

def get_room_from_db(room_number: int = -1):
    if room_number == -1:
        return ERROR_CODE, "ROOM_NUMBER can't be -1"
    sql = DB_CURSER.mogrify("SELECT * FROM rooms WHERE room_number = %s" % str(room_number))
    DB_CURSER.execute(sql)
    room = DB_CURSER.fetchone()
    if room == None:
        return [ERROR_CODE, f"room --{room_number}-- dosn't exsist"]
    return room

#################################### Insert data to DB ####################################
def create_date_range_in_db(order_id, room_number, date_range):
    """create a date range in the date_range table for the room and order"""
    check_date_range_for_order = DB_CURSER.mogrify(""" select * from dates_range where order_id = %s""" % str(order_id))
    DB_CURSER.execute(check_date_range_for_order)
    check_date_range_for_order = DB_CURSER.fetchone()
    if check_date_range_for_order != None:
        return [ERROR_CODE, f"date_range from order:{order_id} exsis --> {check_date_range_for_order}"]
    date_range_to_db = [
        order_id,
        room_number,
        date_range.get_arrival_date(),
        date_range.get_leaving_date(),
    ]
    sql = DB_CURSER.mogrify("INSERT INTO dates_range VALUES(%s,%s,%s,%s)", date_range_to_db)
    DB_CURSER.execute(sql)
    return OK_CODE,f"Date range for order {order_id} created: {date_range.get_arrival_date()} - {date_range.get_leaving_date()}"
def create_order_in_db(order_info):
    sql = DB_CURSER.mogrify(
        """INSERT INTO orders (customer_name,number_of_guests,room_number, breackfast ,lunch ,diner ,electric_car ,pet ,create_time ,create_by ) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id""",
        order_info,
    )
    DB_CURSER.execute(sql)
    return DB_CURSER.fetchone()[0]

def create_room_in_db(room_capacity):
    sql = DB_CURSER.mogrify("INSERT INTO rooms (room_capacity) VALUES(%s)", room_capacity)
    DB_CURSER.execute(sql)
    return DB_CURSER.fetchall()

#################################### Side functions ####################################

def move_order_to_history(order: Order = None):
    ORDERS_HISTORY.append(order)

#################################### Menu options ####################################

# ====================================================section 11 - add new room fault====================================================
def add_new_room_fault(room_number, fault):
    sql = DB_CURSER.mogrify("INSERT INTO rooms_faults VALUES(%s,%s)", [room_number, fault])
    DB_CURSER.execute(sql)

# ========================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 10 - delete order====================================================
def delete_date_range_from_db_by_order(order_id: int = -1):
    if order_id == -1:
        return ERROR_CODE, "ORDER_ID can't be -1"
    sql = DB_CURSER.mogrify("""
        DELETE FROM dates_range WHERE order_id = %s
    """ % str(order_id))
    DB_CURSER.execute(sql)

def delete_order_from_db_by_id(delete_code: int = 0, order_id: int = -1):
    # try:
    if delete_code != DELETE_CODE:  # Must have a delete code to confirm the delete
        return ERROR_CODE, f"Error -> Delete code not mach : {delete_code}"
    if order_id == -1:
        return ERROR_CODE, "ORDER_ID can't be -1"
    order = get_order_from_db(order_id)  # Search the order
    if type(order) == type([]):
        return order
    delete_date_range_from_db_by_order(order_id=order_id)
    sql = DB_CURSER.mogrify("""
            DELETE FROM orders WHERE id = %s
        """ % str(order_id))
    DB_CURSER.execute(sql)

    move_order_to_history(order)  # Add the order to history
    create_log_order_room(ORDERS_LOGGER_LEVELS["order-deleted"]["value"],
                          ORDERS_LOGGER_LEVELS["order-deleted"]["msg"] % (
                              order_id, CURRENT_USER))  # log the delete of the order
    return OK_CODE, f"Order number {order_id} deleted (siil live in history)"
    # except Exception as e:
    #     return ERROR_CODE, f"Error -> {e}"

# ==================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 9 - LOGS====================================================
# =========================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 7 - check-out====================================================
# ==============================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 6 - check-in=====================================================


def check_in(order_id: int=-1):
	try:
        check_in_q = DB_CURSER.mogrify("""select check_in from orders where id = %s"""% order_id)
        DB_CURSER.execute(check_in_q)
        order_check_in_status = DB_CURSER.fetchone()
		if not order_check_in_status and not order.get_check_out_status():
			today =date.today().strftime("%d/%m/%Y")
			if today >= order.get_arrival_date() and today < order.get_leaving_date():
				pass
			else:
				return False,"Can't be checked-in not between arrival and leaving dates"
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


# =============================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 5 - get rooms====================================================
def get_room_faults_from_db(room_number):
    res = DB_CURSER.execute(
        "SELECT * FROM rooms_faults WHERE room_number = %s " % room_number
    )
    return res.fetchall()

# =============================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 4 - get orders====================================================
# add view in the app to view all orders
# ==============================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 3 - add new room====================================================
def create_room_in_db(room_capacity: int):
    res = DB_CURSER.execute("INSERT INTO rooms (room_capacity) VALUES(%s)" % room_capacity)
    if res != None:
        return res.fetchall()
    return True

# =================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 2 - update order====================================================
# =================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# ====================================================section 1 - add new order====================================================
def search_available_room(guests_num, date_range):
    sql = DB_CURSER.mogrify("""SELECT r.room_number,r.room_capacity
        FROM rooms r
        LEFT JOIN rooms_faults rf ON r.room_number = rf.room_number
        LEFT JOIN dates_range dr ON r.room_number = dr.room_number
        WHERE r.room_capacity >= %s 
        AND (dr.start_date IS NULL OR dr.end_date IS NULL
            OR (dr.start_date > %s OR dr.end_date < %s))
        AND rf.room_number IS NULL;
    """, (guests_num, date_range.get_arrival_date(), date_range.get_leaving_date()))
    DB_CURSER.execute(sql)
    rooms_available = DB_CURSER.fetchall()
    if len(rooms_available) > 0:
        smallest_room = min(rooms_available, key=lambda x: x[0])
        return smallest_room[0]
    return 0

def create_new_order_in_db(customer_name: str = None, guests: int = None, breackfast: bool = False, lanch: bool = False,
                     diner: bool = False, electric_car: bool = False,
                     pet: bool = False, arrival_date: str = None, leaving_date: str = None):
    """
    Get data of the order and create new one and add to the ORDERS list

    :return: Error if there is one
    """
    if (
            customer_name == None or guests == None or arrival_date == None or leaving_date == None):
        return VERABLE_ERROR_CODE, "Please fill all the fields"
    try:
        # print("------------------Start create order------------------")
        if guests < 1:  # check if the guests number is ok
            return VERABLE_ERROR_CODE, "Can be 0 guests"
        order_dates_range = create_range(
            arrival_date, leaving_date
        )  # create date range for the order
        if order_dates_range is None:  # check the dates range was created
            return VERABLE_ERROR_CODE, "Cannot create a date range"
        if (
                not order_dates_range.range_ok
        ):  # check if there is a error in the date range
            return order_dates_range.error_text
        room = search_available_room(
            guests, order_dates_range
        )  # look for available room
        if room == 0:
            return ROOM_ERROR_CODE, "No room available"
        # room_num = room.get_room_number()  # get room number
        # customer_exist_orders = search_order(customer_name=customer_name)
        # if type(customer_exist_orders) is list and len(customer_exist_orders) >= 3:
        #     return MAX_ORDERS_CODE, "The customer have 3 order and can have more"

        # create the order
        order_info = [
            customer_name,
            guests,
            room,
            breackfast,
            lanch,
            diner,
            electric_car,
            pet,
            datetime.now().strftime("%H:%M:%S , %d/%m/%Y"),
            "Admin",
        ]
        order_id = create_order_in_db(order_info)
        # customer_name,number_of_guests,room_number, breackfast ,lunch ,diner ,electric_car ,pet ,create_time ,create_by
        print(create_date_range_in_db(
            order_id, room, order_dates_range
        ))  # create date-range for room and order

        # create_log("NEW ORDER", "New order create, order ID: %s" % (order_id))
        # print("----------------Order create---------------", new_order)  # , ROOMS [ ROOMS.index(room) ])
        create_log_order_room(
            ORDERS_LOGGER_LEVELS["new-order"]["value"],
            ORDERS_LOGGER_LEVELS["new-order"]["msg"] % order_id,
        )
        # print("-------------END create order------------")
        return OK_CODE, f"Order created successfully - {order_id}"
    except KeyboardInterrupt:
        exit()
        return ERROR_CODE, "keyboard error"

# ==================================================================================================================================


def Test():
    create_DB()
    # create_room_in_db(4)
    # create_room_in_db(8)
    # create_room_in_db(100)
    # create_room_in_db(500)
    # create_room_in_db(100)
    # create_room_in_db(3)
    add_new_room_fault(random.randint(0,144), "fix it")
    dr1 = Dates_Range("01/02/2024", "01/03/2024", 1)
    dr2 = Dates_Range("01/02/2024", "01/03/2024", 2)

    # print(create_new_order_in_db(customer_name="naor", guests=2, arrival_date="01/02/2024", leaving_date="01/03/2024"))
    # print(create_new_order_in_db(customer_name="naor", guests=50, arrival_date="01/02/2024", leaving_date="01/03/2024"))
    # print(delete_order_from_db_by_id(delete_code=DELETE_CODE, order_id=12))
    # print(get_room_from_db(300))
    DB_CON.commit()
    DB_CURSER.close()
    DB_CON.close()

if __name__ == '__main__':
    Test()
