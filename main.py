import sys
from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QVBoxLayout
from PyQt5 import QtCore

from UI_Compiled.interface_qt5 import Ui_MainWindow
from UI_Compiled import CustomWidgets
from task_processing.Workers import ProcessThread
from globals import *


class Display_0(QMainWindow):
    def __init__(self):
        super(Display_0, self).__init__()

        self.started = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.added_widgets = 0

        # scroll area layout
        self.scroll_area_layout = QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(self.scroll_area_layout)

        self.ui.pushButton_start_process.clicked.connect(self.validate_and_start)
        self.ui.pushButton_new_rows.clicked.connect(self.add_custom_widget)

    def add_custom_widget(self):
        self.added_widgets += 1
        new_widget = CustomWidgets.RowWidget(self.added_widgets)
        self.scroll_area_layout.addWidget(new_widget)

    def validate_and_start(self):
        pass

    def add_status_label(self, args):
        label, q_color = args

        item = QListWidgetItem(label)
        item.setBackground(q_color)
        item.setToolTip(f"{label}")

        self.ui.listWidget_status.addItem(item)

    def set_status(self, message):
        self.ui.statusbar.showMessage(message, 5 * 1000)
        self.started -= 1
        if self.started == 0:
            self.ui.pushButton_start_process.setText("Start Process")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Display_0()
    window.show()
    sys.exit(app.exec())
