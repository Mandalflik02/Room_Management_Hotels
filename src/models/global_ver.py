

OK_CODE = 357


ORDERS=[]  # list of orders
ROOMS=[]  # list of room
LOGS=[]  # list of logs


stop_time_thread=False


windows_indexes = {
	"home-menu": 0,
	"new-order": 1,
	"rooms-view": 3,
	"view-order": 2,
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


