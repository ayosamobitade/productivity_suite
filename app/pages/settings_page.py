from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("Settings Page")
        layout.addWidget(label)