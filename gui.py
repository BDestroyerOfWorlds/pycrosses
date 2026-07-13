#this will be so ass
import main
import sys
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QListView, QWidget

from main import dead_list


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.centralWidget()

        self.list_view = QListView

        self.model = QStringListModel(dead_list)

        self.list_view.setModel(self.model)
        layout.addWidget(self.list_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#this shit doesnt even run yet dont even bother with it




