import sqlite3

def connect_db():
    conn = sqlite3.connect("users.db")
    return conn