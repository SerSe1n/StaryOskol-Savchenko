import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.do_paint = False
        self.btn = QPushButton('btn', self)
        self.btn.clicked.connect(self.update_picture)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(color)
            qp.setBrush(color)
            a = randint(20, 250)
            qp.drawEllipse((800 - a) // 2, 300, a, a)
            qp.end()
            self.do_paint = False

    def update_picture(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())