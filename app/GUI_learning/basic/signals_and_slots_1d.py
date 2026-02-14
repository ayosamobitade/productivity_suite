from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My Own Application")

        self.button = QPushButton("Press me")
        self.button.setCheckable(True)
        self.button.released.connect(self.on_button_was_released)
        self.button.setChecked(self.button_is_checked)  

        #set the center widget of the main window
        self.setCentralWidget(self.button)

    def on_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        
        # Print the current state of the button
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()