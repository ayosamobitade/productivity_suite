from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# you only need one QApplication instance. it is used to allow the GUI to run
# and to handle events. ie command line arguments and window events
app = QApplication(sys.argv)

# Create a main window instance
window = QWidget()

# window are hidden by default, so we need to show it
window.show()

# start the event loop
app.exec()