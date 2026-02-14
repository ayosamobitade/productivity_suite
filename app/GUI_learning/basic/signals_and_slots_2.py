from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Own Application")

        self.button = QPushButton("Press me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)
      

    def the_button_was_clicked(self):
        self.button.setText("Yout already clicked me!")
        self.button.setEnabled(False)

        # Also change the window title
        self.setWindowTitle("My Oneshot App!")

        print("Button was clicked!")

app = QApplication(sys.argv)    

window = MainWindow()
window.show()

app.exec()