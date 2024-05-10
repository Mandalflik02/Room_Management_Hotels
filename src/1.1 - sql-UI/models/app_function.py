import re
import sqlite3
from datetime import date

from Logs import *
from global_ver import *
from order import Order
# from .room import Room
from range_of_dates import Dates_Range, create_range

#################################### Setup Database ####################################
def create_DB():
    DB_CURSER.execute("DROP TABLE IF EXISTS rooms")
    DB_CURSER.execute("DROP TABLE IF EXISTS rooms_faults")
    DB_CURSER.execute("DROP TABLE IF EXISTS dates_range")
    DB_CURSER.execute("DROP TABLE IF EXISTS orders")
    res = DB_CURSER.execute("select name from sqlite_master where type='table'")
    print(res.fetchall())
    DB_CURSER.execute(
        """CREATE TABLE IF NOT EXISTS rooms(room_number INTEGER PRIMARY KEY AUTOINCREMENT,
        room_capacity INTEGER not null,
        room_is_catch bool DEFAULT 0  check(room_is_catch in (0,1)),
        room_is_clean bool DEFAULT 0  check(room_is_clean in (0,1)))"""
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
        """CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name text not null,
        number_of_guests integer not null,
        room_number integer not null,
        breackfast bool check(breackfast in (0,1)), 
        lunch bool check(lunch in (0,1)), 
        diner bool check(diner in (0,1)), 
        electric_car bool check(electric_car in (0,1)), 
        pet bool check(pet in (0,1)), 
        check_in bool DEFAULT 0 check(check_in in (0,1)), 
        check_out bool DEFAULT 0 check(check_out in (0,1)),
        create_time text not null,
        create_by text not null)"""
    )

#################################### Get data from DB ####################################
def get_room_faults_from_db(room_number):
    res = DB_CURSER.execute(
        "SELECT * FROM rooms_faults WHERE room_number = %s " % room_number
    )
    return res.fetchall()

#################################### Insert data to DB ####################################
def create_date_range_in_db(order_id, room_number, date_range):
    """create a date range in the date_range table for the room and order"""
    DB_date_range = [
        order_id,
        room_number,
        date_range.get_arrival_date(),
        date_range.get_leaving_date(),
    ]
    res = DB_CURSER.execute("INSERT INTO dates_range VALUES(?,?,?,?)", DB_date_range)
    return res.fetchall()

def create_order_in_db(order_info):
    # order_info = [
    #     datetime.now().strftime("%H:%M:%S , %d/%m/%Y"),
    #     "Admin",
    #     order.get_customer_name(),
    #     order.get_guests_num(),
    #     int(order.get_meal_options()[0]),
    #     int(order.get_meal_options()[1]),
    #     int(order.get_meal_options()[2]),
    #     order.get_electric_car(),
    #     order.get_pet(),
    #     order.get_room_number(),
    # ]
    DB_CURSER.execute(
        """INSERT INTO orders (customer_name,number_of_guests,room_number, breackfast ,lunch ,diner ,electric_car ,pet ,create_time ,create_by ) 
        VALUES(?,?,?,?,?,?,?,?,?,?)""",
        order_info,
    )
    return DB_CURSER.lastrowid

def create_room_in_db(room_capacity):
    return DB_CURSER.execute(
        "INSERT INTO rooms (room_capacity) VALUES(?)", [room_capacity]
    ).fetchall()

#################################### Side functions ####################################

def search_room_by_number(room_number):
    for r in ROOMS:
        # go over all the room and search the room with the number the function get
        if r.get_room_number() == room_number: return r

def print_one_or_more_order(order: Order = None):
    try:
        for o in order: print(o)
    except:
        print(order)

def search_order_in_database(name: str = "", id: str = "00000000"):
    orders_filtered = []
    for o in ORDERS:
        # if the customer in the order is the one I look for add to list
        if o.get_customer_name() == name or o.get_order_id() == id:
            orders_filtered.append(o)
    return orders_filtered  # return list with all the orders

def search_order(customer_name="", order_id="00000000"):
    try:
        orders_filtered = search_order_in_database(customer_name, order_id)  # search order by customer name or order ID
        if len(orders_filtered) != 0:
            return orders_filtered
    except Exception as e:
        print("An Error search order in database", e)

def move_order_to_history(order: Order = None):
    ORDERS_HISTORY.append(order)

#################################### Menu options ####################################

# ====================================================section 11 - add new room fault====================================================
def add_new_room_fault(room_number, fault):
    DB_CURSER.execute("INSERT INTO rooms_faults VALUES(?,?)", [room_number, fault])

# ========================================================================================================================================

# ====================================================section 10 - delete order====================================================
# ==================================================================================================================================

# ====================================================section 9 - LOGS====================================================
# =========================================================================================================================

# ====================================================section 7 - check-out====================================================
# ==============================================================================================================================

# ====================================================section 6 - check-in====================================================
# =============================================================================================================================

# ====================================================section 5 - get rooms====================================================
# ==============================================================================================================================

# ====================================================section 4 - get orders====================================================
# ===============================================================================================================================

# ====================================================section 3 - add new room====================================================
def create_room_in_db(room_capacity: int):
    return DB_CURSER.execute("INSERT INTO rooms (room_capacity) VALUES(?)", [room_capacity]).fetchall()
# =================================================================================================================================

# ====================================================section 2 - update order====================================================
# =================================================================================================================================

# ====================================================section 1 - add new order====================================================
def search_available_room(guests_num, date_range):
    rooms_available = DB_CURSER.execute(
        """SELECT DISTINCT r.room_number,r.room_capacity
        FROM rooms r
        WHERE r.room_capacity >= ? 
        AND NOT EXISTS(
            SELECT 1
            FROM rooms_faults rf
            WHERE rf.room_number = r.room_number
        )
        AND NOT EXISTS (
            SELECT 1
            FROM dates_range dr
            WHERE dr.room_number = r.room_number
            AND dr.start_date <= ? 
            AND dr.end_date >= ?
    )""",
        (guests_num, date_range.get_arrival_date(), date_range.get_leaving_date()),
    )
    rooms_available = rooms_available.fetchall()
    if len(rooms_available) > 0:
        smallest_room = min(rooms_available, key=lambda x: x[0])
        return smallest_room[0]
    return 0

def create_new_order(customer_name: str = None, guests: int = None, meal_options: str = None, electric_car: bool = None,
                     pet: bool = None, arrival_date: str = None, leaving_date: str = None):
    """
    Get data of the order and create new one and add to the ORDERS list

    :return: Error if there is one
    """
    if (
            customer_name == None or guests == None or meal_options == None or electric_car == None or pet == None or arrival_date == None or leaving_date == None):
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
            int(meal_options[0]),
            int(meal_options[1]),
            int(meal_options[2]),
            electric_car,
            pet,
            datetime.now().strftime("%H:%M:%S , %d/%m/%Y"),
            "Admin",
        ]
        order_id = create_order_in_db(order_info)
        # customer_name,number_of_guests,room_number, breackfast ,lunch ,diner ,electric_car ,pet ,create_time ,create_by
        # execute the create order with the relevent data (not create object) and then get the order id from the db
        create_date_range_in_db(
            order_id, room, order_dates_range
        )  # create date-range for room and order

        # ROOMS[ROOMS.index(room)].add_date_catch(
        #     arrival_date, leaving_date, order_id
        # )  # add date_range to the room -> range when the room is caught
        # ORDERS.append(new_order)  # add order to the orders list
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
    create_room_in_db(4)
    create_room_in_db(8)
    create_room_in_db(100)
    create_room_in_db(5)
    create_room_in_db(100)
    create_room_in_db(3)
    add_new_room_fault(3, "dooooooo")
    dr1 = Dates_Range("01/02/2024", "01/03/2024", 1)
    dr2 = Dates_Range("01/02/2024", "01/03/2024", 2)

    print(create_new_order("naor", 100, "010", 0, 1, "01/02/2024", "01/03/2024"))
    print(create_new_order("naor", 3, "010", 0, 1, "01/02/2024", "01/03/2024"))

    res = DB_CURSER.execute("PRAGMA table_info(orders)").fetchall()
    titels = [t[1] for t in res]
    print(titels)

    res = DB_CURSER.execute("SELECT * FROM orders ")
    for o in res.fetchall():
        print(o)

if __name__ == '__main__':
    Test()
