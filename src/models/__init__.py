try:
    from .order import Order
    from .room import Room
    from .range_of_dates import Dates_Range,create_range
    from .global_ver import *
    from .menu_opstions import *
    from .Logs import *
    from .dialogs import *
except Exception as e:
    print("Error -> models.__init__ ->" +str(e))
    create_log_error(msg=e)