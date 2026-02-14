from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Own Application")

        button = QPushButton("Press me")
        button.setCheckable(True)

        button.clicked.connect(self.on_button_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def on_button_clicked(self):
        print("Button was clicked!")

    def the_button_was_toggled(self, checked):
        print(f"Button toggled: {'Checked' if checked else 'Unchecked'}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()