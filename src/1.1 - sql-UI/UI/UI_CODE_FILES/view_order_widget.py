from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi

from models import *
from models.dialogs.dialog_msg import MSG_Dialog

class View_Order_Widget(QWidget):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(View_Order_Widget, self).__init__()
        loadUi("UI/UI_Files/view_order_widget.ui", self)  # load the UI of the page
        self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget
        self.order_id = None

        self.check_in_status = False
        self.check_out_status = False

        self.check_in_btn.clicked.connect(self.check_in_order)
        self.check_out_btn.clicked.connect(self.check_out_order)
        self.delete_btn.clicked.connect(self.delete_order)
        self.update_btn.clicked.connect(self.update_order)
        self.home_btn.clicked.connect(self.home)

    def check_in_order(self):
        """
        Change the status of check-in for the order after ask the user in dialog
        """
        msg_label = "Check-in customer??" if not self.check_in_status else "Cancel check-in customer??"
        q = MSG_Dialog(msg_label, "Yes", "No")  # ask the user he want to check-in/undo the check-in for this order
        q.exec_()
        if q.status == "No":
            return
        self.check_in_status = not self.check_in_status  # change the status of check-in in the UI variable
        try:
            if self.check_in_status:
                # if the check-in status is True that mean the user is click to check-in the order
                error = check_in_db(order_id=self.order_id)  # tupel of (check-in status,error)
                if error[0]:
                    # if no error check-in the customer
                    self.change_btn_color(self.check_in_btn, self.check_in_status)  # add color to button
                else:
                    # if there is a error when try to check-in
                    self.check_in_status = not self.check_in_status  # return the value to what was before the function
                    MSG_Popup(error[1]).exec_()  # show the error in popup msg
            # print(error[1])
            else:
                # if the check-in status is False that mean the user is click to cencel check-in the order
                if cancel_check_in_db(order_id=self.order_id)[0] == OK_CODE:
                    self.change_btn_color(self.check_in_btn, self.check_in_status)  # cencel the color of the button
                else:
                    # if the user is already check-out
                    self.check_in_status = not self.check_in_status  # return the value to what was before the function
                    MSG_Popup("The customer is already check out!!").exec_()
        # print("The customer is already check out!!")
        except Exception as e:
            print("check-in in widget", e)

    def check_out_order(self):
        """
        Change the status of check-out for the order after ask the user in dialog
        """
        msg_label = "Check-out customer and close order??" if not self.check_out_status else "Cancel check-out customer??"
        q = MSG_Dialog(msg_label, "Yes", "No")  # ask the user if he want to check-out/undo check-out for this order
        q.exec_()
        if q.status == "No":
            return
        self.check_out_status = not self.check_out_status  # change the status of check-out in the UI variable
        try:
            if self.check_out_status:
                # if the check-out status is True that mean the user is click to check-out the order
                error = check_out_db(order_id=self.order_id)  # tupel of (check-out status,error)
                if error[0]:
                    # if no error check-in the customer
                    self.change_btn_color(self.check_out_btn, self.check_out_status)  # add color to button
                    self.home()
                else:
                    # if there is a error when try to check-out
                    self.check_out_status = not self.check_out_status  # return the value to what was before the function
                    MSG_Popup(error[1]).exec_()  # show the error in popup msg
            # print(error[1])
            else:
                # if the check-out status is False that mean the user is click to cencel check-out the order
                cancel_check_out_db(order_id=self.order_id)
                self.change_btn_color(self.check_out_btn, self.check_out_status)  # cencel the color of the button

        except Exception as e:
            print("check-out in widget", e)

    def change_btn_color(self, btn, status):
        """
        Change the color of the button depend on his status (click/unclick)
        """
        style = """
					QPushButton:hover {
						background-color: rgb(10, 123, 204);
					}
					QPushButton{
						font: 18pt "Calibri";
						border-radius:15px;
						border-radius:10px;
						color: rgb(255, 255, 255);
						border:2px solid  rgb(255, 255, 255);
				"""  # the basic style for the button
        if status:
            style += """	background: rgb(10, 123, 204);	"""  # add background color when the status is true
        style += """	}	"""  # close style
        btn.setStyleSheet(style)  # set the style sheet for the button

    def delete_order(self):
        """
        Remove the order from the ORDERS list and go back to home page
        """
        delete_status = MSG_Dialog("Delete the order", "Yes", "No")
        delete_status.exec_()
        if delete_status.status == "No":
            return
        delete_status = delete_order_from_db_by_id(delete_code=DELETE_CODE, order_id=self.order_id)
        if delete_status[0] == ERROR_CODE:
            MSG_Popup(delete_status[1]).exec_()
            return
        MSG_Popup(delete_status[1]).exec_()
        self.home()

    def update_order(self):
        self.clear_ui()
        self.widget.widget(windows_indexes["update-order"]).set_order_id(self.order_id)
        self.widget.setCurrentIndex(windows_indexes["update-order"])  # return to home menu

    def home(self):
        """
        Go back to home page after clear the page from the current order that display
        """
        self.clear_ui()
        self.widget.setCurrentIndex(windows_indexes["home-menu"])  # return to home menu

    def clear_ui(self):
        """
        Clear the UI object -> set the text to defualt
        """
        self.order_id_label.setText("View order: ")
        self.created_by_label.setText("Order created by:")
        self.creation_date_label.setText("Order creation date: ")
        self.customer_name_label.setText("Customer name: ")
        self.adults_label.setValue(0)
        self.arrivel_label.setText("")
        self.leaving_label.setText("")
        order_widget_labels = [self.electric_car_label,
                               self.pet_label,
                               self.breakfast_label,
                               self.lunch_label,
                               self.dinner_label]
        for label in order_widget_labels:
            label.setPixmap(QPixmap('UI/ICONS/unchecked.png'))

    def display_order(self):
        """
        Put the data from the order in the UI objects
        """
        order = get_order_from_db_by_id(self.order_id)
        orders_dates = get_start_and_end_dates(self.order_id)
        print(order)
        print(orders_dates)
        self.order_id_label.setText(f"View order: {order[0]}")
        self.created_by_label.setText(f"Order created by: {order[12]}")
        self.creation_date_label.setText(f"Order creation date: {order[11]}")
        self.customer_name_label.setText(f"Customer name: {order[1]}")
        self.adults_label.setValue(order[2])
        self.arrivel_label.setText(f"{orders_dates[0]}")
        self.leaving_label.setText(f"{orders_dates[0]}")
        order_vars_and_widget_labels = [(order[7], self.electric_car_label),
                                        (order[8], self.pet_label),
                                        (order[4], self.breakfast_label),
                                        (order[5], self.lunch_label),
                                        (order[6], self.dinner_label)]
        for order_stat in order_vars_and_widget_labels:
            if order_stat[0] == True:
                order_stat[1].setPixmap(QPixmap('UI/ICONS/checked.png'))
            else:
                order_stat[1].setPixmap(QPixmap('UI/ICONS/unchecked.png'))

    def set_order_to_display(self, order_id=-1):
        """
        Function that set the order variable for the widget

        :param order_to_display: The order you want to display
        :type order_to_display: Order
        """
        if order_id == -1:
            return ERROR_CODE, " Order ID can't be -1"
        self.order_id = order_id

# results = [t [ 1 ].setPixmap(QPixmap('UI/ICONS/checked.png')) if  t [ 0 ] == True else t [ 1 ].setPixmap(QPixmap('UI/ICONS/unchecked.png')) for t in order_vars_and_widget_labels]
