from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QPushButton
from PyQt5.uic import loadUi

from models import *
from models.dialogs.popup_msg import MSG_Popup
from models.dialogs.dialog_msg import MSG_Dialog
from .room_dates_catch_dialog import Dates_Catch_Dialog
from .new_room_dialog import New_Room_Dialog

class Room_View_Widget(QWidget):

    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Room_View_Widget, self).__init__()
        loadUi("UI/UI_Files/rooms_view_widget.ui", self)  # load the UI of the page
        self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget

        self.rooms_widget.addWidget(self.create_titles_frame())
        self.home_btn.clicked.connect(self.home)
        self.new_room_btn.clicked.connect(self.new_room)

    def home(self):
        """

		Go back to home page after clear the page from the current order that display
		"""
        self.clear_rooms_table()

        self.widget.setCurrentIndex(windows_indexes["home-menu"])  # return to home menu

    def new_room(self):
        """Create a new room and add it to the table"""

        new_room_dialog = New_Room_Dialog()
        new_room_dialog.exec_()
        if new_room_dialog.capacity < 1 or new_room_dialog.capacity > 15:
            return
        create_room_in_db(new_room_dialog.capacity)
        self.refresh_rooms_status()

    def clear_rooms_table(self):

        for i in reversed(range(1, self.rooms_widget.count())):
            self.rooms_widget.itemAt(i).widget().setParent(None)

    def refresh_rooms_status(self):
        self.clear_rooms_table()
        try:
            rooms = get_rooms_from_db()
            for r in rooms:
                self.rooms_widget.addWidget(self.create_room_frame(r))
        except Exception as e:
            print(e)

    def create_titles_frame(self):

        title_style = ("border-radius:15px;\n"

                       "font-size:21px;\n"

                       "background-color:rgba(13, 153, 255,0.4);\n"

                       "color: rgb(255, 255, 255);\n"

                       "\n"

                       "border:2px solid  rgb(255, 255, 255);\n"

                       "border-radius:10px;")

        frame_titles = QFrame(self)
        frame_titles.setFixedHeight(70)
        frame_titles.setFixedWidth(1280)
        number_title = QLabel(self)
        number_title.setGeometry(0, 10, 150, 50)

        number_title.setStyleSheet(title_style)

        number_title.setText("Room number")

        number_title.setObjectName("number_title")

        number_title.setParent(frame_titles)

        number_title.setAlignment(Qt.AlignCenter)

        capacity_title = QtWidgets.QLabel(self)

        capacity_title.setGeometry(170, 10, 150, 50)

        capacity_title.setStyleSheet(title_style)

        capacity_title.setText("Room capacity")

        capacity_title.setObjectName("capacity_title")

        capacity_title.setParent(frame_titles)

        capacity_title.setAlignment(Qt.AlignCenter)

        now_status_title = QtWidgets.QLabel(self)

        now_status_title.setGeometry(350, 10, 200, 50)

        now_status_title.setStyleSheet(title_style)

        now_status_title.setText("Room status(NOW)")

        now_status_title.setObjectName("now_status_title")

        now_status_title.setParent(frame_titles)

        now_status_title.setAlignment(Qt.AlignCenter)

        cleanning_status_title = QtWidgets.QLabel(self)

        cleanning_status_title.setGeometry(580, 10, 230, 50)

        cleanning_status_title.setStyleSheet(title_style)

        cleanning_status_title.setText("Room cleanning satus")

        cleanning_status_title.setObjectName("cleanning_status_title")

        cleanning_status_title.setParent(frame_titles)

        cleanning_status_title.setAlignment(Qt.AlignCenter)

        faults_title = QtWidgets.QLabel(self)

        faults_title.setGeometry(840, 10, 130, 50)

        faults_title.setStyleSheet(title_style)

        faults_title.setText("Room faults")

        faults_title.setObjectName("faults_title")

        faults_title.setParent(frame_titles)

        faults_title.setAlignment(Qt.AlignCenter)

        dates_catch_title = QtWidgets.QLabel(self)

        dates_catch_title.setGeometry(1000, 10, 240, 50)

        dates_catch_title.setStyleSheet(title_style)

        dates_catch_title.setText("Dates the room is catch")

        dates_catch_title.setObjectName("dates_catch_title")

        dates_catch_title.setParent(frame_titles)

        dates_catch_title.setAlignment(Qt.AlignCenter)

        return frame_titles

    def create_room_frame(self, room=None):
        if room is None:
            return None
        feild_style = ("border-radius:15px;\n"
                       "font-size:21px;\n"
                       "background-color:rgb(48, 120, 200);\n"
                       "color: rgb(255, 255, 255);\n"
                       "\n"
                       "border:2px solid  rgb(255, 255, 255);\n"
                       "border-radius:10px;")

        room_frame = QFrame(self)
        room_frame.setFixedHeight(60)
        room_frame.setFixedWidth(1280)

        number_room = QLabel(room_frame)
        number_room.setGeometry(0, 0, 150, 50)
        number_room.setStyleSheet(feild_style)
        number_room.setText(str(room[0]))
        number_room.setObjectName("room_number")
        number_room.setAlignment(Qt.AlignCenter)

        capacity_room = QLabel(room_frame)
        capacity_room.setGeometry(170, 0, 150, 50)
        capacity_room.setStyleSheet(feild_style)
        capacity_room.setText(str(room[1]))
        capacity_room.setObjectName("room_capacity")
        capacity_room.setAlignment(Qt.AlignCenter)

        now_status_room = QLabel(room_frame)
        now_status_room.setGeometry(350, 0, 200, 50)
        now_status_room.setStyleSheet(feild_style)
        now_status_room.setText(str(room[2]))
        now_status_room.setObjectName("room_now_status")
        now_status_room.setAlignment(Qt.AlignCenter)

        cleanning_status_room = QLabel(room_frame)
        cleanning_status_room.setGeometry(580, 0, 230, 50)
        cleanning_status_room.setStyleSheet(feild_style)
        cleanning_status_room.setText(str(room[3]))
        cleanning_status_room.setObjectName("room_cleanning_status")
        cleanning_status_room.setAlignment(Qt.AlignCenter)

        faults_room = QPushButton(room_frame)
        faults_room.setGeometry(840, 0, 130, 50)
        faults_room.setStyleSheet(feild_style)
        faults_room.setIcon(QIcon(QPixmap('UI/ICONS/alert.png')))
        faults_room.setIconSize(QSize(30, 30))
        faults_room.setObjectName("room_faults")
        faults_room.clicked.connect(lambda: self.show_faults(room[0]))

        dates_catch_room = QPushButton(room_frame)
        dates_catch_room.setGeometry(1000, 0, 240, 50)
        dates_catch_room.setStyleSheet(feild_style)
        dates_catch_room.setIcon(QIcon(QPixmap('UI/ICONS/calendar.png')))
        dates_catch_room.setIconSize(QSize(30, 30))
        dates_catch_room.setObjectName("room_dates_catch")
        dates_catch_room.clicked.connect(lambda: self.show_dates_catch(room[0]))

        btn_style = """
		QPushButton:hover {
			background:   rgb(48, 120, 200);
		}
		QPushButton{
			border-radius:15px;
			background: rgba(35, 130, 220,0.4);
		}
		"""
        delete_room_btn = QtWidgets.QPushButton(room_frame)
        delete_room_btn.setGeometry(1250, 10, 30, 30)
        delete_room_btn.setStyleSheet(btn_style)
        delete_room_btn.setIcon(QIcon(QPixmap('UI/ICONS/close.png')))
        delete_room_btn.setIconSize(QSize(20, 20))
        delete_room_btn.setObjectName("delete_room_btn")
        delete_room_btn.clicked.connect(lambda: self.delete_room(room[0]))

        return room_frame

    # -------------------------clicked event functions-------------------------

    def delete_room(self, room_number):
        delete_status = MSG_Dialog(f"Delete room number {room_number}", "Yes",
                                   "No")  # Check if the user really wants to delete the room
        delete_status.exec()
        if delete_status.status == "Yes":  # If the user really wants to delete the room
            room_dates = get_date_range_by_room_id_db(room_number=room_number)
            if len(room_dates) > 0:  # Check if the the room is not booked
                MSG_Popup("The room is reserved for future bookings, you can't delete it").exec()
                return
            delete_room_db(room_number)
            self.refresh_rooms_status()

    def show_dates_catch(self, room_number):
        room_dates_catch_list = get_date_range_by_room_id_db(room_number=room_number)
        if len(room_dates_catch_list) > 0:
            date_dialog = Dates_Catch_Dialog(room_number, room_dates_catch_list)
            date_dialog.exec()
        else:
            MSG_Popup("The room does not catch").exec_()

    def show_faults(self, room_number):
        room_faults_list = get_room_faults_from_db(room_number=room_number)
        if len(room_faults_list) > 0:
            MSG_Popup(room_faults_list[0][1]).exec_()
        else:
            MSG_Popup("The room have no faults").exec_()
