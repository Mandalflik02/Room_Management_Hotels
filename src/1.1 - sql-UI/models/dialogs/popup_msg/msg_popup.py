from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class MSG_Popup(QDialog):
    def __init__(self, label_text):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(MSG_Popup, self).__init__()
        loadUi("models/dialogs/popup_msg/msg_popup.ui", self)  # load the UI of the page

        self.msg_label.setText(label_text)
        self.setWindowTitle(label_text)

        self.msg_btn_1.setText("OK")
        self.msg_btn_1.clicked.connect(self.btn1_click)

    def btn1_click(self):
        self.close()
