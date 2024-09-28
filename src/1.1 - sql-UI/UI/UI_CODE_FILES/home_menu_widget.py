from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from .list_dialog import List_Dialog
from models import *
from models.dialogs.popup_msg import MSG_Popup


class Home_Menu_Widget(QWidget):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Home_Menu_Widget, self).__init__()
        loadUi("UI/UI_Files/home_menu_widget.ui", self)  # load the UI of the page
        self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget

        ############### buttons section #############
        self.new_order_button.clicked.connect(self.new_order_function)  # click event to the new order button
        self.rooms_button.clicked.connect(self.rooms_function)  # click event to the rooms button

        self.search_order_button.clicked.connect(self.search_order_function)  # click event to the search order button

    #############################################

    def new_order_function(self):
        # start when click on the new-order button
        self.widget.setCurrentIndex(windows_indexes["new-order"])

    def rooms_function(self):
        # start when click on the rooms button
        self.widget.widget(windows_indexes["rooms-view"]).refresh_rooms_status()
        self.widget.setCurrentIndex(windows_indexes["rooms-view"])

    def search_order_function(self):
        # start when click on the search-order button
        text_to_search = self.search_order_line_edit.text()
        finds_orders = ()
        if text_to_search.isnumeric():
            finds_orders = get_order_from_db_by_id(
                order_id=text_to_search.zfill(8))  # if the user enter a number send if to the search function
            search_type = "NUMBER"
        elif text_to_search.isalpha():
            finds_orders = get_order_from_db_by_customer_name(
                customer_name=text_to_search)  # if the user enter a plain text send if to the search function
            search_type = "TEXT"
        else:
            MSG_Popup(
                "You need to enter name or order number to search").exec_()  # else, show popup msg telling the user that he need to enter text/number
            return "You need to enter name or order number to search"
        status_code,orders=finds_orders[0],finds_orders[1]

        if status_code == ERROR_CODE:
            text_to_msg = f"Can't find orders with the name:{text_to_search}" if search_type == "TEXT" else f"Can't find order number:{text_to_search}"
            MSG_Popup(text_to_msg).exec_()  # show poopup msg
            return text_to_msg
        elif status_code == MULTI_ORDERS:
            dialog_list = List_Dialog(self.widget, orders,
                                      text_to_search)  # create list dialog with the customer orders
            dialog_list.exec_()
        elif status_code == OK_CODE:
            self.widget.widget(windows_indexes["view-order"]).set_order_to_display(orders[0])
            self.widget.widget(windows_indexes[
                                   "view-order"]).display_order()  # run the function that put the data in the ui in view_order_widget
            self.search_order_line_edit.setText("")  # clear search line
            self.widget.setCurrentIndex(windows_indexes["view-order"])  # go to view order widget that display the order
