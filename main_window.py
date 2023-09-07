
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, screen_number):
        super().__init__()
        self.timer_logic = None  # Initialize to None, will set this later from the entrypoint
        self.initUI(screen_number)
        self.dragPosition = None

    def initUI(self, screen_number):
        self.setWindowTitle(f"Timer - Screen {screen_number}")
        self.timer_label = QLabel('00:00', self)
        self.timer_label.setFont(QFont('Digital-7', 48))
        self.timer_label.resize(200, 100)
        self.timer_label.move(0, 10)
        self.resize(160, 100)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  
    
       

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()