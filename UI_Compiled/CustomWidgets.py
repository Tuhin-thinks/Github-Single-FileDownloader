from . import custom_widget

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject


class RowWidget(QWidget, custom_widget.Ui_custom_downloader_widget):
    def __init__(self, name: int):
        super(RowWidget, self).__init__()
        self.setupUi(self)

        self.label_status.setText(f"Pending - {name}")
