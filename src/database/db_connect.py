import sqlite3
class DatabaseConnection:
    """This class creates a context manager for database connection"""

    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_traceback):
        if exc_type or exc_val or exc_traceback:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()