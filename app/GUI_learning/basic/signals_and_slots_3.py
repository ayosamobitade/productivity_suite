from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

from random import choice

window_titles = [
    "my App",
    "My App",
    "My Own Application", 
    "Another Window", 
    "Sample Window",
    "Test Window",
    "Demo Application",
    "Example App",
    "Sample App",
    "Something went wrong!"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My Own Application")

        self.button = QPushButton("Press me")
        self.button.clicked.connect(self.on_button_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def on_button_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed to: %s" % window_title)

        if window_title == "Something went wrong!":
            self.button.setDisabled(True)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()