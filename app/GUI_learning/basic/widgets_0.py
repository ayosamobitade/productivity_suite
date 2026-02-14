from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                               QVBoxLayout, QWidget, QCheckBox, QLabel,
                               QLineEdit, QHBoxLayout, QFormLayout, QComboBox,
                               QSlider, QSpinBox, QProgressBar, QTabWidget)
from PySide6.QtCore import Qt


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # To use all the widgets and see how they look like and should be labelled
        self.setWindowTitle("Widget Showcase")  

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)   
        layout = QVBoxLayout(central_widget)
        # Add a button
        button = QPushButton("Click Me")
        layout.addWidget(button)    
        # Add a checkbox
        checkbox = QCheckBox("Check Me")
        layout.addWidget(checkbox)
        # Add a label
        label = QLabel("This is a label")
        layout.addWidget(label)
        # Add a line edit
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Type here...")
        layout.addWidget(line_edit)
        # Add a horizontal layout with a form layout
        form_layout = QFormLayout()
        form_layout.addRow("Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        layout.addLayout(form_layout)
        # Add a combo box
        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo_box)
        # Add a slider
        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setRange(0, 100)
        layout.addWidget(slider)
        # Add a spin box
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)
        layout.addWidget(spin_box)
        # Add a progress bar
        progress_bar = QProgressBar()
        progress_bar.setValue(50)
        layout.addWidget(progress_bar)
        # Add a tab widget
        tab_widget = QTabWidget()
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("This is the first tab"))
        tab1.setLayout(tab1_layout)
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("This is the second tab"))
        tab2.setLayout(tab2_layout)
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")
        layout.addWidget(tab_widget)
        # Set the main window size
        self.setFixedSize(600, 400)
        # Set the layout to the central widget
        central_widget.setLayout(layout)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()