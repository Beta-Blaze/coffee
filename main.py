import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.textBrowser.setText(self.text())

    def text(self):
        list1 = []
        bd = sqlite3.connect('coffee.sqlite')
        cur = bd.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        for elem in result:
            list1.append(', '.join(map(lambda x: str(x), elem)))
        bd.close()
        return '\n'.join(list1)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
