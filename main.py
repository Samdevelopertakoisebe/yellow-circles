import random
from threading import Timer
from PyQt5.QtWidgets import QMainWindow, QAbstractButton, QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QFont, QIcon, QPixmap, QColor, QBrush
from PyQt5 import QtCore, Qt
import sys


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("создать", self)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 750, 400, 460)

        self.button.setGeometry(175, 5, 50, 50)
        self.button.clicked.connect(self.click_event)

        self.map = QPixmap(400, 400)
        self.map.fill(QColor("White"))

        self.map_holder = QLabel(self)
        self.map_holder.setGeometry(0, 50, 400, 400)
        self.map_holder.setPixmap(self.map)

    def click_event(self):
        self.brush = QPainter(self.map_holder.pixmap())
        self.brush.setBrush(QColor("yellow"))
        a = random.randint(1, 400)
        self.brush.drawEllipse(*[random.randint(-100, 300) for _ in range(2)], a, a)
        self.brush.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
