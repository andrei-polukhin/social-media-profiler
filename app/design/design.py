import sys
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        # Finding input fields
        self.first_name_input = self.findChild(QtWidgets.QLineEdit, "first_name_field")
        self.last_name_input = self.findChild(QtWidgets.QLineEdit, "last_name_field")
        self.location_input = self.findChild(QtWidgets.QLineEdit, "location_field")
        self.company_input = self.findChild(QtWidgets.QLineEdit, "company_field")
        self.job_title_input = self.findChild(QtWidgets.QLineEdit, "job_title_field")
        self.school_input = self.findChild(QtWidgets.QLineEdit, "school_field")
        self.twitter_input = self.findChild(QtWidgets.QLineEdit, "twitter_field")
        self.instagram_input = self.findChild(QtWidgets.QLineEdit, "instagram_field")
        self.additional_text = self.findChild(QtWidgets.QTextEdit, "additional_info_field")


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
