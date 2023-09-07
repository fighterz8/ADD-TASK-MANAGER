from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self, window1, window2):
        super().__init__()
        self.window1 = window1
        self.window2 = window2
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        slider1_label = QLabel("Window 1")
        slider2_label = QLabel("Window 2")
        
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 300)  # 0 to 300 seconds (5 minutes)
        self.slider1.valueChanged.connect(self.updateTime1)  # Modified line
        
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 300)  # 0 to 300 seconds (5 minutes)
        self.slider2.valueChanged.connect(self.updateTime2)  # Modified line

        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.reset_button = QPushButton("Reset")
        
        self.start_button.clicked.connect(self.start_timers)
        
     
        self.start_button.clicked.connect(self.window1.timer_logic.start)
        self.start_button.clicked.connect(self.window2.timer_logic.pause)
        
        self.pause_button.clicked.connect(self.window1.timer_logic.pause)
        self.pause_button.clicked.connect(self.window2.timer_logic.pause)
        
        self.reset_button.clicked.connect(self.window1.timer_logic.reset)
        self.reset_button.clicked.connect(self.window2.timer_logic.reset)
        self.reset_button.clicked.connect(self.reset_timers_and_sliders)

        layout.addWidget(slider1_label)
        layout.addWidget(self.slider1)
        layout.addWidget(slider2_label)
        layout.addWidget(self.slider2)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.reset_button)
        
        self.setLayout(layout)
    
    def closeEvent(self, event):
        self.window1.close()
        self.window2.close()
        event.accept()

    def reset_timers_and_sliders(self):
        self.slider1.setValue(0)
        self.slider2.setValue(0)
        self.window1.timer_logic.reset()
        self.window2.timer_logic.reset()
    
    # New methods to update time based on the sliders
    def start_timers(self):
        self.window1.timer_logic.start()
        self.window2.timer_logic.pause()
        
    def updateTime1(self, value):
        self.window1.timer_logic.setTime(value)
        self.window1.timer_logic.updateCounterLabel(self.window1.timer_label, value)
    
    def updateTime2(self, value):
        self.window2.timer_logic.setTime(value)
        self.window2.timer_logic.updateCounterLabel(self.window2.timer_label, value)