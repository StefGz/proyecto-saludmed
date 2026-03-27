import sqlite3
import atexit 

class Connection:

    def __init__(self, data_path):
        self.database = data_path
        self.conn = sqlite3.connect(self.database)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params = ()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error:
            self.conn.rollback()
            raise

    def get_all(self, query, params = ()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error:
            raise

    def get_one(self, query, params = ()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error:
            raise
            
    def close_connection(self):
        if self.conn:
            self.conn.close()

db_connection = Connection("database/data_saludmed.db")

atexit.register(db_connection.close_connection)