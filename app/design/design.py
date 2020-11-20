# -*- coding: utf-8 -*-
"""The main GUI window design of the project."""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from app.backend.backend import main_backend


class Window(QMainWindow):
    """
    Create PyQt GUI window with necessary input fields \
    and connect the submit button to the backend of the project.
    """
    def __init__(self):
        super().__init__()
        uic.loadUi("app/design/ui/main.ui", self)
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
        self.directory_text = self.findChild(QtWidgets.QLineEdit, "directory_text")
        # Finding buttons
        self.select_button = self.findChild(QtWidgets.QPushButton, "select_directory")
        self.submit_button = self.findChild(QtWidgets.QPushButton, "submit_button")
        # Connecting buttons to methods
        self.select_button.clicked.connect(self.choose_directory_as_dialog)
        self.submit_button.clicked.connect(self.send_input_to_backend)

    def choose_directory_as_dialog(self):
        """Choose the directory on the PC where file will be saved."""
        file = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select the output directory")
        )
        self.directory_text.setText(file)

    def send_input_to_backend(self):
        """Collect app user's input and send it to the backend of the project."""
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        location = self.location_input.text()
        company = self.company_input.text()
        job_title = self.job_title_input.text()
        school = self.school_input.text()
        twitter = self.twitter_input.text()
        instagram = self.instagram_input.text()
        additional_text = self.additional_text.toPlainText()
        config_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "location": location,
            "company": company,
            "job_title": job_title,
            "school": school,
            "twitter_profile": twitter,
            "instagram_nickname": instagram,
            "additional_text": additional_text
        }
        output_directory = self.directory_text.text()
        main_backend(config_dict, output_directory)
