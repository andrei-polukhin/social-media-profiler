# -*- coding: utf-8 -*-

import sys
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from app.design.design import Window


class TestDesign(unittest.TestCase):
    app = QApplication(sys.argv)
    design_object = Window()

    def test_check_existence_of_all_elements(self):
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "first_name_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "last_name_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "location_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "company_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "job_title_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "school_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "twitter_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "instagram_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QTextEdit, "additional_info_field"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QLineEdit, "directory_text"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QPushButton, "select_directory"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QPushButton, "submit_button"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QAction, "actionCredits"))
        self.assertIsNotNone(TestDesign.design_object.findChild(QtWidgets.QProgressBar, "app_progress_bar"))

    def test_getting_values_from_inputs(self):
        self.assertIsInstance(TestDesign.design_object.first_name_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.last_name_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.location_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.company_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.job_title_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.school_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.twitter_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.instagram_input.text(), str)
        self.assertIsInstance(TestDesign.design_object.additional_text.toPlainText(), str)

    def test_setting_values_to_input_fields(self):
        # Testing QLineEdit
        initial_value_of_qline_edit = TestDesign.design_object.company_input.text()
        TestDesign.design_object.company_input.setText("some arbitrary text in here")
        end_value_of_qline_edit = TestDesign.design_object.company_input.text()
        self.assertNotEqual(initial_value_of_qline_edit, end_value_of_qline_edit)
        # Testing QTextEdit
        initial_value_of_qtext_edit = TestDesign.design_object.additional_text.toPlainText()
        TestDesign.design_object.additional_text.setText("some arbitrary text in here")
        end_value_of_qtext_edit = TestDesign.design_object.additional_text.toPlainText()
        self.assertNotEqual(initial_value_of_qtext_edit, end_value_of_qtext_edit)

    def test_progress_bar(self):
        progress_bar = TestDesign.design_object.findChild(QtWidgets.QProgressBar, "app_progress_bar")
        self.assertEqual(progress_bar.value(), 0)
        self.assertIsNone(progress_bar.setValue(28))
        self.assertEqual(progress_bar.value(), 28)


if __name__ == '__main__':
    unittest.main()
