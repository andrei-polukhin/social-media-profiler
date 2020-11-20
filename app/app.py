# -*- coding: utf-8 -*-
"""The main app module of the project."""

import sys
from PyQt5.QtWidgets import QApplication
from app.design.design import Window


def run() -> None:
    """Run GUI that is already connected to the backend."""
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())
