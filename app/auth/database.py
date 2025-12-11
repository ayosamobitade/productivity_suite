import sqlite3
import os

DB_PATH = "app.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn