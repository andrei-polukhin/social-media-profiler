# -*- coding: utf-8 -*-
"""The main GUI window design of the project."""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.backend.backend import main_backend


class Window(QMainWindow):
    """
    Create PyQt GUI window with necessary input fields \
    and connect the submit button to the backend of the project.
    """
    def __init__(self):
        super().__init__()
        uic.loadUi("app/design/ui/main.ui", self)
        self.setWindowTitle("SocialMediaProfiler")
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
        self.extra_field_name = self.findChild(QtWidgets.QLineEdit, "extra_field_name")
        self.extra_field_input = self.findChild(QtWidgets.QLineEdit, "extra_field_input")
        self.directory_text = self.findChild(QtWidgets.QLineEdit, "directory_text")
        # Finding the title label
        self.title_label = self.findChild(QtWidgets.QLabel, "title")
        self.title_label.adjustSize()
        # Finding buttons
        self.select_button = self.findChild(QtWidgets.QPushButton, "select_directory")
        self.submit_button = self.findChild(QtWidgets.QPushButton, "submit_button")
        self.credits_from_menu = self.findChild(QtWidgets.QAction, "actionCredits")
        # Finding the progress bar
        self.progress_bar = self.findChild(QtWidgets.QProgressBar, "app_progress_bar")
        # Connecting buttons to methods
        self.select_button.clicked.connect(self.__choose_directory_as_dialog)
        self.submit_button.clicked.connect(self.__send_input_to_backend)
        self.credits_from_menu.triggered.connect(self.__open_credits_message)

    def __choose_directory_as_dialog(self):
        """Choose the directory on the PC where file will be saved."""
        file = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select the output directory")
        )
        self.directory_text.setText(file)

    def __send_input_to_backend(self):
        """Collect app user's input and send it to the backend of the project."""
        self.progress_bar.setValue(0)
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        location = self.location_input.text()
        company = self.company_input.text()
        job_title = self.job_title_input.text()
        school = self.school_input.text()
        twitter = self.twitter_input.text()
        instagram = self.instagram_input.text()
        extra_field_name = self.extra_field_name.text()
        extra_field_input = self.extra_field_input.text()
        additional_text = self.additional_text.toPlainText()
        if extra_field_name and extra_field_input:
            config_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "location": location,
                "company": company,
                "job_title": job_title,
                "school": school,
                "twitter_profile": twitter,
                "instagram_nickname": instagram,
                "additional_text": additional_text,
                extra_field_name: extra_field_input
            }
        else:
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
        input_fields = [
            self.first_name_input, self.last_name_input, self.location_input,
            self.company_input, self.job_title_input, self.school_input,
            self.twitter_input, self.instagram_input, self.extra_field_name,
            self.extra_field_input, self.additional_text
        ]
        for input_field in input_fields:
            input_field.clear()
        output_directory = self.directory_text.text()
        self.progress_bar.setValue(2)
        main_backend(config_dict, output_directory, self.progress_bar)
        # The backend module sets self.progress_bar.value() to 100%

    @staticmethod
    def __open_credits_message():
        """Open the about message of this project."""
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("This app has been built by Andrew Polukhin")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
