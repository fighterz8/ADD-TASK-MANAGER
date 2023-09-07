from PyQt5.QtCore import QTimer

class TimerLogic:
    def __init__(self, window, sibling_timer=None, slider=None):
        self.window = window
        self.sibling_timer = sibling_timer
        self.slider = slider
        self.time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)

    def setTime(self, seconds):
        self.time = seconds

    def start(self):
        self.timer.start(1000)

    def pause(self):
        self.timer.stop()

    def reset(self):
        self.time = 0
        self.updateCounterLabel(self.window.timer_label, self.time)  # Reset to 0

    def updateTime(self):
        if self.time > 0:
            self.time -= 1
        else:
            self.pause()
            if self.sibling_timer:
                self.sibling_timer.start()
                self.setTime(self.slider.value())
        self.updateCounterLabel(self.window.timer_label, self.time)


    def updateCounterLabel(self, label, seconds):
        if seconds < 60:
            label.setText(str(seconds)) 
        else:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            label.setText(f"{minutes}:{remaining_seconds:02}")