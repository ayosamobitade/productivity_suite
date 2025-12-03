from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productivity Suite")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        self.button.setText("Clicked!")
        print("Button was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





