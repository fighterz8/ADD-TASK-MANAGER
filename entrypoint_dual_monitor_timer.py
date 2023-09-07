
import sys
from PyQt5.QtWidgets import QApplication
from timer_logic import TimerLogic
from main_window import MainWindow
from control_panel import ControlPanel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Initialize main windows first so we can pass them to the TimerLogic
    window1 = MainWindow(1)
    window2 = MainWindow(2)
    
    # Initialize timer logics
    timer_logic1 = TimerLogic(window1)
    timer_logic2 = TimerLogic(window2)
    
    # Set timer logic for each window
    window1.timer_logic = timer_logic1
    window2.timer_logic = timer_logic2
    
    control_panel = ControlPanel(window1, window2)
    
    # Set sibling timers
    timer_logic1.sibling_timer = timer_logic2
    timer_logic2.sibling_timer = timer_logic1
    
    # Set sliders
    timer_logic1.slider = control_panel.slider1
    timer_logic2.slider = control_panel.slider2

    control_panel.show()
    
    # Set the position of the windows and show them
    window1.move(1750, 0)  # Top left corner of the first monitor
    window1.show()
    
    window2.move(3670, 0)  # Top right corner, assuming a 1920x1080 resolution for the first monitor
    window2.show()
    
    sys.exit(app.exec_())