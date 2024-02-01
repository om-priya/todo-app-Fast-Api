from database.db_connect import DatabaseConnection
from config.sql_queries import SqlQuery


class DatabaseAccess:
    DB_PATH = "todo.db"

    # execute query of non returning type such as update, delete, insert
    @classmethod
    def execute_non_returning_query(cls, query, params=None):
        """Execute a non-returning query (update, delete, insert)."""
        with DatabaseConnection(cls.DB_PATH) as connection:
            cursor = connection.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

    # execute query of returning type such as read
    @classmethod
    def execute_returning_query(cls, query, params=None):
        """Execute a returning query (read)."""
        with DatabaseConnection(cls.DB_PATH) as connection:
            cursor = connection.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            data_from_db = cursor.fetchall()
        return data_from_db
