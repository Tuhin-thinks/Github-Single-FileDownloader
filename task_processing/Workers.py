import random

from PyQt5 import QtCore, QtGui
from Utils import file_downloader, shortcuts

import globals


class WorkerSignals(QtCore.QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple`

    result
        `object` data returned from processing, anything
    """
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)


class ProcessThread(QtCore.QRunnable):

    def __init__(self, parameters: dict, name: str):
        super(ProcessThread, self).__init__()

        self.parameters = parameters
        self.name = name
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self) -> None:
        max_threads = self.parameters['max_threads']
        for i in range(max_threads):
            if globals.TERMINATION_FLAG[0]:
                break
            r, g, b = shortcuts.select_color_codes()
            q_color = QtGui.QColor(r, g, b)
            self.signals.result.emit((f"[*] started: {i + 1} - {self.name}", q_color))
            file_downloader.download_file_from_link(f"contents_{random.random() * 1000}.zip",
                                                    "http://212.183.159.230/50MB.zip")
            self.signals.result.emit((f"[+] complete: {i + 1} - {self.name}", q_color))
        self.signals.finished.emit()
