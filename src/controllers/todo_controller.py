import shortuuid

from config.sql_queries import SqlQuery
from database.db_access import DatabaseAccess


def get_all_todo(user_id):
    res_data = DatabaseAccess.execute_returning_query(SqlQuery.GET_ALL_TODO, (user_id,))
    return res_data


def create_todo(title, description, priority, user_id):
    todo_id = shortuuid.ShortUUID().random(length=8)
    params = (todo_id, priority, description, user_id, title)
    DatabaseAccess.execute_non_returning_query(SqlQuery.INSERT_TODO_TABLE, params)


def update_todo(title, description, priority, todo_id):
    params = (title, priority, description, todo_id)
    DatabaseAccess.execute_non_returning_query(SqlQuery.UPDATE_TODO, params)
