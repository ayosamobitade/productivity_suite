# window can be anything not just the main window
# and to handle events. i.e., command line arguments and window events


from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Only needed for access to command line arguments
import sys

# YOu only need one QApplication instance. It is used to allow the GUI to run

app = QApplication(sys.argv)

window = QPushButton("Click Me")

window.show()

#Starting the event loop
app.exec()