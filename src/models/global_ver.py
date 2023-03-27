

OK_CODE = 357
ERROR_CODE = 999
DELETE_CODE = 633

ORDERS=[]  # list of orders
ORDERS_HISTORY=[]# list of old orders
ROOMS=[]  # list of room
LOGS=[]  # list of logs


stop_time_thread=False
LOGIN_USER="TEST-USER"

windows_indexes = {
	"home-menu": 0,
	"new-order": 1,
	"rooms-view": 2,
	"view-order": 3,
	"view-room": 4,
	"settings": 5,
	"manager-page": 6,
	"login-create":7,
	"msg-box": 33,
}  # A list of all the indexes of each page



def create_msg_dialog(msg,btn1_text,btn2_text):
	dialog = MSG_Dialog("go to rooms", "bobo1", "gogo2")
	dialog.exec_()
	status = dialog.status
	print(status)


