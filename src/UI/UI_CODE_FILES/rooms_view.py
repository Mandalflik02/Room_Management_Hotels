from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFrame, QLabel
from PyQt5.uic import loadUi


class Rooms_View(QWidget):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Rooms_View, self).__init__()
		loadUi("UI/UI_Files/rooms_view_widget.ui", self)  # load the UI of the page
		self.widget = widget  # the widget-stack that has all widgets --> so I can move to any other widget
		
		self.rooms_widget.addWidget(self.create_titles_frame())
	
	def create_titles_frame(self):
		title_style = ("border-radius:15px;\n"
		               "font-size:21px;\n"
		               "background-color:rgba(13, 153, 255,0.4);\n"
		               "color: rgb(255, 255, 255);\n"
		               "\n"
		               "border:2px solid  rgb(255, 255, 255);\n"
		               "border-radius:10px;")
		
		frame_titles = QFrame(self)
		frame_titles.setFixedHeight(100)
		frame_titles.setFixedWidth(1280)
		
		number_title = QLabel(self)
		number_title.setGeometry(30, 10, 150, 50)
		number_title.setStyleSheet(title_style)
		number_title.setText("Room number")
		number_title.setObjectName("number_title")
		number_title.setParent(frame_titles)
		number_title.setAlignment(Qt.AlignCenter)

		capacity_title = QtWidgets.QLabel(self)
		capacity_title.setGeometry(210, 10, 150, 50)
		capacity_title.setStyleSheet(title_style)
		capacity_title.setText("Room capacity")
		capacity_title.setObjectName("capacity_title")
		capacity_title.setParent(frame_titles)
		capacity_title.setAlignment(Qt.AlignCenter)

		now_status_title = QtWidgets.QLabel(self)
		now_status_title.setGeometry(390, 10, 200, 50)
		now_status_title.setStyleSheet(title_style)
		now_status_title.setText("Room status(NOW)")
		now_status_title.setObjectName("now_status_title")
		now_status_title.setParent(frame_titles)
		now_status_title.setAlignment(Qt.AlignCenter)

		cleanning_status_title = QtWidgets.QLabel(self)
		cleanning_status_title.setGeometry(620, 10, 230, 50)
		cleanning_status_title.setStyleSheet(title_style)
		cleanning_status_title.setText("Room cleanning satus")
		cleanning_status_title.setObjectName("cleanning_status_title")
		cleanning_status_title.setParent(frame_titles)
		cleanning_status_title.setAlignment(Qt.AlignCenter)
		
		faults_title = QtWidgets.QLabel(self)
		faults_title.setGeometry(880, 10, 130, 50)
		faults_title.setStyleSheet(title_style)
		faults_title.setText("Room faults")
		faults_title.setObjectName("faults_title")
		faults_title.setParent(frame_titles)
		faults_title.setAlignment(Qt.AlignCenter)

		dates_catch_title = QtWidgets.QLabel(self)
		dates_catch_title.setGeometry(1040, 10, 240, 50)
		dates_catch_title.setStyleSheet(title_style)
		dates_catch_title.setText("Dates the room is catch")
		dates_catch_title.setObjectName("dates_catch_title")
		dates_catch_title.setParent(frame_titles)
		dates_catch_title.setAlignment(Qt.AlignCenter)

		return frame_titles
