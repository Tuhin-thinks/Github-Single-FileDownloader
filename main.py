import re
import sys
from functools import partial
from copy import deepcopy
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QVBoxLayout
from PyQt5 import QtCore

from UI_Compiled.interface_qt5 import Ui_MainWindow
from UI_Compiled import CustomWidgets
from Utils import shortcuts
from task_processing.Workers import ProcessThread
from globals import *


class Display_0(QMainWindow):
    def __init__(self):
        super(Display_0, self).__init__()

        self.added_regexes = 0
        self.added_regex_widgets: List['CustomWidgets.RegexRowWidget'] = []
        self.started = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.added_widgets = 0
        self.added_widget_list = []
        self.threadpool = QtCore.QThreadPool()
        self.max_thread_count = self.threadpool.maxThreadCount()

        # scroll area layout
        self.scroll_area_layout = QVBoxLayout()
        self.ui.scrollAreaWidgetContents.setLayout(self.scroll_area_layout)

        self.scroll_area_layout_0 = QVBoxLayout()
        self.ui.scrollAreaWidgetContents_2.setLayout(self.scroll_area_layout_0)

        # widget modifications
        self.ui.pushButton_new_regex_row.setToolTip("add new regex rule")
        self.ui.pushButton_new_rows.setToolTip("add new task")
        # self.ui.lineEdit_replace_text.setToolTip("some text to replace the matching with...")

        self.add_regex_row_widget()  # add a regex string and replace text row

        self.ui.pushButton_start_process.clicked.connect(self.validate_and_start)
        self.ui.pushButton_new_rows.clicked.connect(self.add_custom_widget)
        self.ui.pushButton_new_regex_row.clicked.connect(self.add_regex_row_widget)
        self.ui.pushButton_export.clicked.connect(self.export_regex_rules)

    def export_regex_rules(self):
        """
        create rule data and dump into json
        :return:
        """
        export_data = []
        for widgets in self.added_regex_widgets:
            regex_string = widgets.regex_string
            replace_text = widgets.replace_text
            export_data.append(
                {'regex-string': regex_string, 'replace-text': replace_text}
            )
        with open('regex_data.json', 'w') as regex_rule_data:
            json.dump(export_data, regex_rule_data, indent=3)

    def add_regex_row_widget(self):
        self.added_regexes += 1
        new_widget = CustomWidgets.RegexRowWidget(self.added_regexes)
        self.added_regex_widgets.append(new_widget)
        self.scroll_area_layout_0.addWidget(new_widget)

    def add_custom_widget(self):
        self.added_widgets += 1
        new_widget = CustomWidgets.RowWidget(self.added_widgets)
        self.added_widget_list.append(new_widget)  # store new widget reference to a list
        self.scroll_area_layout.addWidget(new_widget)

    def validate_and_start(self):
        task_list = []
        g_manipulator = self.added_regex_widgets[0].regex_string

        if g_manipulator:
            pass
        else:
            return

        for widget_index, custom_widget in enumerate(self.added_widget_list):
            custom_widget: 'CustomWidgets.RowWidget'
            flag_valid = False
            task_dict = deepcopy({'download-link': None,
                                  'save-as': None,
                                  'manipulator': None,
                                  'widget-instance': widget_index})

            download_link = custom_widget.lineEdit_download_link.text()
            save_as = custom_widget.lineEdit_save_as.text()
            sub_link_manipulator = custom_widget.lineEdit_manipulator.text()

            if download_link and save_as and shortcuts.ping_address(download_link):  # validate link & add to task-list
                task_dict['download-link'] = download_link
                task_dict['save-as'] = save_as
                flag_valid = True  # mark current task as valid (all data passed condition) and add to task-list
            else:
                custom_widget.label_status.setText("Save as is empty or download link is not valid/accessible")
                task_list.clear()
                return

            task_dict['manipulator'] = sub_link_manipulator  # sub line manipulator to be checked during actual scraping

            if flag_valid:  # check if current task is valid, thus add this task to task-list
                task_list.append(task_dict)

        regex_strings = []
        replace_strings = []
        for widget in self.added_regex_widgets:
            regex_strings.append(widget.regex_string)
            replace_strings.append(widget.replace_text)

        job_dict = {'task-list': task_list, 'regex-strings': regex_strings,
                    'replace-texts': replace_strings}
        self.start_download(job_dict)

    def start_download(self, job_dict):
        regex_list = job_dict['regex-strings']
        replace_text_list = job_dict['replace-texts']

        task_list = job_dict['task-list']

        runnables = []
        for task_index, task_dict in enumerate(task_list):
            task_dict: Dict

            # unpack variable-values
            download_link = task_dict['download-link']
            save_as = task_dict['save-as']
            sub_manipulator = task_dict['manipulator']  # TODO: make this feature to override global regex when present

            mod_link = download_link
            for regex_string, replace_text in zip(regex_list, replace_text_list):
                print(f"regex={regex_string},\n"
                      f"replace_text={replace_text},\n"
                      f"mod_link={mod_link}")
                try:
                    temp = re.sub(regex_string, replace_text, mod_link)
                    mod_link = temp
                except Exception as e:
                    print(e.__str__())
                finally:
                    print(mod_link)

            runnable = ProcessThread({"download-link": mod_link, 'save_as': save_as})

            args = f"Completed task: {task_index+1}", shortcuts.select_color_codes()
            runnable.signals.finished.connect(partial(self.add_status_label, args))
            runnables.append(runnable)

        self.started = len(runnables)  # instance variable to keep track, when to re-enable `start-task` button
        self.ui.pushButton_start_process.setDisabled(True)  # disable start button, while downloads in progress

        # start all runnable in the threadpool
        for runnable in runnables:
            self.threadpool.start(runnable)

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
