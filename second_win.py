from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def next_click(self):
        self.tw = FinalWin
        self.hide()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.text_age = QLabel(txt_age)
        self.text_name = QLabel(txt_name)

        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.text_timer = QLabel(txt_timer)
        self.line_age = QLabel(txt_hintage)
        self.line_name = QLabel(txt_hintname)

        self.line_test1 = QLabel(txt_hinttest1)
        self.line_test2 = QLabel(txt_hinttest2)
        self.line_test3 = QLabel(txt_hinttest3)

        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next,alignment=Qt.AlignLeft)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
app = QApplication([])
tw = TestWin()
app.exec()