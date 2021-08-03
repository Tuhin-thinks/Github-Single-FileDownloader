from . import custom_widget
from . import regex_row_widget

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject


class RowWidget(QWidget, custom_widget.Ui_custom_downloader_widget):
    def __init__(self, name: int):
        super(RowWidget, self).__init__()
        self.setupUi(self)

        self.label_status.setText(f"Pending - {name}")


class RegexRowWidget(QWidget, regex_row_widget.Ui_Form):
    def __init__(self, widget_id: int):
        super(RegexRowWidget, self).__init__()
        self.setupUi(self)

        self.label_sequence.setText(str(widget_id))

    @property
    def regex_string(self):
        return self.lineEdit_global_manipulator.text()

    @regex_string.setter
    def regex_string(self, string: str):
        self.lineEdit_global_manipulator.setText(string)

    @property
    def replace_text(self):
        return self.lineEdit_replace_text.text()

    @replace_text.setter
    def replace_text(self, replace_string: str):
        self.lineEdit_replace_text.setText(replace_string)
