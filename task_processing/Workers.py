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

    def __init__(self, parameters: dict):
        super(ProcessThread, self).__init__()

        self.parameters = parameters
        self.signals = WorkerSignals()

    @QtCore.pyqtSlot()
    def run(self) -> None:
        download_link = self.parameters['download-link']
        save_as = self.parameters['save_as']

        file_downloader.download_file_from_link(file_name=save_as,
                                                link=download_link)

        self.signals.finished.emit()
