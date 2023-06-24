from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SizeCalc")
        self.setWindowIcon(QIcon("goblin.png"))
        self.setFixedHeight(650)
        self.setFixedWidth(1100)
        self.setStyleSheet("background-color:red")


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())