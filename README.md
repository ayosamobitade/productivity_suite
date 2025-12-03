# Productivity Suite Desktop App

A **cross-platform desktop application** built with **PySide6 (Qt for Python)**.  
This project is a **full-featured personal productivity suite** including:

- Notes  
- Tasks / To-Do List  
- Calendar  
- Dashboard  
- File Manager  
- Image Viewer  
- Media Player  
- Settings & Themes  

The app is designed to **teach PySide6 fundamentals**, **desktop app architecture**, and **professional project structuring**.

---

## Table of Contents

- [Features](#features)  
- [Screenshots](#screenshots)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies](#technologies)  
- [Contributing](#contributing)  
- [License](#license)

---

## Features

### Core Modules
- **Notes** – Create, edit, delete notes, autosave feature  
- **Tasks** – Add, complete, delete tasks, SQLite database storage  
- **Calendar** – Event management and reminders  
- **Dashboard** – Display charts of tasks, notes, and activity  
- **File Manager** – Browse directories and open files  
- **Image Viewer** – Zoom, rotate, and preview images  
- **Media Player** – Play audio/video files with playlist support  
- **Settings** – Dark/Light mode, font preferences, persistent user configs

---

## Screenshots

*(Add screenshots here once the UI is ready)*

---

## Project Structure

```
productivity_suite/
│
├── venv/ # Virtual environment
├── requirements.txt # Project dependencies
├── main.py # Entry point of the app
├── app/ # Main application package
│ ├── init.py
│ ├── main_window.py # Main window with QStackedWidget
│ ├── sidebar.py # Sidebar navigation
│ ├── pages/ # Individual pages/modules
│ │ ├── init.py
│ │ ├── home_page.py
│ │ ├── notes_page.py
│ │ ├── tasks_page.py
│ │ └── settings_page.py
│ ├── ui/ # Optional .ui files from Qt Designer
│ └── widgets/ # Custom widgets
│ └── init.py
├── README.md
└── .gitignore
```


---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ayosamobitade/productivity_suite.git
cd my_pyside6_app
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

```

## Usage

Run the application:
```bash
python main.py
```

You should see the Main Window with the sidebar navigation.
Click the buttons to switch between Home, Notes, Tasks, and Settings pages.

## Technologies

- Python 3.11+
- PySide6 (Qt for Python)
- SQLite – For local database storage
- Qt Designer – Optional UI design tool
- PyInstaller – For packaging into executables

## Contributing

Contributions are welcome! Here’s how to contribute:

- Fork the repository
- Create a feature branch (git checkout -b feature/YourFeature)
- Commit your changes (git commit -m "Add some feature")
- Push to the branch (git push origin feature/YourFeature)
- Create a pull request

## License

This project is licensed under the MIT License.
See the LICENSE

file for details.

## Contact

Developed by Your Name – ayosamobitade @gmail.com

GitHub: https://github.com/ayosamobitade

## Notes

- Designed as a learning project to master PySide6 and desktop app development.
- Can be extended with Notes search, advanced task filtering, calendar events, and more.
- All assets (icons, images) should be stored in the app/ui folder for organization.


---
