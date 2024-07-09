import random, sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from models import *
from  models.app_function import create_DB
from UI.UI_CODE_FILES import Main_Page


# self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def main():
	create_DB()
	app = QApplication(sys.argv)  # create the app
	main_page = Main_Page()  # create main page
	main_page.show()
	app.exec_()

if __name__ == '__main__':
	main()
