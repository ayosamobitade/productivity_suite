from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from PySide6.QtCore import Qt


class LearningWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Learning Application")


        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")
        viewMenu = menubar.addMenu("View")
        helpMenu = menubar.addMenu("Help")  

        submenu = fileMenu.addMenu("File Submenu")
        anothersubmenu = fileMenu.addMenu("Another Submenu")

        mumuAction = anothersubmenu.addAction("Mumu")
        exisAction = submenu.addAction("Exit")
        thankYou = submenu.addAction("Thank You")

        exisAction.triggered.connect(self.close)
        



app = QApplication()

window = LearningWindow()
window.show()

app.exec()
   
     