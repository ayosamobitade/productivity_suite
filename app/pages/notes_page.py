from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class NotePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Note Page")
        layout.addWidget(label)