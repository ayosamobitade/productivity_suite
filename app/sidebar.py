from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.btn_home = QPushButton("Home")
        self.btn_notes = QPushButton("Notes")
        self.btn_tasks = QPushButton("Tasks")
        self.btn_settings = QPushButton("Settings")

        layout.addWidget(self.btn_home)
        layout.addWidget(self.btn_notes)
        layout.addWidget(self.btn_tasks)
        layout.addWidget(self.btn_settings)

        layout.addStretch()  # Push buttons to the top

