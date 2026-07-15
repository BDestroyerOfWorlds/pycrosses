#turned out okay
import main
import sys
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt

from main import dead_list
from main import golden_list

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        main_layout = QtWidgets.QVBoxLayout(self)

        def sized_header(text, size=18, colour=None):
            lbl = QtWidgets.QLabel(text)
            font = lbl.font()
            font.setPointSize(size)

            lbl.setFont(font)
            return lbl


        self.golden_list_widget = QtWidgets.QListWidget()
        main_layout.addWidget(sized_header("Golden"))
        main_layout.addWidget(self.golden_list_widget)


        self.dead_list_widget = QtWidgets.QListWidget()
        main_layout.addWidget(sized_header("Dead"))
        main_layout.addWidget(self.dead_list_widget)

        for ticker in golden_list:
            self.add_golden_ticker(ticker)

        for ticker in dead_list:
            self.add_dead_ticker(ticker)

    def add_golden_ticker(self, ticker):
        item = QtWidgets.QListWidgetItem(ticker)
        self.golden_list_widget.addItem(item)

    def add_dead_ticker(self, ticker):
        item = QtWidgets.QListWidgetItem(ticker)
        self.dead_list_widget.addItem(item)




app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec()



#gui actually runs now but the function is shit so it barely works




