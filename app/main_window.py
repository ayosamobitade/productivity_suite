from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QStackedWidget


import sys
class MainWindow(QMainWindow):
    def __init__(self, sidebar):
        super().__init__()

        self.setWindowTitle("My Productivity App")
        self.setMinimumSize(1000, 600)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        # horizontal layout
        layout = QHBoxLayout(central)

        # Sidebar passed into main window
        self.sidebar = sidebar
        layout.addWidget(self.sidebar)

        # stacked pages
        self.pages = QStackedWidget()
        layout.addWidget(self.pages)


    def add_page(self, widget):
        '''Add a new page to the stacked widget'''
        self.pages.addWidget(widget)


    def switch_page(self, index):
        '''Switch to the page at the given index'''
        self.pages.setCurrentIndex(index)







