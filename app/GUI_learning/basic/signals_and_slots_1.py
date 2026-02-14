from PySide6.QtWidgets import QApplication, QWidget, QPushButton

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Own Application")

        button = QPushButton("Press me")
        button.setCheckable(True)
        button.clicked.connect(self.on_button_clicked)

        self.setCentralWidget(button)

        
    def on_button_clicked(self):
        print("Button was clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()