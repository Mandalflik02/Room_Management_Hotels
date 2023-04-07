


OK_CODE = 111

DELETE_CODE = 633


MAX_ORDERS_CODE =996

ROOM_ERROR_CODE = 997

VERABLE_ERROR_CODE = 998

ERROR_CODE = 999



ORDERS=[]  # list of orders

ORDERS_HISTORY=[]# list of old orders

ROOMS=[]  # list of room

LOGS=[]  # list of logs



stop_time_thread=False
CURRENT_USER="TEST-USER"


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



