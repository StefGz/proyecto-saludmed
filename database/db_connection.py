"""
Database connection module with singleton pattern for SQLite.

This module provides a singleton class DatabaseConnection that manages
a single SQLite connection throughout the application.
"""

import sqlite3
import atexit
from database.db_exception import DatabaseException

class DatabaseConnection:

    """
    Singleton class for managing SQLite database connections.

    This class ensures only one database connection exists throughout the
    application. It provides methods for executing queries and retrieving data.
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
        Create and return the unique instance of the class.

        Args:
            *args: Variable length argument list (passed to __init__).
            **kwargs: Arbitrary keyword arguments (passed to __init__).

        Returns:
            DatabaseConnection: The singleton instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data_path):
        """
        Initialize the database connection and enable foreign key support.

        Args:
            data_path (str): Path to the SQLite database file.

        Raises:
            DatabaseException: If the connection to the database fails.
        """
        if DatabaseConnection._initialized:
            return
        self.database = data_path
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.database)
            self.conn.execute("PRAGMA foreign_keys = ON")
            DatabaseConnection._initialized = True
        except sqlite3.Error as e:
            raise DatabaseException(f"Error connecting to database: {e}")
        
    def execute_query(self, query, params = ()):
        """
        Execute a data modification query (INSERT, UPDATE, DELETE).

        Args:
            query (str): SQL query string with placeholders.
            params (tuple, optional): Values to safely substitute into the placeholders.
            Defaults to an empty tuple.

        Returns:
            bool: True if the operation was successful.

        Raises:
            DatabaseException: If an error occurs during the execution of the query.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            self.conn.rollback()
            raise DatabaseException(f"Error executing database operation: {e}") 

    def get_all(self, query, params = ()):
        """
        Execute a SELECT query and return all rows.

        Args:
            query (str): SQL query string with placeholders.
            params (tuple, optional): Values to safely substitute into the placeholders.
            Defaults to an empty tuple.

        Returns:
            list: A list of tuples, each representing a row.

        Raises:
            DatabaseException: If an error occurs while querying the database.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise DatabaseException(f"Error querying database: {e}") 

    def get_one(self, query, params = ()):
        """
        Execute a SELECT query and return the first row.

        Args:
            query (str): SQL query string with placeholders.
            params (tuple, optional): Values to safely substitute into the placeholders.
            Defaults to an empty tuple.

        Returns:
            tuple or None: The first row as a tuple, or None if no results.

        Raises:
            DatabaseException: If an error occurs while querying the database.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except sqlite3.Error as e:
            raise DatabaseException(f"Error querying database: {e}") 
            
    def close_connection(self):
        """
        Close the database connection if it is open.
        """
        if self.conn:
            self.conn.close()

# Singleton instance
db_connection = DatabaseConnection("database/data_saludmed.db")

# Auto-close connection on program exit
atexit.register(db_connection.close_connection)
