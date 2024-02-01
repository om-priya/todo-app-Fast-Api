from database.db_access import DatabaseAccess
from config.sql_queries import SqlQuery


def check_credentials(email, password):
    params = (email, password)
    res_data = DatabaseAccess.execute_returning_query(SqlQuery.FETCH_USER, params)
    if not res_data:
        return None
    user_id = res_data[0][0]
    return user_id


def sign_up(user_id, email, password):
    params = (user_id, email, password)
    DatabaseAccess.execute_non_returning_query(SqlQuery.INSERT_CRED_TABLE, params)
