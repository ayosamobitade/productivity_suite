from PySide6.QtWidgets import QApplication
import sys

from app.main_window import MainWindow
from app.sidebar import Sidebar
from app.pages.home_page import HomePage
from app.pages.settings_page import SettingsPage
from app.pages.notes_page import NotePage    
from app.pages.tasks_page import TasksPage

def main():
    app = QApplication(sys.argv)

    # Create sidebar
    sidebar = Sidebar()

    # Create main window with sidebar
    window = MainWindow(sidebar)

    # Create pages
    home_page = HomePage()
    notes_page = NotePage()
    tasks_page = TasksPage()
    settings_page = SettingsPage()

    # Add pages to main window
    window.add_page(home_page) # index 0
    window.add_page(notes_page) # index 1
    window.add_page(tasks_page) # index 2
    window.add_page(settings_page) # Index 3

    # Connect sidebar buttons to switch pages
    sidebar.btn_home.clicked.connect(lambda: window.switch_page(0))
    sidebar.btn_notes.clicked.connect(lambda: window.switch_page(1))
    sidebar.btn_tasks.clicked.connect(lambda: window.switch_page(2))
    sidebar.btn_settings.clicked.connect(lambda: window.switch_page(3))

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()